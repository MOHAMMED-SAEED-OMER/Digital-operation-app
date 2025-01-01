import streamlit as st
from datetime import datetime
from utils.database import read_data, write_data, get_next_reference_id

def request_form_page():
    st.title("Request Form")
    st.subheader("Submit a New Request")

    # Options for dropdowns
    requester_names = ["Mohamed", "Abdulla", "Shayma"]
    project_names = ["Future Proof", "ACUW"]
    budget_lines = ["1.1.1", "1.1.2", "1.1.3"]

    # Form for submitting requests
    with st.form("request_form"):
        requester_name = st.selectbox("Requester Name", requester_names)
        project_name = st.selectbox("Project Name", project_names)
        budget_line = st.selectbox("Budget Line", budget_lines)
        request_purpose = st.text_area("Request Purpose")
        amount_requested = st.number_input("Amount Requested", min_value=1, step=1, format="%d")
        note = st.text_area("Details/Notes")

        # Submit button inside the form
        submit_button = st.form_submit_button("Submit Request")

    if submit_button:
        # Validation
        if not request_purpose.strip() or amount_requested <= 0:
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
                "Category": "Expense",  # Fixed category for now
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
                "Details/Notes": note,
            }

            # Write to the database
            write_data(data.append(new_request, ignore_index=True))

            st.success(f"Request submitted successfully with Transaction ID: {transaction_id}")
