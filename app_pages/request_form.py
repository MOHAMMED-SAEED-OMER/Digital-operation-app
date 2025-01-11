import streamlit as st
from datetime import datetime
import pandas as pd
from utils.database import read_data, write_data, get_next_reference_id


def request_form_page():
    # Centered Title with Custom Styling
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h2 style="color: #2E8B57; font-family: Arial, sans-serif;">Submit a New Request</h2>
            <p style="color: #555; font-size: 16px;">Fill out the form below to submit your request</p>
        </div>
    """, unsafe_allow_html=True)

    # Form Design
    with st.form("request_form", clear_on_submit=True):
        # Form Columns for Layout
        col1, col2 = st.columns(2)

        with col1:
            requester_name = st.text_input(
                "Requester Name",
                placeholder="Enter your full name",
                help="Provide your name for identification."
            )
            amount_requested = st.number_input(
                "Amount Requested",
                min_value=0.0,
                step=0.01,
                format="%.2f",
                placeholder="Enter amount in USD",
                help="Specify the amount you need."
            )

        with col2:
            request_purpose = st.text_area(
                "Request Purpose",
                placeholder="Describe the purpose of your request",
                help="Provide detailed information about why you need the funds."
            )

        # Add spacing for a cleaner layout
        st.markdown("<br>", unsafe_allow_html=True)

        # Submit Button
        submit_button = st.form_submit_button(
            "Submit Request",
            type="primary"
        )

    # Process Form Submission
    if submit_button:
        if not requester_name.strip() or not request_purpose.strip() or amount_requested <= 0:
            st.error("⚠️ All fields are required. Please fill out the form completely.")
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
                "Finance Status": None,  # Default finance status
                "Issue Date": None,
                "Liquidated": 0.0,
                "Returned": 0.0,
                "Liquidated Invoices": None
            }

            # Write updated data back to the database
            write_data(data, new_request)

            # Success Message with Visual Indicator
            st.success(f"""
                ✅ **Request Submitted!**
                - **Reference ID:** {reference_id}
                - **Date:** {submission_date}
                """)
