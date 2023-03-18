import requests
import streamlit as st

from src.settings import get_settings
from src.data_models import TimeSeries
from src.logic import calculate_ts_metrics


settings = get_settings()

st.title("Time series prediction app")

with st.form("main_form"):
    session = requests.Session()

    feature_name = st.text_input("Feature name", "post_views_per_day")
    raw_data = st.text_input(
        "Coma separated time series values",
        "1, 2, 3, 2, 1, 3, 4, 2, 1, 2, 9, 11, 8, 5"
    )
    smoothing_level = st.slider(
        "Select smoothing level", min_value=0.0, max_value=1.0, step=0.05, value=0.5
    )
    if raw_data:
        values = list(map(int, raw_data.split(", ")))
        if "values" not in st.session_state:
            st.session_state["values"] = values

        payload = TimeSeries(feature=feature_name, data=values, smoothing_level=smoothing_level).json()
    
        metrics = calculate_ts_metrics(values)

        m1, m2 = st.columns(2)
        m1.metric(label="Mean", value=metrics["mean"])
        m2.metric(label="Std", value=metrics["std"])


    send_req = st.form_submit_button("Predict !")

    if send_req:
        st.header("Result")
        response = session.post(settings.ml_service_url, payload).json()
        c1, c2 = st.columns(2)
        c1.text("Predicted value: ")
        c2.text(round(response["predicted_value"], 3))
