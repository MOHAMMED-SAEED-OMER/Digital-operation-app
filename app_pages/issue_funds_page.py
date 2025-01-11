import streamlit as st
from datetime import datetime
from utils.database import read_data, update_finance_status

def issue_funds_page():
    # Page header with styling
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

    # Debugging: Display the database to confirm what data is being loaded
    st.write("**Database Debug View:**", data)

    # Filter approved requests that have not been issued
    if "Status" not in data.columns or "Finance Status" not in data.columns:
        st.error("The required columns ('Status' and 'Finance Status') are missing from the database.")
        return

    pending_issue_requests = data[(data["Status"] == "Approved") & (data["Finance Status"].isna())]

    # Debugging: Display the filtered data
    st.write("**Filtered Pending Requests:**", pending_issue_requests)

    if pending_issue_requests.empty:
        # Display a friendly message when no requests are pending
        st.markdown("<div class='no-requests'>🎉 All approved requests have been issued!</div>", unsafe_allow_html=True)
    else:
        # Display each pending request in a detailed format
        for i, row in pending_issue_requests.iterrows():
            st.markdown("<hr>", unsafe_allow_html=True)  # Add a separator between requests
            st.markdown(f"""
                <h4 style='color: #117A65;'>Request Details</h4>
                <ul style='list-style-type: none; padding: 0;'>
                    <li><strong>Request ID:</strong> {row['Reference ID']}</li>
                    <li><strong>Requester Name:</strong> {row['Requester Name']}</li>
                    <li><strong>Purpose:</strong> {row['Request Purpose']}</li>
                    <li><strong>Amount Requested:</strong> ${row['Amount Requested']:.2f}</li>
                </ul>
            """, unsafe_allow_html=True)

            # Add an "Issue Money" button
            if st.button(f"Issue Money for Request {row['Reference ID']}", key=f"issue_{row['Reference ID']}"):
                issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if update_finance_status(row["Reference ID"], "Issued", issue_date):
                    st.success(f"Funds for Request ID {row['Reference ID']} were successfully issued on {issue_date}.")
                else:
                    st.error("Failed to issue funds. Please try again.")

                # Trigger a page refresh
                st.session_state["reload_key"] = st.session_state.get("reload_key", 0) + 1
                st.experimental_rerun()
