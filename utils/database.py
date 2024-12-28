import pandas as pd
import os
from filelock import FileLock

DATABASE_FILE = "database.csv"
LOCK_FILE = DATABASE_FILE + ".lock"

def initialize_database():
    if not os.path.exists(DATABASE_FILE):
        columns = ["Reference ID", "Request Submission Date", "Requester Name", "Request Purpose", "Amount Requested", "Status"]
        pd.DataFrame(columns=columns).to_csv(DATABASE_FILE, index=False)

def read_data():
    if os.path.exists(DATABASE_FILE):
        return pd.read_csv(DATABASE_FILE)
    else:
        return pd.DataFrame(columns=["Reference ID", "Request Submission Date", "Requester Name", "Request Purpose", "Amount Requested", "Status"])

def write_data(data):
    with FileLock(LOCK_FILE):
        data.to_csv(DATABASE_FILE, index=False)

def update_request_status(reference_id, status):
    data = read_data()
    if reference_id in data["Reference ID"].values:
        data.loc[data["Reference ID"] == reference_id, "Status"] = status
        write_data(data)
        return True
    return False
