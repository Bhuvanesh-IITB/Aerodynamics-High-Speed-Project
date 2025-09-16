import streamlit as st
import numpy as np
import pandas as pd
st.title("Normal Shock Calculator",anchor=False)
st.write('### Input Data')
col1, col2 = st.columns(2)
M = col1.number_input('Mach Number',min_value=0.00,value=1.01)
g = col2.number_input('gamma',value=1.4)
def normal(M,g):
    u = (g+1)/(g-1)
    k = ((g-1)*M**2)+2
    l = (2*g*M**2)-(g-1)
    M2 = np.sqrt(k/l)
    p = l/(g+1)
    d = (g+1)*M**2/k
    t = (u+p)/(u+(1/p))
    p0 = ((1+((g-1)/2)*M2**2)**(g/(g-1))/(1+((g-1)/2)*M**2)**(g/(g-1)))*p
    p2p = 1/(((1+((g-1)/2)*M2**2)**(g/(g-1)))*p)
    return M,M2,p,t,d,p0,p2p
if M > 1:
    r=normal(M,g)
else:
    st.write('Error, Mach Number should be Greater than 1')
labels = [
    "Mach Number M1",
    "Exit Mach Number M2",
    "Pressure Ratio / Strength of Shock P2/P1",
    "Temperature Ratio T2/T1",
    "Density Ratio D2/D1",
    "Stagnation pressure ratio P02/P01",
    "P02/p1"
]
t = pd.DataFrame({"Parameters":labels, "Values":r})
st.write("## Values")
st.write(t)
st.markdown("---")  # horizontal line
st.markdown("Made by **Bhuvanesh K**, IIT Bombay")