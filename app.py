import streamlit as st
import pandas as pd

# Initialize a placeholder for the database
data = []

# Define the pages
def welcome_page():
    st.title("Welcome to the Request Management System")
    st.write("This application allows you to submit and view requests.")

def request_form():
    st.title("Request Form")
    
    # Form fields
    with st.form("request_form"):
        requester_name = st.text_input("Requester Name")
        purpose = st.text_input("Purpose of Request")
        amount_requested = st.number_input("Amount Requested", min_value=0.0, format="%.2f")
        submission_date = st.date_input("Submission Date")
        
        # Submit button
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            global data
            data.append({
                "Requester Name": requester_name,
                "Purpose": purpose,
                "Amount Requested": amount_requested,
                "Submission Date": str(submission_date)
            })
            st.success("Request submitted successfully!")

def database_page():
    st.title("Request Database")
    global data
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.write("No requests have been submitted yet.")

# Streamlit app structure
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Welcome", "Request Form", "Database"])

if page == "Welcome":
    welcome_page()
elif page == "Request Form":
    request_form()
elif page == "Database":
    database_page()
