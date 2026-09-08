/*
 * Cross-linking, hover previews, and click-to-split-pane for rule
 * references ("Rule 6.3.3", "9.1.2", "Rules 7.5.3-7.5.5", etc.) across
 * the Rules of Play.
 *
 * Server side (rule_anchors.py, a Sphinx extension) has already:
 *   - given every numbered rule's paragraph a stable id, e.g.
 *     <p id="rule-6-3-3"><strong>6.3.3</strong> ...</p>
 *   - emitted _static/rule_index.json, a flat map of every rule number
 *     to the HTML page it lives on.
 *
 * This script:
 *   1. Fetches that manifest once per page load.
 *   2. Walks the rendered content, finds every rule-number-shaped text
 *      token that is a real, known rule (gated on manifest membership --
 *      this is what keeps it from linking version numbers, dates, or
 *      probability figures that happen to look like "58.2"), and turns
 *      it into a real link.
 *   3. Hovering a link shows a small bordered popup with that one
 *      rule's text (same-page: read directly from the DOM; other page:
 *      fetched once and cached).
 *   4. Clicking a link opens a two-pane split view (two same-origin
 *      iframes) instead of navigating away -- the left pane keeps your
 *      place, the right pane jumps to the target, both fully independent
 *      readers. Once both panes exist, clicking a rule reference in
 *      either one sends only the OTHER pane to that target -- the pane
 *      you clicked in stays exactly where it was, so it keeps working as
 *      your place in the book while the other pane becomes your lookup
 *      surface. (An earlier version sent both panes to the same target,
 *      which collapsed the point of having two of them.)
 *   5. If the rule a pane just jumped to has a hidden ".. container::
 *      rule-guide" block right after it (authored in the RST -- see
 *      showGuideIfAvailable below), that block is shown in place of the
 *      raw rule paragraph for that one target, in that one pane only.
 *      Everything else on the page renders normally.
 *   6. On narrow/touch viewports, all of the above is skipped in favour
 *      of plain single-tab anchor navigation -- nothing new to break on
 *      mobile. A plain anchor jump always shows the raw rule text; the
 *      guide swap is a split-pane-only enhancement.
 *
 * Hover previews are only wired on the top-level document, not inside
 * the split-pane iframes -- a deliberate scope cut, noted so it isn't
 * mistaken for a bug. Click-to-split, cross-pane sync, and linkification
 * all work fully inside the iframes.
 */
