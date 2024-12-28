import pandas as pd
import os
from filelock import FileLock

DATABASE_FILE = "database.csv"
LOCK_FILE = DATABASE_FILE + ".lock"

def initialize_database():
    if not os.path.exists(DATABASE_FILE):
        columns = ["Reference ID", "Request Submission Date", "Requester Name", "Request Purpose", "Amount Requested"]
        pd.DataFrame(columns=columns).to_csv(DATABASE_FILE, index=False)

def read_data():
    if os.path.exists(DATABASE_FILE):
        return pd.read_csv(DATABASE_FILE)
    else:
        return pd.DataFrame(columns=["Reference ID", "Request Submission Date", "Requester Name", "Request Purpose", "Amount Requested"])

def write_data(existing_data, new_request):
    new_data = pd.DataFrame([new_request])
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)

    with FileLock(LOCK_FILE):
        updated_data.to_csv(DATABASE_FILE, index=False)

def get_next_reference_id(data):
    if data.empty:
        return "REQ-001"
    else:
        max_id = int(data["Reference ID"].str.split("-").str[1].max())
        return f"REQ-{max_id + 1:03}"
