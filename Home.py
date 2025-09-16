import streamlit as st
import numpy as np
import pandas as pd
st.markdown("<h1 style='text-align: center;'>Compressible Flow Calculator</h1>",
    unsafe_allow_html=True)
container = st.container(border=True)
with container:
    st.write("This tool provides quick and accurate solutions for key compressible flow relations.It includes the following")
    st.write("Isentropic Flow Calculator – Computes Mach number, pressure, temperature, and density ratios and critical property ratios for isentropic process")
    st.write("Normal Shock Calculator – Determines post-shock properties such as Mach number, pressure, temperature, and density across a normal shock.")
    st.write("Oblique Shock Calculator – Evaluates flow deflection, shock angle, and property changes for oblique shocks at given conditions")
    st.text("Whether you’re studying aerodynamics, propulsion, or high-speed flows, this calculator helps simplify complex compressible flow analysis")
st.markdown("---")  # horizontal line
st.markdown("Made by **Bhuvanesh K** (23B0064), IIT Bombay")