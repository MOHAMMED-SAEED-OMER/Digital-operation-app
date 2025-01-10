import streamlit as st
from utils.database import read_data, update_request_status

def managers_view_page():
    st.title("Manager's View")
    st.subheader("Approve or Decline Pending Requests")

    # Load data
    data = read_data()

    # Filter pending requests
    pending_requests = data[data["Status"] == "Pending"]

    if pending_requests.empty:
        st.info("No pending requests.")
    else:
        # Display pending requests
        st.dataframe(pending_requests)

        # Select a request to approve/decline
        selected_request = st.selectbox(
            "Select a Request to Review:",
            pending_requests["Reference ID"].values
        )

        if st.button("Approve"):
            if update_request_status(selected_request, "Approved"):
                st.success(f"Request {selected_request} has been approved.")
