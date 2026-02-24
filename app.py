import streamlit as st

st.title("Cooling Tower Performance Calculator")

Thot = st.number_input("Hot water temperature (°C)", value=40.0)
Tcold = st.number_input("Cold water temperature (°C)", value=32.0)
Twb = st.number_input("Wet bulb temperature (°C)", value=28.0)
flow = st.number_input("Circulating water flow (m3/hr)", value=5000.0)
coc = st.number_input("Cycles of concentration", value=4.0)
drift_percent = st.number_input("Drift loss (%)", value=0.02)
evap_factor = st.number_input("Evaporation factor", value=0.00085)

range_val = Thot - Tcold
approach = Tcold - Twb
effectiveness = range_val / (range_val + approach) if (range_val + approach) != 0 else 0
efficiency = effectiveness * 100

evap = evap_factor * flow * range_val
drift = flow * drift_percent / 100
blowdown = evap / (coc - 1) if coc > 1 else 0
makeup = evap + drift + blowdown

st.header("Results")
st.write(f"Range: {range_val:.2f} °C")
st.write(f"Approach: {approach:.2f} °C")
st.write(f"Effectiveness: {effectiveness:.2f}")
st.write(f"Efficiency: {efficiency:.2f} %")

st.subheader("Water Losses")
st.write(f"Evaporation loss: {evap:.2f} m3/hr")
st.write(f"Drift loss: {drift:.2f} m3/hr")
st.write(f"Blowdown: {blowdown:.2f} m3/hr")
st.write(f"Make-up water: {makeup:.2f} m3/hr")
