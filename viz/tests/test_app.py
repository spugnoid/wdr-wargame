import pathlib

from streamlit.testing.v1 import AppTest

APP_PATH = str(pathlib.Path(__file__).resolve().parents[1] / "app.py")


def test_app_boots_without_exception():
    at = AppTest.from_file(APP_PATH)
    at.run(timeout=15)
    assert not at.exception


def test_every_view_renders_without_exception():
    at = AppTest.from_file(APP_PATH)
    at.run(timeout=15)
    view_names = at.sidebar.radio[0].options
    assert view_names == [
        "Vehicle Armor Comparison",
        "Gun Penetration Curves",
        "Gun vs. Vehicle Matchup",
        "Infantry Unit Comparison",
    ]
    for view_name in view_names:
        at.sidebar.radio[0].set_value(view_name).run(timeout=15)
        assert not at.exception, f"{view_name} raised: {at.exception}"
