import pandas as pd
import os
from filelock import FileLock

DATABASE_FILE = "database.csv"
LOCK_FILE = DATABASE_FILE + ".lock"

def write_data(existing_data, new_request=None):
    """
    Save the database. If a new_request is provided, it appends it to the data.
    Otherwise, overwrites the database with the existing_data.
    """
    with FileLock(LOCK_FILE):
        if new_request is not None:
            # Append the new request to the existing data
            new_data = pd.DataFrame([new_request])
            updated_data = pd.concat([existing_data, new_data], ignore_index=True)
            updated_data.to_csv(DATABASE_FILE, index=False)
        else:
            # Overwrite the entire data with existing_data
            existing_data.to_csv(DATABASE_FILE, index=False)
