import streamlit as st
from utils.database import read_data, write_data

def managers_view_page():
    st.markdown("<h2 style='text-align: center;'>Manager's View</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Review and manage pending requests.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Load data
    data = read_data()

    if "Status" not in data.columns:
        st.error("The database is missing the 'Status' column.")
        return

    # Filter pending requests
    pending_requests = data[data["Status"] == "Pending"]

    if pending_requests.empty:
        st.info("No pending requests at the moment.")
    else:
        st.markdown("### Pending Requests")
        for i, row in pending_requests.iterrows():
            with st.container():
                st.markdown(f"""
                <div style='border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin-bottom: 15px; background-color: #f9f9f9;'>
                    <p><strong>Request ID:</strong> {row['Reference ID']}</p>
                    <p><strong>Requester Name:</strong> {row['Requester Name']}</p>
                    <p><strong>Request Purpose:</strong> {row['Request Purpose']}</p>
                    <p><strong>Amount Requested:</strong> ${row['Amount Requested']:.2f}</p>
                </div>
                """, unsafe_allow_html=True)

                # Approve and Decline buttons
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"Approve {row['Reference ID']}", key=f"approve_{row['Reference ID']}"):
                        data.loc[i, "Status"] = "Approved"
                        write_data(data)  # Save updated DataFrame
                        st.success(f"Request {row['Reference ID']} has been approved.")
                        st.stop()
                with col2:
                    if st.button(f"Decline {row['Reference ID']}", key=f"decline_{row['Reference ID']}"):
                        data.loc[i, "Status"] = "Declined"
                        write_data(data)  # Save updated DataFrame
                        st.warning(f"Request {row['Reference ID']} has been declined.")
                        st.stop()

        # Optional: Debugging - Show updated database
        if st.checkbox("Show updated database for debugging"):
            st.dataframe(data)
