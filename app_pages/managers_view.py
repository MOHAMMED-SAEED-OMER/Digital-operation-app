import streamlit as st
from utils.database import read_data, write_data

def managers_view_page():
    st.title("Manager's View")
    st.write("Review and manage pending requests.")

    # Load data
    data = read_data()

    # Check if required columns exist
    if "Status" not in data.columns:
        st.error("The database is missing the 'Status' column.")
        return

    # Filter pending requests
    pending_requests = data[data["Status"] == "Pending"]

    if pending_requests.empty:
        st.info("No pending requests at the moment.")
    else:
        st.subheader("Pending Requests")
        for i, row in pending_requests.iterrows():
            with st.container():
                st.markdown(f"""
                **Request ID:** {row['Reference ID']}  
                **Requester Name:** {row['Requester Name']}  
                **Request Purpose:** {row['Request Purpose']}  
                **Amount Requested:** ${row['Amount Requested']:.2f}  
                """)

                # Approve/Decline buttons
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"Approve {row['Reference ID']}", key=f"approve_{row['Reference ID']}"):
                        data.loc[i, "Status"] = "Approved"
                        write_data(data)  # Save the updated data
                        st.success(f"Request {row['Reference ID']} has been approved.")
                        st.experimental_rerun()

                with col2:
                    if st.button(f"Decline {row['Reference ID']}", key=f"decline_{row['Reference ID']}"):
                        data.loc[i, "Status"] = "Declined"
                        write_data(data)  # Save the updated data
                        st.warning(f"Request {row['Reference ID']} has been declined.")
                        st.experimental_rerun()

        # Debugging: Show updated database
        if st.checkbox("Show database (debugging)"):
            st.dataframe(data)

