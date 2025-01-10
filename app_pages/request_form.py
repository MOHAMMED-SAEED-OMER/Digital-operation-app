import streamlit as st
from datetime import datetime
from utils.database import read_data, write_data, get_next_reference_id


def request_form_page():
    # Form Container
    st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <h2 style="color: #4CAF50;">Submit a New Request</h2>
            <p style="font-size: 18px; line-height: 1.6; color: #666;">
                Please fill out the form below to submit your request for funding.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Form Layout
    with st.form(key="request_form"):
        st.markdown("<h4 style='color: #4CAF50;'>Requester Information</h4>", unsafe_allow_html=True)
        requester_name = st.text_input("Requester Name")
        st.markdown("<hr style='margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)

        st.markdown("<h4 style='color: #4CAF50;'>Request Details</h4>", unsafe_allow_html=True)
        request_purpose = st.text_area("Request Purpose", placeholder="Enter a detailed purpose for the request.")
        amount_requested = st.number_input("Amount Requested (in $)", min_value=0.0, format="%.2f", step=0.01)
        st.markdown("<hr style='margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)

        # Submit Button
        submit_button = st.form_submit_button(label="Submit Request", type="primary")

    # Handle Form Submission
    if submit_button:
        if requester_name.strip() == "" or request_purpose.strip() == "" or amount_requested <= 0:
            st.error("All fields are required. Please fill out the form completely.")
        else:
            # Read existing data
            data = read_data()

            # Generate new request details
            reference_id = get_next_reference_id(data)
            submission_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create new request
            new_request = {
                "Reference ID": reference_id,
                "Request Submission Date": submission_date,
                "Requester Name": requester_name,
                "Request Purpose": request_purpose,
                "Amount Requested": amount_requested,
                "Status": "Pending",  # Set initial status
            }

            # Write to the database
            write_data(data, new_request)

            # Success message with confirmation
            st.markdown(f"""
                <div style="text-align: center; margin-top: 20px; padding: 10px; background-color: #e8f5e9; border-radius: 8px;">
                    <h3 style="color: #4CAF50;">Request Submitted Successfully!</h3>
                    <p>Reference ID: <b>{reference_id}</b></p>
                    <p>Your request has been submitted for review. You will be notified once it's processed.</p>
                </div>
            """, unsafe_allow_html=True)
