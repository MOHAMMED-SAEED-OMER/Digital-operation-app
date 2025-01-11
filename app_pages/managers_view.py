import streamlit as st
from utils.database import read_data, update_request_status

def managers_view_page():
    # Page Title with Centered Styling
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h2 style="color: #2E8B57; font-family: Arial, sans-serif;">Manager's View</h2>
            <p style="color: #555; font-size: 16px;">Approve or Decline Pending Requests</p>
        </div>
    """, unsafe_allow_html=True)

    # Load data
    data = read_data()

    # Filter pending requests
    pending_requests = data[data["Status"] == "Pending"]

    if pending_requests.empty:
        # Informative Message
        st.info("🎉 No pending requests at the moment. All caught up!")
    else:
        # Display pending requests in a styled container
        st.markdown("### Pending Requests")
        for index, row in pending_requests.iterrows():
            with st.container():
                st.markdown(f"""
                <div style="border: 1px solid #ddd; padding: 15px; border-radius: 10px; margin-bottom: 15px; background-color: #f9f9f9;">
                    <p><strong>Request ID:</strong> {row['Reference ID']}</p>
                    <p><strong>Requester Name:</strong> {row['Requester Name']}</p>
                    <p><strong>Purpose:</strong> {row['Request Purpose']}</p>
                    <p><strong>Amount:</strong> ${row['Amount Requested']:.2f}</p>
                </div>
                """, unsafe_allow_html=True)

                # Approve and Decline Buttons
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Approve", key=f"approve_{row['Reference ID']}"):
                        if update_request_status(row['Reference ID'], "Approved"):
                            st.success(f"✅ Request {row['Reference ID']} has been approved.")
                            st.session_state["refresh_key"] = st.session_state.get("refresh_key", 0) + 1  # Increment refresh key
                            st.experimental_set_query_params(refresh=str(st.session_state["refresh_key"]))
                            st.stop()  # Stops execution to ensure updated view
                        else:
                            st.error("❌ Failed to update the request status.")
                with col2:
                    if st.button("Decline", key=f"decline_{row['Reference ID']}"):
                        if update_request_status(row['Reference ID'], "Declined"):
                            st.warning(f"⚠️ Request {row['Reference ID']} has been declined.")
                            st.session_state["refresh_key"] = st.session_state.get("refresh_key", 0) + 1
                            st.experimental_set_query_params(refresh=str(st.session_state["refresh_key"]))
                            st.stop()
                        else:
                            st.error("❌ Failed to update the request status.")
