import streamlit as st

st.set_page_config(page_title="Lethabo Phalime e-Portfolio", layout="wide")

# Sidebar for common info
st.sidebar.title("Lethabo C. Phalime")
st.sidebar.write("Introduction")

st.title("Welcome to my e-Portfolio")
st.markdown("---")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # Use a placeholder or your GitHub image path
    st.image("https://via.placeholder.com/350", caption="Lethabo Phalime")

with col2:
    st.header("Professional Profile")
    st.write("""
    Welcome to my e-Portfolio. I am an aspiring data professional currently completing my 
    Honours degree at the **University of the Free State**. 
    
    My academic journey is centered on bridging the gap between raw data and strategic 
    financial decision-making. I am passionate about:
    * **Analytical Problem Solving:** Turning complex datasets into actionable insights.
    * **Technology & Innovation:** Exploring Data Science, Python, and SASL datasets.
    * **Financial Modeling:** Understanding market trends and economic indicators.
    """)
    st.info("💡Turning data into insight and insight into action.")
