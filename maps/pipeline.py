"""YAML-driven orchestration for maps: reads scene description files,
renders each to SVG, writes output.

Source data (one YAML file per example scene):
  data/*.yaml

Run: python3 -m maps.pipeline (from the repo root -- maps/ needs no
PYTHONPATH entry, unlike counters/armor_calc or counters/infantry_calc
which need PYTHONPATH=counters. maps/ already sits directly under the
repo root, and Python's -m flag adds the current working directory to
sys.path, so the package is found without help. Verified empirically
before writing this plan.)
Output: maps/svg_output/*.svg (one per data/*.yaml file, same stem)
"""

from __future__ import annotations

import pathlib

import yaml

from maps.renderer import render_to_string
from maps.scene import load_scene

DATA_DIR = pathlib.Path(__file__).parent / "data"
OUTPUT_DIR = pathlib.Path(__file__).parent / "svg_output"


def render_all() -> list[pathlib.Path]:
    """Render every scene in DATA_DIR to an SVG file in OUTPUT_DIR.

    Returns:
        Paths of the SVG files written, in the order processed.
    """
    OUTPUT_DIR.mkdir(exist_ok=True)
    written = []
    for yaml_path in sorted(DATA_DIR.glob("*.yaml")):
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
        scene = load_scene(data)
        svg_text = render_to_string(scene)
        output_path = OUTPUT_DIR / f"{yaml_path.stem}.svg"
        output_path.write_text(svg_text)
        written.append(output_path)
    return written


def main() -> None:
    for path in render_all():
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
