import streamlit as st

st.set_page_config(page_title="Lethabo Phalime e-Portfolio", layout="wide")

# Sidebar for common info
st.sidebar.title("Lethabo C. Phalime")
st.sidebar.write("BCom Honours Student | Business & Financial Analytics")

st.title("Welcome to my e-Portfolio")
st.markdown("---")

col1, col2 = st.columns([1, 2])
with col1:
    st.image("download (2).jpg") # Main Profile Image

with col2:
    st.header("About Me")
    st.write("""
    I am a Bachelor of Commerce Honours student specializing in **Business and Financial Analytics** at the University of the Free State. This portfolio reflects my journey in bridging the gap 
    between complex data and actionable financial insights.
    
    My focus lies in using cutting-edge analytical tools to solve real-world economic problems 
    and identifying patterns that drive strategic decision-making.
    """)
