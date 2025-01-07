# column_mapping.py

COLUMN_MAPPING = {
    "trx_id": "TRX ID",
    "trx_type": "TRX type",
    "trx_category": "TRX category",
    "project_name": "Project name",
    "budget_line": "Budget line",
    "purpose": "Purpose",
    "detail": "Detail",
    "requested_amount": "Requested Amount",
    "approval_status": "Approval Status",
    "approval_date": "Approval date",
    "payment_status": "Payment status",
    "payment_date": "Payment date",
    "liquidated_amount": "Liquidated amount",
    "liquidation_date": "Liquidation date",
    "returned_amount": "Returned amount",
    "liquidated_invoices": "Liquidated invoices",
    "related_request_id": "Related request ID",
    "remarks": "Remarks",
}

def get_column_name(key):
    """
    Retrieve the column name for a given key.
    """
    return COLUMN_MAPPING.get(key, key)  # Return the key itself if no mapping exists

def get_all_columns():
    """
    Retrieve all database columns from the mapping.
    """
    return list(COLUMN_MAPPING.values())
