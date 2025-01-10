import streamlit as st
from datetime import datetime
import pandas as pd
from utils.database import read_data, write_data, get_next_reference_id


def request_form_page():
    st.markdown("<h2 style='text-align: center;'>Submit a New Request</h2>", unsafe_allow_html=True)

    # Form fields
    with st.form("request_form"):
        requester_name = st.text_input("Requester Name")
        request_purpose = st.text_area("Request Purpose")
        amount_requested = st.number_input("Amount Requested", min_value=0.0, format="%.2f")

        # Submit button inside the form
        submit_button = st.form_submit_button("Submit Request")

    if submit_button:
        if not requester_name.strip() or not request_purpose.strip() or amount_requested <= 0:
            st.error("All fields are required. Please fill out the form completely.")
        else:
            # Read existing data
            data = read_data()

            # Generate new request details
            reference_id = get_next_reference_id(data)
            submission_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create new request details
            new_request = {
                "Reference ID": reference_id,
                "Request Submission Date": submission_date,
                "Requester Name": requester_name,
                "Request Purpose": request_purpose,
                "Amount Requested": amount_requested,
                "Status": "Pending",  # Default status
                "Finance Status": "Pending",  # Default finance status
                "Issue Date": None,
                "Liquidated": 0.0,
                "Returned": 0.0,
                "Liquidated Invoices": None
            }

            # Write updated data back to the database
            write_data(data, new_request)

            st.success(f"Request submitted successfully with Reference ID: {reference_id}")
