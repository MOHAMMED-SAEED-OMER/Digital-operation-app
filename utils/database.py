import os
import pandas as pd
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
    Read the database as a Pandas DataFrame.
    """
    if os.path.exists(DATABASE_FILE):
        return pd.read_csv(DATABASE_FILE)
    else:
        initialize_database()
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

def write_data(data):
    """
    Save the updated DataFrame to the database.
    """
    with FileLock(LOCK_FILE):
        data.to_csv(DATABASE_FILE, index=False)

def get_next_reference_id(data):
    """
    Generate the next unique reference ID based on the existing data.
    """
    if data.empty:
        return "REQ-001"
    else:
        max_id = int(data["Reference ID"].str.split("-").str[1].max())
        return f"REQ-{max_id + 1:03}"
