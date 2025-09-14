import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Streamlit UI
st.set_page_config(page_title="Climate Resilience Dashboard", layout="wide")
st.title("🌍 AI-Powered Climate Resilience Predictor (India)")
st.markdown("Enter weather & pollution values to predict **climate risk indicator**.")

# User inputs
rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0.0, max_value=500.0, step=1.0)
pm25 = st.number_input("💨 PM2.5 (µg/m³)", min_value=0.0, max_value=1000.0, step=1.0)
pm10 = st.number_input("🌫️ PM10 (µg/m³)", min_value=0.0, max_value=1000.0, step=1.0)
temperature = st.number_input("🌡️ Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.5)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0, step=1.0)

# Features for model
features = pd.DataFrame({
    'rainfall': [rainfall],
    'pm25': [pm25],
    'pm10': [pm10],
    'temperature': [temperature],
    'humidity': [humidity]
})

# Prediction button
if st.button("🔮 Predict Risk Level"):
    prediction = model.predict(features)[0]
    st.success(f"Predicted Climate Risk Indicator: **{prediction:.2f}**")

    if prediction > 150:
        st.error("⚠️ High Risk! (Flood/Heatwave/Pollution)")
    elif prediction > 75:
        st.warning("⚡ Moderate Risk. Stay cautious.")
    else:
        st.info("✅ Low Risk. Conditions are safe.")



