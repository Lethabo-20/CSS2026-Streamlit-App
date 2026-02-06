import streamlit as st

# 1. Setup the Sidebar Navigation
st.sidebar.title("Portfolio Navigation")
page = st.sidebar.radio("Select a Section:", 
    ["Home", "Academic Background", "Projects", "Contact Details"])

# 2. THE HOME PAGE
if page == "Home":
    st.title("Lethabo Chantel Phalime")
    st.subheader("BCom Honours: Business and Financial Analytics")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("download (2).jpg") # Placeholder for your photo
    with col2:
        st.write("### Introduction")
        st.write("""
        Welcome to my e-Portfolio. I am a student at the University of the Free State 
        specializing in data-driven financial insights.
        """)

# 3. THE ACADEMIC PAGE
elif page == "Academic Background":
    st.title("🎓 Academic Background")
    st.write("### University of the Free State")
    st.write("- Bachelor of Commerce Honours in Business and Financial Analytics")
    st.info("Key Focus: Advanced Business Analytics, Econometrics, and Data Science.")

# 4. THE PROJECTS PAGE
elif page == "Projects":
    st.title("📂 Research & Projects")
    project_list = ["Lead-Lag Analysis", "Anomaly Detection", "SASL Place Name Project"]
    selected_project = st.selectbox("View Project Details:", project_list)
    
    st.write(f"### {selected_project}")
    if selected_project == "Balancing Imabalanced datasets using AI Project":
        st.write("Pending research project details.")
    else:
        st.write("Details for this academic project will be updated soon.")

# 5. THE CONTACT PAGE
elif page == "Contact Details":
    st.title("✉️ Contact Information")
    st.write("LinkedIn: [Lethabo Chantel Phalime](http://www.linkedin.com/in/lethabochantelphalime-a64661245)")
    st.write("GitHub: [Lethabo-20](https://github.com/Lethabo-20)")