(function () {
  'use strict';

  var RULE_TOKEN_RE = /\b\d+[a-z]?(?:\.\d+[a-z]?){1,4}\b/g;
  var MOBILE_QUERY = '(max-width: 900px)';
  var manifestPromise = null;
  var pageCache = new Map(); // page URL (no hash) -> Document, or null if fetch failed

  function isMobile() {
    return window.matchMedia(MOBILE_QUERY).matches;
  }

  function isInOwnSplitPane() {
    // This same script runs again, independently, every time a page loads
    // inside one of our own split-view iframes (it's the same site, so the
    // iframe's <script src="rule_links.js"> tag fires its own boot() just
    // like a normal top-level page load). Left unguarded, that second copy
    // would attach its own click-to-split handler on top of wireFrame's
    // (below), which already fully owns navigation and linkification for
    // pane content -- the two would race, and on a wide-enough pane (a
    // pane's own width, not the outer window's, decides isMobile() here)
    // the pane's own copy can boot a nested split view of its own, seen
    // briefly before wireFrame's navigation tears it back down. Detecting
    // "I am one of our own panes" and skipping self-boot entirely removes
    // the race instead of relying on timing.
    try {
      return !!(window.frameElement && window.frameElement.classList.contains('rule-split-pane'));
    } catch (e) {
      return false; // cross-origin frameElement access (shouldn't happen, same-origin site)
    }
  }

  function loadManifest() {
    if (!manifestPromise) {
      // _static/ is always a sibling of the current page's directory
      // depth in a Sphinx build with html_static_path=['_static'] and
      // no further nesting of source docs, so a relative path from the
      // page works both at the top level and inside a same-origin
      // split-pane iframe (which loads the same site, same relative
      // layout).
      manifestPromise = fetch('_static/rule_index.json')
        .then(function (r) { return r.ok ? r.json() : {}; })
        .catch(function () { return {}; });
    }
    return manifestPromise;
  }

  function anchorId(ruleNumber) {
    return 'rule-' + ruleNumber.replace(/\./g, '-');
  }

  // ---- Linkification -------------------------------------------------

  function linkifyRoot(root, manifest) {
    if (!root) return;
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        var el = node.parentElement;
        while (el && el !== root) {
          var tag = el.tagName;
          if (tag === 'A' || tag === 'STRONG' || tag === 'SCRIPT' ||
              tag === 'STYLE' || tag === 'PRE' || tag === 'CODE') {
            return NodeFilter.FILTER_REJECT;
          }
          el = el.parentElement;
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    });

    var textNodes = [];
    var n;
    while ((n = walker.nextNode())) textNodes.push(n);

    textNodes.forEach(function (node) {
      var text = node.nodeValue;
      RULE_TOKEN_RE.lastIndex = 0;
      var match;
      var pieces = [];
      var lastIndex = 0;
      var found = false;

      while ((match = RULE_TOKEN_RE.exec(text))) {
        var ruleNumber = match[0];
        var page = manifest[ruleNumber];
        if (!page) continue; // not a real rule number -- leave as plain text
        found = true;
        if (match.index > lastIndex) {
          pieces.push(document.createTextNode(text.slice(lastIndex, match.index)));
        }
        var a = document.createElement('a');
        a.className = 'rule-ref';
        a.href = page + '#' + anchorId(ruleNumber);
        a.dataset.rule = ruleNumber;
        a.textContent = ruleNumber;
        pieces.push(a);
        lastIndex = match.index + ruleNumber.length;
      }

      if (!found) return;
      if (lastIndex < text.length) {
        pieces.push(document.createTextNode(text.slice(lastIndex)));
      }
      var parent = node.parentNode;
      pieces.forEach(function (piece) { parent.insertBefore(piece, node); });
      parent.removeChild(node);
    });
  }

  // ---- Hover popup (top-level document only) --------------------------

  function initHoverPopup(manifest) {
    var popup = document.createElement('div');
    popup.className = 'rule-popup';
    popup.hidden = true;
    document.body.appendChild(popup);

    var showTimer = null;
    var currentTarget = null;

    function hide() {
      if (showTimer) { clearTimeout(showTimer); showTimer = null; }
      popup.hidden = true;
      currentTarget = null;
    }

    function renderInto(html) {
      popup.innerHTML = html || '<em>(rule text unavailable)</em>';
    }

    function fetchAndCacheContent(pageUrl, ruleNumber) {
      var cached = pageCache.get(pageUrl);
      if (cached !== undefined) {
        return Promise.resolve(cached);
      }
      return fetch(pageUrl)
        .then(function (r) { return r.ok ? r.text() : null; })
        .then(function (html) {
          var doc = html ? new DOMParser().parseFromString(html, 'text/html') : null;
          pageCache.set(pageUrl, doc);
          return doc;
        })
        .catch(function () {
          pageCache.set(pageUrl, null);
          return null;
        });
    }

    function showFor(link, ruleNumber, page) {
      currentTarget = link;
      var rect = link.getBoundingClientRect();
      popup.style.left = Math.min(rect.left, window.innerWidth - 340) + 'px';
      popup.style.top = (rect.bottom + window.scrollY + 6) + 'px';

      var samePage = page === location.pathname.split('/').pop();
      if (samePage) {
        var el = document.getElementById(anchorId(ruleNumber));
        renderInto(el ? el.innerHTML : null);
        popup.hidden = false;
        return;
      }

      renderInto('<em>Loading&hellip;</em>');
      popup.hidden = false;
      fetchAndCacheContent(page, ruleNumber).then(function (doc) {
        if (currentTarget !== link) return; // moved on already
        var el = doc && doc.getElementById(anchorId(ruleNumber));
        renderInto(el ? el.innerHTML : null);
      });
    }

    document.body.addEventListener('mouseover', function (e) {
      var link = e.target.closest('a.rule-ref');
      if (!link || document.getElementById('rule-split-view')) return;
      if (showTimer) clearTimeout(showTimer);
      showTimer = setTimeout(function () {
        var ruleNumber = link.dataset.rule;
        var page = link.getAttribute('href').split('#')[0];
        showFor(link, ruleNumber, page);
      }, 150);
    });

    document.body.addEventListener('mouseout', function (e) {
      var link = e.target.closest('a.rule-ref');
      if (!link) return;
      if (e.relatedTarget && (e.relatedTarget === popup || popup.contains(e.relatedTarget))) return;
      hide();
    });
  }

  // ---- Click-to-split pane ---------------------------------------------

  function buildSplitView() {
    var overlay = document.createElement('div');
    overlay.id = 'rule-split-view';

    var closeBtn = document.createElement('button');
    closeBtn.id = 'rule-split-close';
    closeBtn.type = 'button';
    closeBtn.textContent = '✕ Close split view';
    closeBtn.addEventListener('click', function () {
      leftFrame.src = 'about:blank';
      rightFrame.src = 'about:blank';
      overlay.hidden = true;
    });

    var leftFrame = document.createElement('iframe');
    leftFrame.className = 'rule-split-pane';
    var rightFrame = document.createElement('iframe');
    rightFrame.className = 'rule-split-pane';

    overlay.appendChild(closeBtn);
    overlay.appendChild(leftFrame);
    overlay.appendChild(rightFrame);
    document.body.appendChild(overlay);

    return { overlay: overlay, left: leftFrame, right: rightFrame };
  }

  function highlightTarget(doc, hash) {
    if (!hash) return null;
    var el = doc.getElementById(hash.slice(1));
    if (!el) return null;
    el.scrollIntoView({ block: 'center' });
    el.classList.add('rule-ref-target');
    setTimeout(function () { el.classList.remove('rule-ref-target'); }, 2500);
    return el;
  }

  // Right pane: guide-or-raw. A rule authored with a ".. container::
  // rule-guide" block immediately after it (hidden by CSS during normal
  // reading -- see custom.css) gets that block shown here IN PLACE OF
  // the raw rule paragraph, but only inside a split pane, and only for
  // the specific rule that pane just jumped to. Everything else on the
  // page -- neighbouring rules, tables, cross-references -- renders
  // normally; only the one targeted paragraph is swapped.
  function resetGuideSwaps(doc) {
    var guides = doc.querySelectorAll('.rule-guide');
    for (var i = 0; i < guides.length; i++) {
      guides[i].style.display = '';
      var raw = guides[i].previousElementSibling;
      if (raw) raw.style.display = '';
    }
  }

  function showGuideIfAvailable(targetEl) {
    if (!targetEl) return;
    var guide = targetEl.nextElementSibling;
    if (!guide || !guide.classList.contains('rule-guide')) return;
    targetEl.style.display = 'none';
    guide.style.display = 'block';
  }

  function wireFrame(frame, otherFrame, manifest) {
    frame.addEventListener('load', function () {
      var doc = frame.contentDocument;
      if (!doc || !doc.body) return; // about:blank or cross-origin (shouldn't happen, same-origin site)
      linkifyRoot(doc.body, manifest);

      // Jumping to a second target on a page already loaded in this pane
      // (very common -- most rule cross-references stay within the same
      // section) changes only the iframe's URL fragment, which does NOT
      // fire a fresh 'load' event in the browser. Re-run the
      // highlight/guide-swap step on 'hashchange' too, so the second (and
      // every subsequent) same-page jump is handled, not just the first.
      function jumpToCurrentHash() {
        resetGuideSwaps(doc);
        var targetEl = highlightTarget(doc, frame.contentWindow.location.hash);
        showGuideIfAvailable(targetEl);
      }
      jumpToCurrentHash();
      frame.contentWindow.addEventListener('hashchange', jumpToCurrentHash);

      doc.body.addEventListener('click', function (e) {
        var link = e.target.closest('a.rule-ref');
        if (!link) return;
        e.preventDefault();
        // Send only the OTHER pane to the target -- the pane you're
        // reading stays put, so it keeps working as a lookup surface
        // instead of both panes converging on the same page.
        otherFrame.src = link.getAttribute('href');
      });
    });
  }

  var splitViewRefs = null;

  function openSplitView(targetHref, manifest) {
    if (!splitViewRefs) {
      splitViewRefs = buildSplitView();
      wireFrame(splitViewRefs.left, splitViewRefs.right, manifest);
      wireFrame(splitViewRefs.right, splitViewRefs.left, manifest);
    }
    splitViewRefs.overlay.hidden = false;
    var currentPage = location.pathname.split('/').pop() || 'index.html';
    var currentHash = location.hash || '';
    splitViewRefs.left.src = currentPage + currentHash;
    splitViewRefs.right.src = targetHref;
  }

  function initClickHandler(manifest) {
    document.body.addEventListener('click', function (e) {
      var link = e.target.closest('a.rule-ref');
      if (!link) return;
      if (isMobile()) return; // let it navigate normally
      e.preventDefault();
      openSplitView(link.getAttribute('href'), manifest);
    });
  }

  // ---- Boot -------------------------------------------------------------

  document.addEventListener('DOMContentLoaded', function () {
    if (isInOwnSplitPane()) return; // wireFrame() (this file, above) already owns this page's behavior
    var content = document.querySelector('.rst-content') || document.body;
    loadManifest().then(function (manifest) {
      if (!manifest || Object.keys(manifest).length === 0) return;
      linkifyRoot(content, manifest);
      if (!isMobile()) {
        initHoverPopup(manifest);
      }
      initClickHandler(manifest);
    });
  });
})();
