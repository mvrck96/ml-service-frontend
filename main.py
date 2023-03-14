import requests
import streamlit as st

from src.settings import get_settings
from src.data_models import TimeSeries

settings = get_settings()

st.title("Time series prediction app")

feature_name = st.text_input("feature name")
time_series = st.text_input(
    "Coma separated time series values, e.g. 10, 9, 12 ..., 17, 22"
)
smoothing_level = st.slider(
    "Select smoothing level", min_value=0.0, max_value=1.0, step=0.05, value=0.5
)

if st.button("Send data to model"):
    ts = list(map(int, time_series.split(", ")))
    payload = TimeSeries(
        feature=feature_name,
        data=ts,
        smoothing_level=smoothing_level
        )
    response = requests.post(url=settings.ml_service_url, data=payload.json())
    st.text(response.json())
