import streamlit as st
from datetime import datetime
from utils.database import read_data, update_finance_status

def issue_funds_page():
    # Page header
    st.markdown("""
        <style>
        .page-header {
            text-align: center;
            color: #2E86C1;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .page-subheader {
            text-align: center;
            color: #5D6D7E;
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }
        .info-box {
            text-align: center;
            font-size: 1.2rem;
            color: #2E86C1;
            margin-top: 20px;
        }
        .request-card {
            border: 1px solid #D6DBDF;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
            background-color: #F4F6F7;
        }
        .request-card h4 {
            margin: 0;
            color: #2E86C1;
        }
        .request-card ul {
            list-style: none;
            padding: 0;
        }
        .request-card ul li {
            margin-bottom: 8px;
        }
        </style>
        <div class="page-header">Issue Funds</div>
        <div class="page-subheader">Approve and Issue Money for Approved Requests</div>
    """, unsafe_allow_html=True)

    # Load data
    data = read_data()

    # Filter approved requests that have not been issued
    pending_issue_requests = data[(data["Status"] == "Approved") & (data["Finance Status"].isna())]

    if pending_issue_requests.empty:
        st.markdown("<div class='info-box'>🎉 No approved requests to issue!</div>", unsafe_allow_html=True)
    else:
        for i, row in pending_issue_requests.iterrows():
            st.markdown("<div class='request-card'>", unsafe_allow_html=True)
            st.markdown(f"""
                <h4>Request Details</h4>
                <ul>
                    <li><strong>Request ID:</strong> {row['Reference ID']}</li>
                    <li><strong>Requester Name:</strong> {row['Requester Name']}</li>
                    <li><strong>Purpose:</strong> {row['Request Purpose']}</li>
                    <li><strong>Amount Requested:</strong> ${row['Amount Requested']:.2f}</li>
                </ul>
            """, unsafe_allow_html=True)

            # "Issue Money" button
            if st.button(f"Issue Money for {row['Reference ID']}", key=f"issue_{row['Reference ID']}"):
                issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                update_finance_status(row["Reference ID"], "Issued", issue_date)
                st.success(f"Funds for Request ID {row['Reference ID']} were successfully issued on {issue_date}.")
                st.session_state["reload_key"] = st.session_state.get("reload_key", 0) + 1  # Trigger a page reload

            st.markdown("</div>", unsafe_allow_html=True)

