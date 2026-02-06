import streamlit as st

st.set_page_config(page_title="Academic Background", layout="wide")
st.sidebar.write("Academic Background")
st.title("Academic Background")

with st.expander("University of the Free State", expanded=True):
    st.write("### BCom Honours in Business and Financial Analytics")
    st.write("**2025 - Present**")
    st.write("""
    This postgraduate program focuses on advanced analytical techniques and their application in 
    business environments. Key areas of study include:
    """)
    
    # Using a list for readability
    skills = [
        "Advanced Business Analytics",
        "Financial Econometrics",
        "Data Science & Machine Learning",
        "Mathematical Modeling for Business"
    ]
    for skill in skills:
        st.write(f"- {skill}")

st.success("I am dedicated to continuous learning and staying updated with the latest trends in the financial tech space.")
