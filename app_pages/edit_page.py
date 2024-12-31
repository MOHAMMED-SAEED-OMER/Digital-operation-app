import streamlit as st
from utils.database import read_data, edit_request

def edit_page():
    st.title("Edit Database")
    st.subheader("Modify Existing Requests")

    # Load the data
    data = read_data()

    # Display all requests in a table
    st.write("### Existing Requests")
    st.dataframe(data)

    # Select a request to edit
    reference_id = st.selectbox("Select a Request ID to Edit", data["Reference ID"])

    if reference_id:
        # Get the selected request
        selected_request = data[data["Reference ID"] == reference_id].iloc[0]

        # Display editable fields
        requester_name = st.text_input("Requester Name", selected_request["Requester Name"])
        request_purpose = st.text_area("Request Purpose", selected_request["Request Purpose"])
        amount_requested = st.number_input(
            "Amount Requested", min_value=0.0, value=float(selected_request["Amount Requested"]), format="%.2f"
        )
        finance_status = st.selectbox(
            "Finance Status", ["Pending", "Issued", "Liquidated"], index=["Pending", "Issued", "Liquidated"].index(selected_request["Finance Status"])
        )
        liquidated = st.number_input(
            "Amount Liquidated", min_value=0.0, value=float(selected_request.get("Liquidated", 0.0)), format="%.2f"
        )
        # Allow negative values for `returned`
        returned = st.number_input(
            "Amount Returned", value=float(selected_request.get("Returned", 0.0)), format="%.2f"
        )
        liquidated_invoices = st.text_area("Liquidated Invoices", selected_request.get("Liquidated Invoices", ""))

        # Save changes
        if st.button("Save Changes"):
            updated_request = {
                "Requester Name": requester_name,
                "Request Purpose": request_purpose,
                "Amount Requested": amount_requested,
                "Finance Status": finance_status,
                "Liquidated": liquidated,
                "Returned": returned,
                "Liquidated Invoices": liquidated_invoices,
            }
            edit_request(reference_id, updated_request)
            st.success(f"Request ID {reference_id} updated successfully!")

            # Simulate a page refresh by reloading session state
            st.session_state["refresh_key"] = st.session_state.get("refresh_key", 0) + 1
            st.stop()  # Stops the current script execution to trigger a reload
