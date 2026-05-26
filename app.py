import streamlit as st
import random
import time


st.title("🚰 Smart Water Purification Intelligence System")

st.subheader("Enter Water & Operational Parameters")

# Simulated IoT Sensor Data
tds = random.randint(200, 2000)
hardness = random.randint(100, 500)
turbidity = random.randint(1, 10)
temperature = random.randint(20, 40)

# Display Live Sensor Readings
st.subheader("📡 Live IoT Sensor Monitoring")

st.metric("TDS Level", f"{tds} ppm")
st.metric("Water Hardness", f"{hardness} mg/L")
st.metric("Turbidity", turbidity)
st.metric("Temperature", f"{temperature} °C")


litres_processed = st.slider(
    "Litres Processed",
    500,
    10000,
    2000
)

risk_score = (
    (tds * 0.5) +
    (hardness * 0.45) +
    (turbidity * 40) +
    (litres_processed * 0.15)
)

if risk_score < 2500:
    risk = "Low Risk"

elif risk_score < 3200:
    risk = "Medium Risk"

else:
    risk = "High Risk"

membrane_life = (
    48
    - (tds * 0.003)
    - (hardness * 0.004)
    - (turbidity * 0.6)
    - (litres_processed * 0.0015)
)

membrane_life = max(6, membrane_life)

if tds < 300:
    purifier = "UV Purifier"

elif tds < 1200:
    purifier = "UF + UV Purifier"

else:
    purifier = "RO + UV Purifier"

st.subheader("📊 Prediction Results")

st.write("### Operational Risk:", risk)

st.write(
    "### Estimated Membrane Lifespan:",
    round(membrane_life, 1),
    "Months"
)

st.write(
    "### Recommended Purifier:",
    purifier
)