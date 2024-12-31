import pandas as pd
import streamlit as st
from utils.database import read_data, write_data

def edit_page():
    st.title("Edit Database")
    st.subheader("Modify Existing Requests")

    # Load the data
    data = read_data()

    # Ensure there are requests to edit
    if data.empty:
        st.info("No requests found in the database.")
        return

    # Display all requests in a table
    st.write("### Existing Requests")
    st.dataframe(data)

    # Select a request to edit
    reference_id = st.selectbox("Select a Request ID to Edit", data["Reference ID"])

    if reference_id:
        # Get the selected request
        selected_request = data[data["Reference ID"] == reference_id].iloc[0]

        # Display fields for editing
        st.write("### Edit Request Details")
        requester_name = st.text_input("Requester Name", selected_request["Requester Name"])
        request_purpose = st.text_area("Request Purpose", selected_request["Request Purpose"])
        amount_requested = st.number_input(
            "Amount Requested", min_value=0.0, value=float(selected_request["Amount Requested"]), format="%.2f"
        )
        finance_status = st.selectbox(
            "Finance Status", options=["Pending", "Issued", "Liquidated"], index=["Pending", "Issued", "Liquidated"].index(selected_request["Finance Status"])
        )
        liquidated = st.number_input(
            "Amount Liquidated", min_value=0.0, value=float(selected_request["Liquidated"]), format="%.2f"
        )
        returned = st.number_input(
            "Amount Returned", min_value=0.0, value=float(selected_request["Returned"]), format="%.2f"
        )
        invoice_links = st.text_area("Invoice Links", selected_request["Invoice Links"])

        # Save changes
        if st.button("Save Changes"):
            # Update the selected row
            data.loc[data["Reference ID"] == reference_id, "Requester Name"] = requester_name
            data.loc[data["Reference ID"] == reference_id, "Request Purpose"] = request_purpose
            data.loc[data["Reference ID"] == reference_id, "Amount Requested"] = amount_requested
            data.loc[data["Reference ID"] == reference_id, "Finance Status"] = finance_status
            data.loc[data["Reference ID"] == reference_id, "Liquidated"] = liquidated
            data.loc[data["Reference ID"] == reference_id, "Returned"] = returned
            data.loc[data["Reference ID"] == reference_id, "Invoice Links"] = invoice_links

            # Save to the database
            write_data(data)

            st.success(f"Request ID {reference_id} updated successfully!")
