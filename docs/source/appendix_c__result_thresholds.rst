Appendix C — Result Thresholds
==============================

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Margin (Roll + Resolution FP − Defence − Cover)**
     - **Result**
   * - Below 0
     - No effect
   * - 0 to 8
     - Suppressed — place SUPPRESSED marker
   * - 9 to 13
     - Pinned — place PINNED marker
   * - 14 to 18
     - Casualty — flip unit to rear face (or CI if already on rear face)
   * - 19 to 22
     - Casualty + Suppressed — flip unit to rear face and place SUPPRESSED marker
   * - 23+
     - Broken — unit is CI, remove from map to BROKEN zone


Long Range Cap: when effective rFP is 3 or less after all modifiers, maximum result is Pinned regardless of margin.

Multiple attack step-up order: Suppressed → Pinned → Casualty → Casualty+Suppressed → Broken.

Outcome Probability Table
-------------------------


Exact probabilities for the 1d6+1d8+1d12 roll (576 outcomes) at each net modifier, under the v0.9.2 thresholds. The net modifier is Resolution FP minus the target's Defence and cover. Values under 0.05% shown as —. This table is reference material for scenario designers and does not need to be consulted during play.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - **Net modifier (Resolution FP − Defence − Cover)**
     - **No effect**
     - **Suppressed**
     - **Pinned**
     - **Casualty**
     - **Cas+Sup**
     - **Broken**
   * - -14
     - 41.8%
     - 54.7%
     - 3.5%
     - —
     - —
     - —
   * - -13
     - 34.0%
     - 59.9%
     - 6.1%
     - —
     - —
     - —
   * - -12
     - 26.7%
     - 63.5%
     - 9.5%
     - 0.2%
     - —
     - —
   * - -11
     - 20.1%
     - 65.5%
     - 13.7%
     - 0.7%
     - —
     - —
   * - -10
     - 14.4%
     - 65.5%
     - 18.4%
     - 1.7%
     - —
     - —
   * - -9
     - 9.7%
     - 63.5%
     - 23.3%
     - 3.5%
     - —
     - —
   * - -8
     - 6.1%
     - 59.9%
     - 28.0%
     - 6.1%
     - —
     - —
   * - -7
     - 3.5%
     - 54.7%
     - 32.1%
     - 9.5%
     - 0.2%
     - —
   * - -6
     - 1.7%
     - 48.3%
     - 35.6%
     - 13.7%
     - 0.7%
     - —
   * - -5
     - 0.7%
     - 41.1%
     - 38.0%
     - 18.4%
     - 1.7%
     - —
   * - -4
     - 0.2%
     - 33.9%
     - 39.2%
     - 23.3%
     - 3.5%
     - —
   * - -3
     - —
     - 26.7%
     - 39.2%
     - 28.0%
     - 5.9%
     - 0.2%
   * - -2
     - —
     - 20.1%
     - 38.0%
     - 32.1%
     - 9.0%
     - 0.7%
   * - -1
     - —
     - 14.4%
     - 35.6%
     - 35.6%
     - 12.7%
     - 1.7%
   * - +0
     - —
     - 9.7%
     - 32.1%
     - 38.0%
     - 16.7%
     - 3.5%
   * - +1
     - —
     - 6.1%
     - 28.0%
     - 39.2%
     - 20.7%
     - 6.1%
   * - +2
     - —
     - 3.5%
     - 23.3%
     - 39.2%
     - 24.3%
     - 9.7%
   * - +3
     - —
     - 1.7%
     - 18.4%
     - 38.0%
     - 27.4%
     - 14.4%
   * - +4
     - —
     - 0.7%
     - 13.7%
     - 35.6%
     - 29.9%
     - 20.1%
   * - +5
     - —
     - 0.2%
     - 9.5%
     - 32.1%
     - 31.4%
     - 26.7%
   * - +6
     - —
     - —
     - 6.1%
     - 28.0%
     - 31.9%
     - 34.0%


Calibration anchors: a single LMG line (effective rFP 7) against a squad (Defence 8) in the open is net −1; in light woods net −4; in a heavy building net −6; entrenched net −7. Suppression becomes the most likely outcome once the target has meaningful cover; open ground remains lethal by design.
