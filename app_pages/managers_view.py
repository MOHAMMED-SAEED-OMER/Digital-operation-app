import streamlit as st
from utils.database import read_data, update_request_status

def managers_view_page():
    # Header with modern styling
    st.markdown("""
        <style>
        .page-header {
            text-align: center;
            color: #2E86C1;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .page-subheader {
            text-align: center;
            color: #566573;
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
        }
        </style>
        <div class="page-header">Manager's View</div>
        <div class="page-subheader">Review and manage pending requests efficiently</div>
    """, unsafe_allow_html=True)

    # Load data
    data = read_data()

    # Filter pending requests
    pending_requests = data[data["Status"] == "Pending"]

    if pending_requests.empty:
        st.markdown("<div style='text-align: center; font-size: 1.2rem; color: #27AE60;'>🎉 All requests have been reviewed!</div>", unsafe_allow_html=True)
    else:
        # Display pending requests
        st.dataframe(pending_requests)

        # Select a request to review
        selected_request = st.selectbox(
            "Select a request to review:",
            pending_requests["Reference ID"].values
        )

        if selected_request:
            # Show request details
            request_details = pending_requests[pending_requests["Reference ID"] == selected_request].iloc[0]
            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown(f"""
                <h4 style='color: #2E86C1;'>Request Details</h4>
                <ul style='list-style-type: none; padding: 0;'>
                    <li><strong>Requester Name:</strong> {request_details['Requester Name']}</li>
                    <li><strong>Purpose:</strong> {request_details['Request Purpose']}</li>
                    <li><strong>Amount Requested:</strong> ${request_details['Amount Requested']:.2f}</li>
                    <li><strong>Submission Date:</strong> {request_details['Request Submission Date']}</li>
                </ul>
            """, unsafe_allow_html=True)

            # Approve/Decline buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Approve Request", key=f"approve_{selected_request}"):
                    success = update_request_status(selected_request, "Approved")
                    if success:
                        st.success(f"Request {selected_request} has been approved.")
                        st.experimental_set_query_params(refresh=str(datetime.now()))  # Force refresh
                        st.stop()
                    else:
                        st.error("Failed to approve the request. Please try again.")
            with col2:
                if st.button("❌ Decline Request", key=f"decline_{selected_request}"):
                    success = update_request_status(selected_request, "Declined")
                    if success:
                        st.warning(f"Request {selected_request} has been declined.")
                        st.experimental_set_query_params(refresh=str(datetime.now()))  # Force refresh
                        st.stop()
                    else:
                        st.error("Failed to decline the request. Please try again.")
