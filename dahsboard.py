import streamlit as st
from joblib import load
import pandas as pd




if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page=="home":
    st.title("PayPredict AI")
    st.subheader("Predict Your Salary with AI")
    st.write("Based on skills, experience, and market trends")
    if st.button("Start Prediction")  :
        st.session_state.page = "predict"
    
elif st.session_state.page=="predict":
   
    st.title("💰 Salary Prediction Form")

# Inputs
    rating = st.slider("Rating", 1, 5)

    location = st.selectbox("Location", ["Bangalore","Mumbai","Hyderabad", "Pune","Chennai", "New Delhi","Kolkata", "Jaipur"])

    employment_status = st.selectbox(
        "Employment Status",
        ["Full-time", "Part-time", "Intern", "Traineer"]
    )
    if employment_status =="Part-time":
        employment_status=3
    elif employment_status=="Traineer":
        employment_status=2
    elif employment_status=="Intern":
        employment_status=1
    else:
        employment_status=4


    seniority = st.selectbox(
        "Seniority",
        ["Junior", "Mid", "Senior"]
    )
    if seniority=="Junior":
        seniority=1
    elif seniority=="Senior":
         seniority=3
    else:
         seniority=2



# Job Role (one-hot style)
    job_role = st.selectbox(
        "Job Role",
        ["Data", "Frontend", "Web", "Other"]
    )
    if location == "Bangalore":
        location= 5
    elif location == "Mumbai":
        location=4
    elif location in ["Hyderabad", "Pune"]:
        location= 3
    elif location in ["Chennai", "New Delhi"]:
        location =2
    elif location in ["Kolkata", "Jaipur"]:
        location =1
    else:
        location= 0

# Convert to one-hot encoding
    job_role_data = 1 if job_role == "Data" else 0
    job_role_frontend = 1 if job_role == "Frontend" else 0
    job_role_web = 1 if job_role == "Web" else 0
    job_role_other = 1 if job_role == "Other" else 0

# Final input dictionary
    input_data = {
    "Rating": rating,
    "Location": location,
    "Employment Status": employment_status,
    "Seniority": seniority,
    "Job Role_data": job_role_data,
    "Job Role_frontend": job_role_frontend,
    "Job Role_other": job_role_other,
    "Job Role_web": job_role_web
    }


    if st.button("Predict Salary"):
        
        x=1
        model = load("salary_model.pkl")
        df = pd.DataFrame([input_data])
        predicted = model.predict(df)
        if predicted == 4:
            st.success("💰 Very High Salary: 9,25,000+ INR")
        elif predicted == 3:
            st.info("💰 High Salary: 5,00,000 - 9,25,000 INR")
        elif predicted == 2:
            st.warning("💰 Medium Salary: 3,00,000 - 5,00,000 INR")
        else:
             st.error("💰 Low Salary: Below 3,00,000 INR")

        