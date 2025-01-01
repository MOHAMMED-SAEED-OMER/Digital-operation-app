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
            "Transaction ID", "Transaction Type", "Date", "Amount",
            "Source/Purpose", "Category", "Project Name", "Budget Line",
            "Approval Status", "Finance Status", "Issue Date",
            "Liquidated", "Liquidation date", "Returned",
            "Liquidated Invoice link", "Related Request ID", "Details/Notes"
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
            "Transaction ID", "Transaction Type", "Date", "Amount",
            "Source/Purpose", "Category", "Project Name", "Budget Line",
            "Approval Status", "Finance Status", "Issue Date",
            "Liquidated", "Liquidation date", "Returned",
            "Liquidated Invoice link", "Related Request ID", "Details/Notes"
        ])

def write_data(data):
    """
    Save the DataFrame back to the database.
    """
    with FileLock(LOCK_FILE):
        data.to_csv(DATABASE_FILE, index=False)


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
