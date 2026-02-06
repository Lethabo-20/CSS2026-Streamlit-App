import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Researcher Profile", layout="wide")

# 2. Sidebar Navigation (Matching the Screenshot)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Profile", "Publications", "STEM Data Explorer", "Contact"])

# 3. Content for "Profile" Page
if page == "Profile":
    st.header("Researcher Profile")
    
    # Create two columns: one for image, one for text
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Replace the URL with your own photo uploaded to GitHub
        st.image("https://via.placeholder.com/300", caption="Lethabo Chantel Phalime")
    
    with col2:
        st.subheader("Lethabo Chantel Phalime")
        st.write("**Field:** Data Science & Computing")
        st.write("**Institution:** University of the Free State (UFS)")
        st.write("**Role:** Researcher")
        
        st.write("I am a computing academic with interests in:")
        st.markdown("""
        * Data science and analysis
        * South African Sign Language (SASL) Place Names
        * Quantum computing
        * Linux and file management
        """)

# 4. Placeholders for other pages
elif page == "Publications":
    st.title("Publications")
    st.write("List your research papers and symposium presentations here.")

elif page == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.write("This is where your data visualizations will go.")

elif page == "Contact":
    st.title("Contact")
    st.write("How people can reach you.")
