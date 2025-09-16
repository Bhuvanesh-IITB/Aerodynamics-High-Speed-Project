import streamlit as st
import numpy as np
import pandas as pd
st.title("Oblique Shock Calculator",anchor=False)
st.write('### Input Data')
col1, col2,col3 = st.columns(3)
M = col1.number_input('Mach Number',min_value=0.00,value=2.00)
g = col2.number_input('gamma',value=1.4)
n = col3.number_input('Turn Angle',value=20.00)
options = ["Weak Shock Solution", "Strong Shock Solution"]
choice = st.selectbox("Choose Solution Type:", options)
if choice == "Weak Shock Solution": k='w'
if choice == "Strong Shock Solution": k='s'
def newton(M,g,n,k='w'):
    tol=1e-10
    n = n*np.pi/180
    if k=='w':
         m = 30*np.pi/180
    if k == 's':
         m = 70*np.pi/180
    while True:
            f = np.tan(n) - ((2*(1/np.tan(m))*(M**2 * (np.sin(m))**2 - 1)) / (2 + M**2 * (g + np.cos(2*m))))
            #fp = -1 * (2*np.cos(2*m)*(M**2 - np.sin(m)**(-2)) + 4*np.tan(m)**(-2) +2*M**2*np.sin(2*m)) / (2 + M**2*(g + np.cos(2*m)))**2
            #fp = ((M**2 - (1/(np.sin(m))**2))-(M**2*np.sin(2*m)*(2+2*(1/np.tan(m)))))/(2+(M**2*(g+np.cos(2*m))))**2
            fp = -1*((2*M**2*np.cos(2*m)+(1/(np.sin(m))**2))*(2 + M**2 * (g + np.cos(2*m))) + (2*M**2*np.sin(2*m))*(2*(1/np.tan(m))*(M**2 * (np.sin(m))**2 - 1)))/(2 + M**2 * (g + np.cos(2*m)))**2
            mn = m - f/fp
            if abs(mn - m) < tol:
                return mn*180/np.pi
            m=mn
def oblique(M,g,m):
    u = (g+1)/(g-1)
    k = ((g-1)*M**2)+2
    l = (2*g*M**2)-(g-1)
    M2 = np.sqrt(k/l)
    p = l/(g+1)
    d = (g+1)*M**2/k
    t = (u+p)/(u+(1/p))
    p0 = ((1+((g-1)/2)*M2**2)**(g/(g-1))/(1+((g-1)/2)*M**2)**(g/(g-1)))*p
    p2p = 1/(((1+((g-1)/2)*M2**2)**(g/(g-1)))*p)
    return m,M,M2,M2/np.sin(np.deg2rad(m-n)),p,t,d,p0,p2p
m=newton(M,g,n,k)
t=M*np.sin(np.deg2rad(m))
if t > 1:
    r=oblique(t,g,m)
else:
     st.write('Error,Normal Mach number should be greater than 1')
st.write("## Values")
labels = ["Shock Angle",
    "Mach Number Normal to shock Mn1",
    "Exit Normal Mach Number Mn2",
    "Exit total Mach Number M2",
    "Pressure Ratio (strength of the shock) P2/P1",
    "Temperature Ratio T2/T1",
    "Density Ratio D2/D1",
    "Stagnation pressure ratio P02/P01",
    "P02/p1"
]   
t = pd.DataFrame({"Parameters":labels, "Values":r})
st.write(t)
st.markdown("---")  # horizontal line
st.markdown("Made by **Bhuvanesh K**, IIT Bombay")