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
        st.markdown("### Pending Requests")
        st.dataframe(pending_requests)

        # Select a request to approve/decline
        selected_request = st.selectbox(
            "Select a Request to Review:",
            pending_requests["Reference ID"].values
        )

        # Approve and Decline buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Approve"):
                if update_request_status(selected_request, "Approved"):
                    st.success(f"Request {selected_request} has been approved.")
                    # Trigger a refresh by updating session state
                    st.session_state["refresh"] = True
                else:
                    st.error("Failed to update the request status.")
        with col2:
            if st.button("Decline"):
                if update_request_status(selected_request, "Declined"):
                    st.warning(f"Request {selected_request} has been declined.")
                    # Trigger a refresh by updating session state
                    st.session_state["refresh"] = True
                else:
                    st.error("Failed to update the request status.")

        # Check if refresh is triggered
        if "refresh" in st.session_state and st.session_state["refresh"]:
            st.session_state["refresh"] = False
            st.experimental_rerun()  # Ensures the page reloads to show updated data
