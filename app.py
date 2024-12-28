import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from datetime import datetime
import uuid

# Google Sheets API Setup
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'keys/service_account.json'

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPE)
client = gspread.authorize(credentials)

# Connect to Google Sheet using URL and tab name
SHEET_URL = 'https://docs.google.com/spreadsheets/d/1PJ0F1NP9RVR3a3nB6O1sZO_4WlBrexRPRw33C7AjW8E/edit#gid=0'
sheet = client.open_by_url(SHEET_URL).worksheet('database')  # Replace 'database' with your tab name if different

# App Title
st.title("E-Operation Fund Request App")

# Form for Fund Request
st.header("Submit a Fund Request")
with st.form("fund_request_form"):
    requester_name = st.text_input("Requester Name")
    request_purpose = st.text_area("Request Purpose")
    amount_requested = st.number_input("Amount Requested", min_value=0.0, step=0.01)
    submit = st.form_submit_button("Submit Request")

    if submit:
        if requester_name and request_purpose and amount_requested > 0:
            # Generate Reference ID and Submission Date
            reference_id = str(uuid.uuid4())[:8]  # Unique 8-character ID
            submission_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Append data to Google Sheet
            sheet.append_row([reference_id, submission_date, requester_name, request_purpose, amount_requested])

            st.success(f"Your request has been submitted! Reference ID: {reference_id}")
        else:
            st.error("Please fill out all fields correctly.")

# Display Existing Requests
st.header("Existing Fund Requests")
data = sheet.get_all_records()
df = pd.DataFrame(data)
st.dataframe(df)
