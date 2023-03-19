import requests
import streamlit as st
import pandas as pd

from src.settings import get_settings
from src.data_models import TimeSeries
from src.logic import calculate_ts_metrics

settings = get_settings()

st.title("Time series prediction app")

with st.form("main_form"):
    session = requests.Session()

    feature_name = st.text_input("Feature name", "post_views_per_day")

    smoothing_level = st.slider(
        "Select smoothing level", min_value=0.0, max_value=1.0, step=0.05, value=0.5
    )
    csv_file = st.file_uploader("Upload csv file", type=["csv"])
    send_req = st.form_submit_button("Predict !")
    

    if csv_file:
        st.subheader("Time series info")

        df = pd.read_csv(csv_file)
        if feature_name not in df.columns:
            st.error("Select valid feature name !")

        values = df[feature_name].values        

        payload = TimeSeries(feature=feature_name, data=list(values), smoothing_level=smoothing_level).json()

        st.line_chart(data=df, y=feature_name)

        metrics = calculate_ts_metrics(values)

        m1, m2 = st.columns(2)
        m1.metric(label="Mean", value=metrics["mean"])
        m2.metric(label="Std", value=metrics["std"])


    if send_req:
        try:
            st.header("Prediction result")
            response = session.post(settings.ml_service_url, payload).json()
            c1, c2 = st.columns(2)
            c1.text("Predicted value: ")
            c2.text(round(response["predicted_value"], 3))
        except requests.exceptions.ConnectionError as e:
            st.warning("Can't connect to service !")
