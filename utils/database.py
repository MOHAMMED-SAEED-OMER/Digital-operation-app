import pandas as pd
import os
from filelock import FileLock

DATABASE_FILE = "database.csv"
LOCK_FILE = DATABASE_FILE + ".lock"

def get_next_reference_id(data):
    """
    Generate the next unique reference ID based on the existing data.
    """
    if data.empty:
        return "REQ-001"
    else:
        max_id = int(data["Reference ID"].str.split("-").str[1].max())
        return f"REQ-{max_id + 1:03}"

def initialize_database():
    """
    Initialize the database with required columns if it does not exist.
    """
    if not os.path.exists(DATABASE_FILE):
        columns = [
            "Reference ID",
            "Request Submission Date",
            "Requester Name",
            "Request Purpose",
            "Amount Requested",
            "Status",  # Approval status (Pending, Approved, Declined)
            "Finance Status",  # Finance status (Pending, Issued)
            "Issue Date",  # Date when money was issued
            "Liquidated",  # Amount spent (liquidated)
            "Returned",  # Amount returned (remaining)
            "Liquidated Invoices"  # Attached invoices (file paths or links)
        ]
        pd.DataFrame(columns=columns).to_csv(DATABASE_FILE, index=False)


def read_data():
    """
    Read the database into a Pandas DataFrame.
    """
    if os.path.exists(DATABASE_FILE):
        return pd.read_csv(DATABASE_FILE)
    else:
        return pd.DataFrame(columns=[
            "Reference ID",
            "Request Submission Date",
            "Requester Name",
            "Request Purpose",
            "Amount Requested",
            "Status",
            "Finance Status",
            "Issue Date",
            "Liquidated",
            "Returned",
            "Liquidated Invoices"
        ])

import streamlit as st
from utils.database import read_data, write_data

def managers_view_page():
    st.markdown("<h2 style='text-align: center;'>Manager's View</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Review and manage pending requests.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Load data
    data = read_data()

    if "Status" not in data.columns:
        st.error("The database is missing the 'Status' column.")
        return

    # Filter pending requests
    pending_requests = data[data["Status"] == "Pending"]

    if pending_requests.empty:
        st.info("No pending requests at the moment.")
    else:
        st.markdown("### Pending Requests")
        for i, row in pending_requests.iterrows():
            with st.container():
                st.markdown(f"""
                <div style='border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin-bottom: 15px; background-color: #f9f9f9;'>
                    <p><strong>Request ID:</strong> {row['Reference ID']}</p>
                    <p><strong>Requester Name:</strong> {row['Requester Name']}</p>
                    <p><strong>Request Purpose:</strong> {row['Request Purpose']}</p>
                    <p><strong>Amount Requested:</strong> ${row['Amount Requested']:.2f}</p>
                </div>
                """, unsafe_allow_html=True)

                # Approve and Decline buttons
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"Approve {row['Reference ID']}", key=f"approve_{row['Reference ID']}"):
                        data.loc[i, "Status"] = "Approved"
                        write_data(data)  # Save updated DataFrame
                        st.success(f"Request {row['Reference ID']} has been approved.")
                        st.stop()
                with col2:
                    if st.button(f"Decline {row['Reference ID']}", key=f"decline_{row['Reference ID']}"):
                        data.loc[i, "Status"] = "Declined"
                        write_data(data)  # Save updated DataFrame
                        st.warning(f"Request {row['Reference ID']} has been declined.")
                        st.stop()

        # Optional: Debugging - Show updated database
        if st.checkbox("Show updated database for debugging"):
            st.dataframe(data)


def update_request_status(reference_id, status):
    """
    Update the status of a specific request in the database.
    """
    data = read_data()
    if reference_id in data["Reference ID"].values:
        data.loc[data["Reference ID"] == reference_id, "Status"] = status
        with FileLock(LOCK_FILE):
            data.to_csv(DATABASE_FILE, index=False)
        return True
    return False

def update_finance_status(reference_id, finance_status, issue_date=None):
    """
    Update the finance status and issue date for a specific request.
    """
    data = read_data()
    if reference_id in data["Reference ID"].values:
        data.loc[data["Reference ID"] == reference_id, ["Finance Status", "Issue Date"]] = [finance_status, issue_date]
        with FileLock(LOCK_FILE):
            data.to_csv(DATABASE_FILE, index=False)
        return True
    return False

def update_liquidation_details(reference_id, liquidated, returned, invoices):
    """
    Update the liquidation details for a specific request.
    """
    data = read_data()
    if reference_id in data["Reference ID"].values:
        data.loc[data["Reference ID"] == reference_id, ["Liquidated", "Returned", "Liquidated Invoices"]] = [
            liquidated, returned, invoices
        ]
        with FileLock(LOCK_FILE):
            data.to_csv(DATABASE_FILE, index=False)
        return True
    return False

def edit_request(reference_id, updated_request):
    """
    Edit the details of a specific request in the database.
    """
    data = read_data()
    if reference_id in data["Reference ID"].values:
        for key, value in updated_request.items():
            if key in data.columns:
                data.loc[data["Reference ID"] == reference_id, key] = value
        with FileLock(LOCK_FILE):
            data.to_csv(DATABASE_FILE, index=False)
        return True
    return False
