import pandas as pd
import os
from filelock import FileLock

DATABASE_FILE = "database.csv"
LOCK_FILE = DATABASE_FILE + ".lock"

def initialize_database():
    """
    Initialize the database with the required columns if it does not exist.
    """
    if not os.path.exists(DATABASE_FILE):
        columns = [
            "Reference ID",
            "Request Submission Date",
            "Requester Name",
            "Request Purpose",
            "Amount Requested",
            "Status",  # Pending, Approved, Declined
            "Finance Status",  # Pending, Issued
            "Issue Date",
            "Liquidated",
            "Returned",
            "Liquidated Invoices",
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
        return pd.DataFrame()

def write_data(data):
    """
    Save the updated DataFrame to the database.
    """
    with FileLock(LOCK_FILE):
        data.to_csv(DATABASE_FILE, index=False)
