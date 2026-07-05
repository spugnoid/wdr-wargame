# With Deepest Regret...

A free, open, hex-and-counter WWII tactical wargame system. Squad-level infantry and armoured combat, 40-yard hex scale.

## Repository layout

```
docs/       Rules of Play, built with Sphinx, hosted on Read the Docs
counters/   Excel counter designer + CorelDraw VBA macro + templates
maps/       SVG hex map generator
```

## Building the docs locally

```
cd docs
pip install -r requirements.txt
sphinx-build -b html source _build/html
```

Open `docs/_build/html/index.html` in a browser.

## License

This project uses two licenses, split by content type:

| Content | License | File |
| --- | --- | --- |
| Rules text (`docs/`), counter art, maps | CC BY 4.0 | [LICENSE-CONTENT.md](LICENSE-CONTENT.md) |
| Code — VBA macro, build scripts, future web client | MIT | [LICENSE-CODE.md](LICENSE-CODE.md) |

Both permit commercial use and modification. CC BY 4.0 requires attribution to the With Deepest Regret Project; MIT requires only that the license notice be preserved. Neither restricts building closed-source tools or commercial products on top of this work.

Note: the game's mechanics (formulas, procedures, result tables as *ideas*) are not subject to copyright and are not "licensed" by either file above — only the specific text, art, and code expressing them are. This is standard for tabletop game design; see the design notes in `docs/source/appendix_e__design_notes.rst` for the project's design rationale if you're building something derivative.

## Status

Rules of Play: v0.9.2, working draft. See `docs/source/appendix_e__design_notes.rst` for the full design-decision log.
