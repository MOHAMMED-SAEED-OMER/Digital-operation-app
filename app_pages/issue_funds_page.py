import streamlit as st
from datetime import datetime
from utils.database import read_data, update_finance_status

def issue_funds_page():
    st.markdown("<h2 style='text-align: center;'>Issue Funds</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Approve and issue funds for approved requests.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Load data from the database
    data = read_data()

    # Ensure required columns exist and fill missing columns with default values
    if "Status" not in data.columns or "Finance Status" not in data.columns:
        st.error("The database is missing required columns: 'Status' or 'Finance Status'.")
        return

    # Ensure Finance Status is properly filled
    data["Finance Status"] = data["Finance Status"].fillna("Pending")

    # Filter approved requests with no finance status (i.e., pending issuance)
    approved_requests = data[(data["Status"] == "Approved") & (data["Finance Status"] == "Pending")]

    if approved_requests.empty:
        st.info("No approved requests to issue at the moment.")
    else:
        st.markdown("### Approved Requests Pending Issuance")
        for i, row in approved_requests.iterrows():
            st.markdown(f"""
            <div style='border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin-bottom: 15px; background-color: #f9f9f9;'>
                <p><strong>Request ID:</strong> {row['Reference ID']}</p>
                <p><strong>Requester Name:</strong> {row['Requester Name']}</p>
                <p><strong>Request Purpose:</strong> {row['Request Purpose']}</p>
                <p><strong>Amount Requested:</strong> ${row['Amount Requested']:.2f}</p>
            </div>
            """, unsafe_allow_html=True)

            # Issue funds button
            if st.button(f"Issue Money for {row['Reference ID']}", key=f"issue_{row['Reference ID']}"):
                issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                update_finance_status(row["Reference ID"], "Issued", issue_date)
                st.success(f"Money issued for Request ID {row['Reference ID']} on {issue_date}.")

                # Refresh the page
                st.experimental_rerun()
