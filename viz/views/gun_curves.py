"""Gun penetration curve comparison view."""

from __future__ import annotations

import plotly.express as px
import streamlit as st

from viz import data


def render() -> None:
    st.header("Gun Penetration Curves")
    st.caption("Penetration vs. range, from armor_calc's gun_curves_output.csv.")

    all_guns = data.gun_ids()
    guns = st.multiselect("Guns to compare", options=all_guns, default=all_guns[:2])

    if not guns:
        st.info("Select at least one gun to compare.")
        return

    chart_data = data.gun_curve_long(guns)
    fig = px.line(
        chart_data,
        x="range_m",
        y="pen_mm",
        color="gun_id",
        markers=True,
        labels={"range_m": "Range (m)", "pen_mm": "Penetration (mm)", "gun_id": "Gun"},
    )
    st.plotly_chart(fig, width="stretch")
