import streamlit as st
import pandas as pd
from datetime import datetime
import os
from filelock import FileLock

# File path for the database CSV
DATABASE_FILE = "database.csv"
LOCK_FILE = DATABASE_FILE + ".lock"

# Function to initialize the database if it doesn't exist
def initialize_database():
    if not os.path.exists(DATABASE_FILE):
        columns = ["Reference ID", "Request Submission Date", "Requester Name", "Request Purpose", "Amount Requested"]
        pd.DataFrame(columns=columns).to_csv(DATABASE_FILE, index=False)

# Function to generate the next Reference ID
def get_next_reference_id(data):
    if data.empty:
        return "REQ-001"
    else:
        max_id = int(data["Reference ID"].str.split("-").str[1].max())
        return f"REQ-{max_id + 1:03}"

# Function to display the welcome page
def welcome_page():
    st.title("Welcome to the E-Operation App")
    st.markdown("""
        - **Submit Requests:** Use the form to submit a new request.
        - **View Database:** View all submitted requests.
    """)

# Function to display the request form
def request_form_page():
    st.title("Request Form")
    st.subheader("Submit a New Request")
    
    # Form fields
    requester_name = st.text_input("Requester Name")
    request_purpose = st.text_area("Request Purpose")
    amount_requested = st.number_input("Amount Requested", min_value=0.0, format="%.2f")

    if st.button("Submit Request"):
        if requester_name.strip() == "" or request_purpose.strip() == "" or amount_requested <= 0:
            st.error("All fields are required. Please fill out the form completely.")
        else:
            # Read existing data
            data = pd.read_csv(DATABASE_FILE)
            
            # Generate new request details
            reference_id = get_next_reference_id(data)
            submission_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Create new request as a DataFrame
            new_request = pd.DataFrame([{
                "Reference ID": reference_id,
                "Request Submission Date": submission_date,
                "Requester Name": requester_name,
                "Request Purpose": request_purpose,
                "Amount Requested": amount_requested,
            }])
            
            # Concatenate the new request to the existing data
            data = pd.concat([data, new_request], ignore_index=True)
            
            # Use file lock for safe write
            with FileLock(LOCK_FILE):
                data.to_csv(DATABASE_FILE, index=False)
            
            st.success(f"Request submitted successfully with Reference ID: {reference_id}")

# Function to display the database
def database_page():
    st.title("Database")
    st.subheader("View All Requests")
    
    # Read and display the database
    if os.path.exists(DATABASE_FILE):
        data = pd.read_csv(DATABASE_FILE)
        st.dataframe(data)
    else:
        st.warning("No requests found. Submit a request to populate the database.")

# Main function to control the app
def main():
    initialize_database()
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Welcome", "Request Form", "Database"])
    
    if page == "Welcome":
        welcome_page()
    elif page == "Request Form":
        request_form_page()
    elif page == "Database":
        database_page()

if __name__ == "__main__":
    main()
