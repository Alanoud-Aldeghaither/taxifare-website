import streamlit as st
import requests
from datetime import datetime

st.title("Taxi Fare Prediction")
st.write("Fill in the ride details below to get a fare estimate:")

pickup_date = st.date_input("Pickup Date", value=datetime.today())
pickup_time = st.time_input("Pickup Time", value=datetime.now().time())
pickup_datetime = f"{pickup_date} {pickup_time}"

pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)
passenger_count = st.number_input("Number of Passengers", min_value=1, max_value=8, value=1)

url = 'https://taxifare.lewagon.ai/predict'

if st.button("Predict Fare"):
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json().get("fare", "Error")
        st.success(f"Predicted Fare: ${prediction}")
    else:
        st.error("Failed to contact the API.")
