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
                    # Refresh the page to update the display
                    refresh_page()
                else:
                    st.error("Failed to update the request status.")
        with col2:
            if st.button("Decline"):
                if update_request_status(selected_request, "Declined"):
                    st.warning(f"Request {selected_request} has been declined.")
                    # Refresh the page to update the display
                    refresh_page()
                else:
                    st.error("Failed to update the request status.")


def refresh_page():
    """
    Refresh the page to update the display.
    Handles compatibility with different Streamlit versions.
    """
    if "refresh_key" not in st.session_state:
        st.session_state["refresh_key"] = 0

    st.session_state["refresh_key"] += 1  # Increment refresh key
    try:
        # Use the latest Streamlit's query_params functionality if available
        st.set_query_params(refresh=str(st.session_state["refresh_key"]))
    except AttributeError:
        # Fallback for older Streamlit versions
        st.experimental_rerun()
