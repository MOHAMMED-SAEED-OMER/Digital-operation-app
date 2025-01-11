import pandas as pd
import os
from filelock import FileLock

DATABASE_FILE = "database.csv"
LOCK_FILE = DATABASE_FILE + ".lock"

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

def write_data(updated_data):
    """
    Write the updated DataFrame to the database.
    """
    with FileLock(LOCK_FILE):
        updated_data.to_csv(DATABASE_FILE, index=False)

def update_request_status(reference_id, status):
    """
    Update the status of a specific request in the database.
    """
    data = read_data()
    if reference_id in data["Reference ID"].values:
        data.loc[data["Reference ID"] == reference_id, "Status"] = status
        write_data(data)
        return True
    return False

def update_finance_status(reference_id, finance_status, issue_date=None):
    """
    Update the finance status and issue date for a specific request.
    """
    data = read_data()
    if reference_id in data["Reference ID"].values:
        data.loc[data["Reference ID"] == reference_id, ["Finance Status", "Issue Date"]] = [finance_status, issue_date]
        write_data(data)
        return True
    return False
