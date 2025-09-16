import streamlit as st
import numpy as np
import pandas as pd
st.title('Isentropic Flow Calculator',anchor=False)
st.write('## Input Data')
col1, col2 = st.columns(2)
M = col1.number_input('Mach Number',min_value=0.00,value=1.00)
g = col2.number_input('gamma',value=1.4)
def isentropic(M,g):
    k = (g+1)/(g-1)
    t = (1+((g-1)/2)*M**2)
    p = t**(g/(g-1))
    d = t**(1/(g-1))
    ma = np.arcsin(1/M)
    pma = (np.sqrt(k)*np.arctan(np.sqrt(((M**2)-1)/k)))-(np.arctan(np.sqrt((M**2)-1)))
    a = t**(k/2)/(M*((g+1)/2)**(k/2))
    t8 = ((g+1)/2)
    p8 = t8**(g/(g-1))
    d8 = t8**(1/(g-1))
    return g,M,ma * (180/np.pi),t,p,d,pma * (180/np.pi),a,t8 / t,p8 / p,d8 / d
r = list(isentropic(M,g))
labels = [
    "Gamma",
    "Mach Number",
    "Mach Angle",
    "Temperature ratio T0/T",
    "Pressure ratio P0/P",
    "Density ratio D0/D",
    "Prandtl Meyer Angle",
    "Area Ratio A/A*",
    "Critical Temperature Ratio T/T*",
    "Critical Pressure Ratio P/P*",
    "Critical Density Ratio d/d*"
]
t = pd.DataFrame({"Parameters":labels, "Values":r})
st.write("## Values")
st.dataframe(t)
st.markdown("---")  # horizontal line
st.markdown("Made by **Bhuvanesh K**, IIT Bombay")