# With Deepest Regret...

[![Documentation Status](https://readthedocs.org/projects/with-deepest-regret/badge/?version=latest)](https://with-deepest-regret.readthedocs.io/en/latest/?badge=latest)

A free, open, hex-and-counter WWII tactical wargame system. Squad-level infantry and armoured combat, 40-yard hex scale.

## Authorship & AI Disclosure

*With Deepest Regret...* is designed by Rod Peters. All game mechanics, numerical
values, and calibration decisions are original human design work, developed and
verified by the designer.

AI assistance (Claude, Anthropic) was used in the development process for:
- Transcribing described design intent into formal rule text
- Computational verification of probability distributions and threshold calibration
- Drafting and formatting of documentation

Every significant design decision, including the reasoning behind it, is recorded
in Appendix E (Design Notes) of the rules document. This record was maintained
throughout development regardless of which tools were used to produce a given draft.

## Repository layout

```
docs/       Rules of Play, built with Sphinx, hosted on Read the Docs
counters/   Design-time calculation engine (Python) — computes the
            armor/gunnery and infantry counter values printed on counters
            from sourced formulas. Nothing here runs at the table.
              armor_calc/     vehicle armor, penetration, and gunnery
              infantry_calc/  infantry/support-weapon counter values
              quality/        shared crew/unit quality-tier vocabulary
maps/       SVG hex-map diagram generator (Python) — renders worked-example
            diagrams (terrain, unit tokens, movement) for the Rules of Play,
            the same docs-as-code way counters/ computes stat values.
```

Each `counters/` package has its own README with details on its data files
and how to run it.

## Reading the docs

The Rules of Play build automatically on every push to `main` and are hosted at [with-deepest-regret.readthedocs.io](https://with-deepest-regret.readthedocs.io/en/latest/).

### Building the docs locally

```
cd docs
pip install -r requirements.txt
sphinx-build -b html source _build/html
```

Open `docs/_build/html/index.html` in a browser.

## Running the calculation engine and tests

```
pip install -r counters/requirements.txt
python3 -m pytest counters/
PYTHONPATH=counters python3 -m armor_calc.pipeline
PYTHONPATH=counters python3 -m infantry_calc.pipeline
```

Both pipelines write plain CSV reference tables (vehicle armor/gunnery
values, infantry counter values) into their own package directory —
open directly in Excel/Sheets to review, or hand-edit the CSV inputs
under each package's `data/` directory to add or correct an entry.

## License

This project uses two licenses, split by content type:

| Content | License | File |
| --- | --- | --- |
| Rules text (`docs/`), counter art, maps | CC BY 4.0 | [LICENSE-CONTENT.md](LICENSE-CONTENT.md) |
| Code — the `counters/` calculation engine, build scripts | MIT | [LICENSE-CODE.md](LICENSE-CODE.md) |

Both permit commercial use and modification. CC BY 4.0 requires attribution to the With Deepest Regret Project; MIT requires only that the license notice be preserved. Neither restricts building closed-source tools or commercial products on top of this work.

Note: the game's mechanics (formulas, procedures, result tables as *ideas*) are not subject to copyright and are not "licensed" by either file above — only the specific text, art, and code expressing them are. This is standard for tabletop game design; see the design notes in `docs/source/appendix_e__design_notes.rst` for the project's design rationale if you're building something derivative.

## Status

Rules of Play: v0.9.2, working draft. See `docs/source/appendix_e__design_notes.rst` for the full design-decision log.
