import streamlit as st
from datetime import datetime
from utils.database import read_data, update_finance_status

def issue_funds_page():
    st.title("Issue Funds")
    st.subheader("Approve and Issue Money for Approved Requests")

    # Load data
    data = read_data()

    # Filter approved requests that have not been issued
    pending_issue_requests = data[(data["Status"] == "Approved") & (data["Finance Status"].isna())]

    if pending_issue_requests.empty:
        st.info("No approved requests to issue.")
    else:
        for i, row in pending_issue_requests.iterrows():
            st.write(f"### Request ID: {row['Reference ID']}")
            st.write(f"- **Requester Name**: {row['Requester Name']}")
            st.write(f"- **Request Purpose**: {row['Request Purpose']}")
            st.write(f"- **Amount Requested**: ${row['Amount Requested']:.2f}")

            # Add an "Issue Money" button
            if st.button(f"Issue Money for {row['Reference ID']}", key=f"issue_{row['Reference ID']}"):
                issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                update_finance_status(row["Reference ID"], "Issued", issue_date)
                st.success(f"Money issued for Request ID {row['Reference ID']} on {issue_date}.")
                st.session_state["reload_key"] = st.session_state.get("reload_key", 0) + 1  # Trigger a page reload
