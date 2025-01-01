import streamlit as st
from datetime import datetime
from utils.database import read_data, write_data, get_next_reference_id

def request_form_page():
    st.title("Request Form")
    st.subheader("Submit a New Request")

    # Form for submitting requests
    with st.form("request_form"):
        requester_name = st.text_input("Requester Name")
        request_purpose = st.text_area("Request Purpose")
        amount_requested = st.number_input("Amount Requested", min_value=0.0, format="%.2f")
        category = st.text_input("Category")  # New column for the category
        project_name = st.text_input("Project Name")  # New column for project name
        budget_line = st.text_input("Budget Line")  # New column for budget line

        # Submit button inside the form
        submit_button = st.form_submit_button("Submit Request")

    if submit_button:
        # Validation
        if not requester_name.strip() or not request_purpose.strip() or amount_requested <= 0:
            st.error("All fields are required. Please fill out the form completely.")
        else:
            # Read existing data
            data = read_data()

            # Generate new request details
            transaction_id = get_next_reference_id(data)  # Generate unique Transaction ID
            submission_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create new request
            new_request = {
                "Transaction ID": transaction_id,
                "Transaction Type": "Expense",  # Requests are categorized as "Expense"
                "Date": submission_date,
                "Amount": amount_requested,
                "Source/Purpose": request_purpose,
                "Category": category,
                "Project Name": project_name,
                "Budget Line": budget_line,
                "Approval Status": "Pending",  # Initial approval status
                "Finance Status": "Pending",  # Initial finance status
                "Issue Date": None,
                "Liquidated": 0.0,  # Initial liquidated amount
                "Liquidation date": None,
                "Returned": 0.0,  # Initial returned amount
                "Liquidated Invoice link": None,
                "Related Request ID": None,
                "Details/Notes": None,
            }

            # Write to the database
            write_data(data.append(new_request, ignore_index=True))

            st.success(f"Request submitted successfully with Transaction ID: {transaction_id}")
