import streamlit as st
from datetime import datetime
from utils.database import read_data, write_data

def issue_funds_page():
    # Header
    st.markdown("<h2 style='text-align: center;'>Issue Funds</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Approve and issue funds for approved requests.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Load data from the database
    data = read_data()

    # Ensure the required columns exist
    if "Status" not in data.columns or "Finance Status" not in data.columns:
        st.error("The database is missing required columns: 'Status' or 'Finance Status'.")
        return

    # Filter approved requests with no finance status (i.e., pending issuance)
    approved_requests = data[(data["Status"] == "Approved") & (data["Finance Status"].isna())]

    if approved_requests.empty:
        st.info("No approved requests to issue at the moment.")
    else:
        st.markdown("### Approved Requests Pending Issuance")
        
        for i, row in approved_requests.iterrows():
            # Display the request details
            with st.container():
                st.markdown(f"""
                <div style='border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin-bottom: 15px; background-color: #f9f9f9;'>
                    <p><strong>Request ID:</strong> {row['Reference ID']}</p>
                    <p><strong>Requester Name:</strong> {row['Requester Name']}</p>
                    <p><strong>Request Purpose:</strong> {row['Request Purpose']}</p>
                    <p><strong>Amount Requested:</strong> ${row['Amount Requested']:.2f}</p>
                </div>
                """, unsafe_allow_html=True)

                # Button to issue funds
                if st.button(f"Issue Funds for {row['Reference ID']}", key=f"issue_{row['Reference ID']}"):
                    # Update the finance status
                    issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    data.loc[i, "Finance Status"] = "Issued"
                    data.loc[i, "Issue Date"] = issue_date

                    # Write the updated data back to the database
                    write_data(data)

                    st.success(f"Funds issued successfully for Request ID {row['Reference ID']} on {issue_date}.")

                    # Break out of the loop to refresh the display
                    break

        # Optional: Display updated data for debugging
        if st.checkbox("Show updated database"):
            st.dataframe(data)
