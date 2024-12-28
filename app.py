import streamlit as st
import pandas as pd
from google.oauth2.service_account import Credentials
from gspread import authorize
import gspread

# Constants
SHEET_URL = 'https://docs.google.com/spreadsheets/d/1PJ0F1NP9RVR3a3nB6O1sZO_4WlBrexRPRw33C7AjW8E/edit?gid=0#gid=0'
TAB_NAME = 'Database'
JSON_FILE_PATH = 'clever-bee-442514-j7-8a5ce402aab0.json'

# Function to create a Google Sheets connection
def create_gsheets_connection():
    credentials = Credentials.from_service_account_file(JSON_FILE_PATH)
    client = authorize(credentials)
    return client.open_by_url(SHEET_URL).worksheet(TAB_NAME)

# Insert data into Google Sheets
def insert_data(requester_name, purpose, amount_requested):
    sheet = create_gsheets_connection()
    submission_date = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Prepare the data to insert
    data = [requester_name, purpose, amount_requested, submission_date]
    sheet.append_row(data)
    st.success("Request submitted successfully!")

# Retrieve data from Google Sheets
def get_data():
    sheet = create_gsheets_connection()
    data = sheet.get_all_records()
    return data

# Streamlit app layout
def main():
    st.title("E-Operation Request System")

    menu = ["Submit Request", "View Requests"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Submit Request":
        st.subheader("Submit a New Request")
        requester_name = st.text_input("Requester Name")
        purpose = st.text_area("Purpose of Request")
        amount_requested = st.number_input("Amount Requested", min_value=0.0, step=0.01)

        if st.button("Submit"):
            if requester_name and purpose and amount_requested > 0:
                insert_data(requester_name, purpose, amount_requested)
            else:
                st.warning("Please fill out all fields correctly.")

    elif choice == "View Requests":
        st.subheader("All Submitted Requests")
        data = get_data()
        if data:
            st.write("### Submitted Requests")
            for row in data:
                st.write(f"Requester: {row['Requester name']}, Purpose: {row['Purpose']}, "
                         f"Amount: {row['amount requested']}, Date: {row['submission date']}")
        else:
            st.info("No data found.")

if __name__ == "__main__":
    main()
