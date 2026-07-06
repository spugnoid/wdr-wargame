"""Streamlit entry point for the comparison dashboard.

Run: streamlit run viz/app.py (from the repo root)

This module only wires navigation between views -- no data loading or
chart construction of its own. See data.py for the data layer and
views/*.py for each comparison view.
"""

from __future__ import annotations

import streamlit as st

from viz.views import gun_curves, gun_vs_vehicle, infantry_comparison, vehicle_armor

st.set_page_config(page_title="With Deepest Regret -- Data Comparison", layout="wide")

VIEWS = {
    "Vehicle Armor Comparison": vehicle_armor.render,
    "Gun Penetration Curves": gun_curves.render,
    "Gun vs. Vehicle Matchup": gun_vs_vehicle.render,
    "Infantry Unit Comparison": infantry_comparison.render,
}

st.sidebar.title("With Deepest Regret...")
st.sidebar.caption("Data comparison dashboard")
choice = st.sidebar.radio("View", options=list(VIEWS.keys()))

VIEWS[choice]()
