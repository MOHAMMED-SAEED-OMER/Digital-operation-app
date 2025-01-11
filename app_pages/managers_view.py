import streamlit as st
from utils.database import read_data, update_request_status

def managers_view_page():
    # Page header
    st.markdown("<h1 style='text-align: center; color: #007BFF;'>Manager's View</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Review and manage pending requests</h4>", unsafe_allow_html=True)

    # Load data
    data = read_data()

    # Filter pending requests
    pending_requests = data[data["Status"] == "Pending"]

    # Display message if no pending requests
    if pending_requests.empty:
        st.info("🎉 No pending requests at the moment. Great job staying on top of approvals!")
    else:
        st.markdown("<h5 style='margin-top: 20px;'>Pending Requests</h5>", unsafe_allow_html=True)
        
        # Display pending requests in a styled table
        st.dataframe(
            pending_requests.style.set_properties(
                **{"background-color": "#f9f9f9", "color": "#333", "border": "1px solid #ddd"}
            )
        )

        # Select a request to review
        selected_request = st.selectbox(
            "Select a request to review",
            pending_requests["Reference ID"].values,
            help="Choose a request ID to approve or decline"
        )

        # Display selected request details
        if selected_request:
            request_details = pending_requests[pending_requests["Reference ID"] == selected_request].iloc[0]
            st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
            st.markdown(f"""
                <h5 style='color: #555;'>Selected Request Details</h5>
                <ul>
                    <li><strong>Requester Name:</strong> {request_details['Requester Name']}</li>
                    <li><strong>Purpose:</strong> {request_details['Request Purpose']}</li>
                    <li><strong>Amount:</strong> ${request_details['Amount Requested']:.2f}</li>
                    <li><strong>Submission Date:</strong> {request_details['Request Submission Date']}</li>
                </ul>
            """, unsafe_allow_html=True)

            # Approval and Decline buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Approve", help="Approve this request"):
                    if update_request_status(selected_request, "Approved"):
                        st.success(f"Request {selected_request} has been approved.")
                    else:
                        st.error("Failed to update the request status.")
            with col2:
                if st.button("❌ Decline", help="Decline this request"):
                    if update_request_status(selected_request, "Declined"):
                        st.warning(f"Request {selected_request} has been declined.")
                    else:
                        st.error("Failed to update the request status.")
