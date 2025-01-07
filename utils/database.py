import pandas as pd
import os
from filelock import FileLock

DATABASE_FILE = "database.csv"
LOCK_FILE = DATABASE_FILE + ".lock"

def get_next_transaction_id(data):
    """
    Generate the next unique transaction ID based on the existing data.
    """
    if data.empty or "TRX ID" not in data.columns:
        return "TRX-0001"
    else:
        # Extract numeric part from Transaction ID and calculate the next ID
        max_id = data["TRX ID"].str.extract(r'(\d+)$').astype(int).max()[0]
        return f"TRX-{max_id + 1:04d}"

def initialize_database():
    """
    Initialize the database with required columns if it does not exist.
    """
    if not os.path.exists(DATABASE_FILE):
        columns = [
            "TRX ID", "TRX type", "TRX category", "Project name",
            "Budget line", "Purpose", "Detail", "Requested Amount",
            "Approval Status", "Approval date", "Payment status", "Payment date",
            "Liquidated amount", "Liquidation date", "Returned amount",
            "Liquidated invoices", "Related request ID", "Remarks"
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
            "TRX ID", "TRX type", "TRX category", "Project name",
            "Budget line", "Purpose", "Detail", "Requested Amount",
            "Approval Status", "Approval date", "Payment status", "Payment date",
            "Liquidated amount", "Liquidation date", "Returned amount",
            "Liquidated invoices", "Related request ID", "Remarks"
        ])

def write_data(data):
    """
    Save the DataFrame back to the database.
    """
    with FileLock(LOCK_FILE):
        data.to_csv(DATABASE_FILE, index=False)

def update_approval_status(trx_id, status):
    """
    Update the approval status and date of a specific transaction in the database.
    """
    data = read_data()
    if trx_id in data["TRX ID"].values:
        data.loc[data["TRX ID"] == trx_id, "Approval Status"] = status
        data.loc[data["TRX ID"] == trx_id, "Approval date"] = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        write_data(data)
        return True
    return False

def update_payment_status(trx_id, payment_status, payment_date=None):
    """
    Update the payment status and date for a specific transaction.
    """
    data = read_data()
    if trx_id in data["TRX ID"].values:
        data.loc[data["TRX ID"] == trx_id, ["Payment status", "Payment date"]] = [
            payment_status,
            payment_date or pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        ]
        write_data(data)
        return True
    return False

def update_liquidation_details(trx_id, liquidated_amount, invoices):
    """
    Update the liquidation details for a specific transaction.
    """
    data = read_data()
    if trx_id in data["TRX ID"].values:
        requested_amount = data.loc[data["TRX ID"] == trx_id, "Requested Amount"].values[0]
        returned_amount = requested_amount - liquidated_amount

        data.loc[data["TRX ID"] == trx_id, ["Liquidated amount", "Liquidation date", "Returned amount", "Liquidated invoices"]] = [
            liquidated_amount,
            pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
            returned_amount,
            invoices
        ]
        write_data(data)
        return True
    return False

def edit_transaction(trx_id, updated_transaction):
    """
    Edit the details of a specific transaction in the database.
    """
    data = read_data()
    if trx_id in data["TRX ID"].values:
        for key, value in updated_transaction.items():
            if key in data.columns:
                data.loc[data["TRX ID"] == trx_id, key] = value
        write_data(data)
        return True
    return False

def ensure_columns_exist(data):
    """
    Ensure all required columns exist in the database, add missing columns if needed.
    """
    required_columns = [
        "TRX ID", "TRX type", "TRX category", "Project name",
        "Budget line", "Purpose", "Detail", "Requested Amount",
        "Approval Status", "Approval date", "Payment status", "Payment date",
        "Liquidated amount", "Liquidation date", "Returned amount",
        "Liquidated invoices", "Related request ID", "Remarks"
    ]
    for col in required_columns:
        if col not in data.columns:
            data[col] = None
    return data
