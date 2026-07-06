import pathlib
import subprocess
import sys

from streamlit.testing.v1 import AppTest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
APP_PATH = str(REPO_ROOT / "viz" / "app.py")


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


def test_app_runs_standalone_without_module_not_found_error():
    """Regression test for a real production failure: `streamlit run
    viz/app.py` -- the exact command this project documents -- failed
    with "ModuleNotFoundError: No module named 'viz'".

    Root cause: Streamlit's script-loading mechanism (like Python's own
    default behavior for direct script execution) adds the target
    script's own containing directory to sys.path, not the repo root
    and not the current working directory. `app.py`'s
    `from viz.views import ...` needs the repo root (viz/'s parent) on
    sys.path to resolve.

    This class of bug slipped past every test above: AppTest runs
    in-process and inherits pytest's own sys.path, which conftest.py
    already fixes up -- it never exercises the sys.path Streamlit's
    real script runner sets up. `python3 -m streamlit run` (used during
    manual verification before this bug was found) also masks it, since
    the `-m` flag itself injects the current working directory onto
    sys.path before Streamlit's own logic runs.

    Running app.py as a plain standalone script reproduces the exact
    same sys.path[0]-is-the-script's-own-directory behavior Streamlit's
    script runner has, without needing to launch a real server.
    """
    result = subprocess.run(
        [sys.executable, APP_PATH],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert "ModuleNotFoundError" not in result.stderr, result.stderr
    assert result.returncode == 0, result.stderr
