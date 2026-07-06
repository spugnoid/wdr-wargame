"""Vehicle armor comparison view."""

from __future__ import annotations

import plotly.express as px
import streamlit as st

from viz import data

AV_COLUMN_LABELS = {
    "av_vs_capped_mm": "vs. Capped",
    "av_vs_tungsten_mm": "vs. Tungsten",
    "av_vs_heat_mm": "vs. HEAT",
}


def render() -> None:
    st.header("Vehicle Armor Comparison")
    st.caption(
        "Hull-Front and Turret-Front armor value, from armor_calc's "
        "roster_output.csv."
    )

    all_vehicles = data.vehicle_names()
    vehicles = st.multiselect(
        "Vehicles to compare", options=all_vehicles, default=all_vehicles[:2]
    )
    av_label = st.radio(
        "Armor value", options=list(AV_COLUMN_LABELS.values()), horizontal=True
    )
    av_column = next(k for k, v in AV_COLUMN_LABELS.items() if v == av_label)

    if not vehicles:
        st.info("Select at least one vehicle to compare.")
        return

    chart_data = data.vehicle_armor_for(vehicles, av_column=av_column)
    fig = px.bar(
        chart_data,
        x="vehicle",
        y="av_mm",
        color="profile",
        barmode="group",
        labels={"av_mm": "AV (mm)", "vehicle": "Vehicle", "profile": "Profile"},
    )
    st.plotly_chart(fig, width="stretch")
