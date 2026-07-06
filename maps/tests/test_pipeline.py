from maps.pipeline import DATA_DIR, OUTPUT_DIR, render_all


def test_render_all_writes_svg_for_pilot_scene():
    written = render_all()
    stems = {p.stem for p in written}
    assert "section7_movement_example1" in stems

    output_path = OUTPUT_DIR / "section7_movement_example1.svg"
    assert output_path.exists()
    content = output_path.read_text()
    assert content.startswith('<?xml version="1.0" encoding="UTF-8"?>')
    assert "<svg" in content
    assert "GREN" in content


def test_render_all_processes_every_yaml_file_in_data_dir():
    written = render_all()
    yaml_files = sorted(DATA_DIR.glob("*.yaml"))
    assert len(written) == len(yaml_files)
