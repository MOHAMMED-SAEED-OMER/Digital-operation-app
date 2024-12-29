import streamlit as st
from datetime import datetime
from utils.database import read_data, update_finance_status, update_liquidation_details

def finance_page():
    st.title("Finance Page")
    st.subheader("Process Approved Requests")

    # Load data
    data = read_data()

    # Filter issued requests
    issued_requests = data[(data["Finance Status"] == "Issued")]

    if issued_requests.empty:
        st.info("No issued requests to process.")
    else:
        for i, row in issued_requests.iterrows():
            st.write(f"### Request ID: {row['Reference ID']}")
            st.write(f"- **Requester Name**: {row['Requester Name']}")
            st.write(f"- **Request Purpose**: {row['Request Purpose']}")
            st.write(f"- **Amount Issued**: ${row['Amount Requested']:.2f}")
            st.write(f"- **Issue Date**: {row['Issue Date']}")

            # Add a "Liquidation" button
            if st.button(f"Liquidate Request {row['Reference ID']}"):
                with st.form(f"Liquidation Form {row['Reference ID']}"):
                    liquidated = st.number_input("Amount Liquidated", min_value=0.0, max_value=row['Amount Requested'], format="%.2f")
                    returned = st.number_input("Amount Returned", min_value=0.0, max_value=row['Amount Requested'], format="%.2f")
                    invoices = st.text_input("Attach Invoice Links (comma-separated)")

                    # Validate liquidation and returned amounts
                    if liquidated + returned > row['Amount Requested']:
                        st.error("The total of liquidated and returned amounts exceeds the issued amount.")
                    else:
                        if st.form_submit_button("Submit Liquidation"):
                            update_liquidation_details(
                                reference_id=row["Reference ID"],
                                liquidated=liquidated,
                                returned=returned,
                                invoices=invoices
                            )
                            st.success(f"Liquidation details for Request ID {row['Reference ID']} updated successfully.")
                            st.experimental_rerun()  # Refresh the page
