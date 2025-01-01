import pandas as pd
import os
from filelock import FileLock

DATABASE_FILE = "database.csv"
LOCK_FILE = DATABASE_FILE + ".lock"

def get_next_reference_id(data):
    """
    Generate the next unique transaction ID based on the existing data.
    """
    if data.empty or "Transaction ID" not in data.columns:
        return "TRX-0001"
    else:
        # Extract numeric part from Transaction ID and calculate the next ID
        max_id = data["Transaction ID"].str.extract(r'(\d+)$').astype(int).max()[0]
        return f"TRX-{max_id + 1:04d}"

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

def update_request_status(transaction_id, status):
    """
    Update the approval status of a specific transaction in the database.
    """
    data = read_data()
    if transaction_id in data["Transaction ID"].values:
        data.loc[data["Transaction ID"] == transaction_id, "Approval Status"] = status
        write_data(data)
        return True
    return False

def update_finance_status(transaction_id, finance_status, issue_date=None):
    """
    Update the finance status and issue date for a specific transaction.
    """
    data = read_data()
    if transaction_id in data["Transaction ID"].values:
        data.loc[data["Transaction ID"] == transaction_id, ["Finance Status", "Issue Date"]] = [finance_status, issue_date]
        write_data(data)
        return True
    return False

def update_liquidation_details(transaction_id, liquidated, returned, invoices):
    """
    Update the liquidation details for a specific transaction.
    """
    data = read_data()
    if transaction_id in data["Transaction ID"].values:
        data.loc[data["Transaction ID"] == transaction_id, ["Liquidated", "Returned", "Liquidated Invoice link"]] = [
            liquidated, returned, invoices
        ]
        write_data(data)
        return True
    return False

def edit_request(transaction_id, updated_request):
    """
    Edit the details of a specific transaction in the database.
    """
    data = read_data()
    if transaction_id in data["Transaction ID"].values:
        for key, value in updated_request.items():
            if key in data.columns:
                data.loc[data["Transaction ID"] == transaction_id, key] = value
        write_data(data)
        return True
    return False

