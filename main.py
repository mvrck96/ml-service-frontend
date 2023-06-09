import requests
import streamlit as st
import pandas as pd

from src.settings import get_settings
from src.data_models import TimeSeries
from src.logic import calculate_ts_metrics

settings = get_settings()

# Set page title and icon
st.set_page_config(
    page_title="Time series prediction app",
    page_icon=":8ball:",
    menu_items={
        "About": "https://mvrck.space/",
        "Report a bug": "https://github.com/mvrck96/ml-service-frontend/issues/new"
    }
)

st.title("📈 Time series prediction UI")

csv_file = st.file_uploader("Upload csv file with time series data", type=["csv"])

# If file uploaded
if csv_file:
    with st.form("main_form"):
        st.header("Prediction parameters")

        df = pd.read_csv(csv_file)
        feature_name = st.selectbox("Pick a feature to predict", options=df.columns)
        smoothing_level = st.slider(
            "Select smoothing level", min_value=0.0, max_value=1.0, step=0.05, value=0.5
        )

        # Assemble payload for POST request
        payload = TimeSeries(
            feature=feature_name,
            data=list(df[feature_name].values),
            smoothing_level=smoothing_level,
        ).json()

        # After button pressed
        if st.form_submit_button("Calculate metrics and make prediction"):
            session = requests.Session()

            st.subheader("Selected time series")
            st.line_chart(data=df, y=feature_name)

            st.subheader("Calculated metrics")
            metrics = calculate_ts_metrics(df[feature_name].values)

            m1, m2 = st.columns(2)
            m1.metric(label="Mean", value=metrics["mean"])
            m2.metric(label="Std", value=metrics["std"])

            st.markdown("---")
            st.subheader("Prediction result")

            try:
                # Send request
                response = session.post(settings.ml_service_url, payload).json()

                pred = round(response["predicted_value"], 3)

                c11, c12 = st.columns(2)
                c11.text("Feature name: ")
                c12.markdown(f"`{response['feature']}`")

                c21, c22 = st.columns(2)
                c21.text("Predicted value: ")
                c22.markdown(f"`{pred}`")

            except requests.exceptions.ConnectionError as e:
                st.warning("Can't connect to backend service !")
