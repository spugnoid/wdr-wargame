"""Gun-vs-vehicle matchup view."""

from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

from viz import data

AV_COLUMN_LABELS = {
    "av_vs_capped_mm": "vs. Capped",
    "av_vs_tungsten_mm": "vs. Tungsten",
    "av_vs_heat_mm": "vs. HEAT",
}


def render() -> None:
    st.header("Gun vs. Vehicle Matchup")
    st.caption(
        "A gun's penetration curve against a target vehicle's armor value -- "
        "the crossing point (if any) is the max effective range."
    )

    gun = st.selectbox("Attacking gun", options=data.gun_ids())
    vehicle = st.selectbox("Target vehicle", options=data.vehicle_names())
    av_label = st.radio(
        "Target armor value", options=list(AV_COLUMN_LABELS.values()), horizontal=True
    )
    av_column = next(k for k, v in AV_COLUMN_LABELS.items() if v == av_label)

    if not gun or not vehicle:
        st.info("Select a gun and a target vehicle.")
        return

    curve = data.gun_curve_long([gun])
    armor = data.vehicle_armor_for([vehicle], av_column=av_column)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=curve["range_m"],
            y=curve["pen_mm"],
            mode="lines+markers",
            name=f"{gun} PEN",
        )
    )
    for _, row in armor.iterrows():
        fig.add_trace(
            go.Scatter(
                x=curve["range_m"],
                y=[row["av_mm"]] * len(curve),
                mode="lines",
                name=f"{vehicle} {row['profile']} AV",
                line={"dash": "dash"},
            )
        )
    fig.update_layout(xaxis_title="Range (m)", yaxis_title="mm")
    st.plotly_chart(fig, width="stretch")
