"""Infantry/support-weapon unit comparison view."""

from __future__ import annotations

import plotly.express as px
import streamlit as st

from viz import data


def render() -> None:
    st.header("Infantry Unit Comparison")
    st.caption(
        "Defence/Morale/M#/F#/G#, from infantry_calc's "
        "infantry_roster_output.csv. Fire lines are shown as text below "
        "since their notation isn't a plain number to chart."
    )

    all_units = data.infantry_unit_ids()
    units = st.multiselect("Units to compare", options=all_units, default=all_units[:2])

    if not units:
        st.info("Select at least one unit to compare.")
        return

    chart_data = data.infantry_stats_for(units)
    fig = px.bar(
        chart_data,
        x="stat",
        y="value",
        color="unit_id",
        barmode="group",
        labels={"stat": "Stat", "value": "Value", "unit_id": "Unit"},
    )
    st.plotly_chart(fig, width="stretch")

    st.subheader("Fire lines")
    st.dataframe(data.infantry_fire_lines_for(units), width="stretch")
