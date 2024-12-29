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
            "Status",          # Approval status (Pending, Approved, Declined)
            "Finance Status",  # Finance status (Pending, Issued)
            "Issue Date"       # Date when money was issued
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
            "Issue Date"
        ])

def write_data(existing_data, new_request):
    """
    Add a new request to the existing data and save to the database.
    """
    # Convert new_request to a DataFrame
    new_data = pd.DataFrame([new_request])

    # Concatenate new data with the existing data
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)

    # Save the updated data to the database file
    with FileLock(LOCK_FILE):
        updated_data.to_csv(DATABASE_FILE, index=False)

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
