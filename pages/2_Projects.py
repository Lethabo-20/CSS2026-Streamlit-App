import streamlit as st

st.set_page_config(page_title="Projects", layout="wide")
st.sidebar.write("Research & Projects")
st.title("📂 Research & Projects")
st.write("Click below to view the details of my various academic and research projects.")

project = st.selectbox("Select a Project:", [
    "Lead-Lag Analysis",
    "Anomaly Detection",
    "Social Media Sentiment Mapping",
    "SASL Place Name Dataset"
])

st.markdown("---")

if project == "Lead-Lag Analysis":
    st.subheader("Lead-Lag Analysis")
    st.write("Investigation into time-series correlations within financial markets to identify leading indicators.")
    
elif project == "Anomaly Detection":
    st.subheader("Anomaly Detection")
    st.write("Developing models to identify irregular patterns and outliers in large financial datasets.")

elif project == "Social Media Sentiment Mapping":
    st.subheader("Social Media Sentiment & Topic Mapping")
    st.write("Analyzing public discourse on social platforms to map sentiment trends and key topics.")

elif project == "SASL Place Name Dataset":
    st.subheader("SASL Place Name Project")
    st.write("Currently working with Dr. Chrismi-Rinda Loth and Dr. Combrink on a dataset project involving South African Sign Language (SASL) toponymy.")
