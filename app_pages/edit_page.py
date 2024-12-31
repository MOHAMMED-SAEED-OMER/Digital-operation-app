import streamlit as st
import pandas as pd
from utils.database import read_data, write_data

def edit_page():
    st.title("Edit Database")
    st.subheader("Modify Existing Requests")

    # Load the existing data
    data = read_data()

    # Display all requests in a table for reference
    st.write("### Existing Requests")
    st.dataframe(data)

    # Select a request to edit
    reference_id = st.selectbox("Select a Request ID to Edit", data["Reference ID"])

    if reference_id:
        # Get the selected request
        selected_request = data[data["Reference ID"] == reference_id].iloc[0]

        # Display editable fields for the selected request
        st.write("### Edit Request Details")
        requester_name = st.text_input("Requester Name", selected_request["Requester Name"])
        request_purpose = st.text_area("Request Purpose", selected_request["Request Purpose"])
        amount_requested = st.number_input(
            "Amount Requested", min_value=0.0, value=float(selected_request["Amount Requested"]), format="%.2f"
        )
        finance_status = st.selectbox(
            "Finance Status",
            options=["Pending", "Issued", "Liquidated"],
            index=["Pending", "Issued", "Liquidated"].index(selected_request["Finance Status"]),
        )
        liquidated = st.number_input(
            "Amount Liquidated", min_value=0.0, value=float(selected_request.get("Liquidated", 0.0)), format="%.2f"
        )
        returned = st.number_input(
            "Amount Returned", min_value=0.0, value=float(selected_request.get("Returned", 0.0)), format="%.2f"
        )
        liquidated_invoices = st.text_area(
            "Liquidated Invoices", selected_request.get("Liquidated Invoices", "")
        )

        # Save changes
        if st.button("Save Changes"):
            # Update the selected row
            data.loc[data["Reference ID"] == reference_id, "Requester Name"] = requester_name
            data.loc[data["Reference ID"] == reference_id, "Request Purpose"] = request_purpose
            data.loc[data["Reference ID"] == reference_id, "Amount Requested"] = amount_requested
            data.loc[data["Reference ID"] == reference_id, "Finance Status"] = finance_status
            data.loc[data["Reference ID"] == reference_id, "Liquidated"] = liquidated
            data.loc[data["Reference ID"] == reference_id, "Returned"] = returned
            data.loc[data["Reference ID"] == reference_id, "Liquidated Invoices"] = liquidated_invoices

            # Overwrite the entire database with updated data
            with open("database.csv", "w") as f:
                data.to_csv(f, index=False)

            st.success(f"Request ID {reference_id} updated successfully!")
            st.experimental_rerun()
