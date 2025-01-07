import streamlit as st
from datetime import datetime
import pandas as pd
from utils.database import read_data, write_data, get_next_transaction_id

def request_form_page():
    st.title("Request Form")
    st.subheader("Submit a New Request")

    # Options for dropdowns
    requester_names = ["Mohamed", "Abdulla", "Shayma"]
    project_names = ["Future Proof", "ACUW"]
    budget_lines = ["1.1", "1.2", "1.3", "1.4", "1.5"]

    # Form for submitting requests
    with st.form("request_form"):
        requester_name = st.selectbox("Requester Name", requester_names)
        project_name = st.selectbox("Project Name", project_names)
        budget_line = st.selectbox("Budget Line", budget_lines)
        request_purpose = st.text_area("Purpose of the Request")
        details_of_expenses = st.text_area("Details of Expenses")
        total_request_amount = st.number_input("Total Request Amount", min_value=1.0, step=0.01, format="%.2f")
        comment = st.text_area("Comment")

        # Submit button inside the form
        submit_button = st.form_submit_button("Submit Request")

    if submit_button:
        # Validation
        if not request_purpose.strip() or not details_of_expenses.strip() or total_request_amount <= 0:
            st.error("All fields are required. Please fill out the form completely.")
        else:
            # Read existing data
            data = read_data()

            # Generate new transaction details
            transaction_id = get_next_transaction_id(data)  # Generate unique Transaction ID
            submission_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create new transaction
            new_transaction = {
                "TRX ID": transaction_id,
                "TRX type": "Expense",  # Requests are categorized as "Expense"
                "TRX category": None,  # To be filled manually later
                "Project name": project_name,
                "Budget line": budget_line,
                "Purpose": request_purpose,
                "Detail": details_of_expenses,
                "Requested Amount": total_request_amount,
                "Approval Status": "Pending",  # Initial approval status
                "Approval date": None,  # Will be filled upon approval
                "Payment status": "Pending",  # Initial payment status
                "Payment date": None,
                "Liquidated amount": 0.0,  # Initial liquidated amount
                "Liquidation date": None,
                "Returned amount": 0.0,  # Initial returned amount
                "Liquidated invoices": None,
                "Related request ID": None,  # Can be linked later if applicable
                "Remarks": comment,
            }

            # Append new transaction to the DataFrame using pd.concat
            updated_data = pd.concat([data, pd.DataFrame([new_transaction])], ignore_index=True)

            # Write the updated data back to the database
            write_data(updated_data)

            st.success(f"Request submitted successfully with Transaction ID: {transaction_id}")
