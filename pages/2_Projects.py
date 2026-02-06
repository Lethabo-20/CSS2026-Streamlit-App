import streamlit as st

st.title("Research & Projects")

# Using tabs to keep the page clean like your Google Site
tab1, tab2, tab3 = st.tabs(["Data Science", "Financial Analytics", "SASL Project"])

with tab1:
    st.subheader("Lead-Lag Analysis & Anomaly Detection")
    st.write("Explored market indicators to identify shifted correlations in financial data.")
    
with tab2:
    st.subheader("Social Media Sentiment Mapping")
    st.write("Topic mapping and sentiment analysis of public financial discourse.")
