import streamlit as st
from datetime import datetime
from utils.database import read_data, update_finance_status

def issue_funds_page():
    # Page header
    st.markdown("""
        <style>
        .page-header {
            text-align: center;
            color: #117A65;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .page-subheader {
            text-align: center;
            color: #566573;
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
        }
        .no-requests {
            text-align: center;
            font-size: 1.2rem;
            color: #117A65;
            margin-top: 20px;
        }
        </style>
        <div class="page-header">Issue Funds</div>
        <div class="page-subheader">Review and issue funds for approved requests</div>
    """, unsafe_allow_html=True)

    # Load data
    data = read_data()

    # Ensure required columns are present
    if "Status" not in data.columns or "Finance Status" not in data.columns:
        st.error("The database is missing required columns ('Status' or 'Finance Status').")
        return

    # Filter approved requests that have not been issued
    pending_issue_requests = data[
        (data["Status"] == "Approved") &
        (data["Finance Status"].isna() | (data["Finance Status"] == "Pending"))
    ]

    if pending_issue_requests.empty:
        st.markdown("<div class='no-requests'>🎉 All approved requests have been issued!</div>", unsafe_allow_html=True)
    else:
        for i, row in pending_issue_requests.iterrows():
            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown(f"""
                <h4 style='color: #117A65;'>Request Details</h4>
                <ul style='list-style-type: none; padding: 0;'>
                    <li><strong>Request ID:</strong> {row['Reference ID']}</li>
                    <li><strong>Requester Name:</strong> {row['Requester Name']}</li>
                    <li><strong>Purpose:</strong> {row['Request Purpose']}</li>
                    <li><strong>Amount Requested:</strong> ${row['Amount Requested']:.2f}</li>
                </ul>
            """, unsafe_allow_html=True)

            # "Issue Money" button
            if st.button(f"Issue Money for {row['Reference ID']}", key=f"issue_{row['Reference ID']}"):
                issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if update_finance_status(row["Reference ID"], "Issued", issue_date):
                    st.success(f"Funds for Request ID {row['Reference ID']} were successfully issued on {issue_date}.")
                else:
                    st.error("Failed to issue funds. Please try again.")

                # Refresh the page using query parameters
                st.set_query_params(reload=str(datetime.now()))
                return  # Stop further execution to reflect changes
