import pandas as pd
import streamlit as st
from datetime import datetime
from utils.database import read_data, update_liquidation_details

def liquidation_page():
    st.title("Liquidation")
    st.subheader("Process Liquidation for Issued Requests")

    # Load data
    data = read_data()

    # Ensure "Finance Status" column is string type
    if "Finance Status" in data.columns:
        data["Finance Status"] = data["Finance Status"].astype(str)  # Convert to strings if needed

    # Filter issued requests that have not been liquidated
    pending_liquidation_requests = data[
        (data["Finance Status"].str.strip().str.lower() == "issued") &
        (pd.isna(data["Liquidated"]) | (data["Liquidated"] == 0))
    ]

    if pending_liquidation_requests.empty:
        st.info("No pending liquidation requests.")
    else:
        for i, row in pending_liquidation_requests.iterrows():
            st.write(f"### Request ID: {row['Reference ID']}")
            st.write(f"- **Requester Name**: {row['Requester Name']}")
            st.write(f"- **Request Purpose**: {row['Request Purpose']}")
            st.write(f"- **Amount Issued**: ${row['Amount Requested']:.2f}")
            st.write(f"- **Issue Date**: {row['Issue Date']}")

            # Create a unique key for each button
            if st.button(f"Liquidate Request {row['Reference ID']}", key=f"liquidate_{row['Reference ID']}"):
                st.session_state["liquidation_reference_id"] = row["Reference ID"]

        # Check if a request is being liquidated
        if "liquidation_reference_id" in st.session_state:
            reference_id = st.session_state["liquidation_reference_id"]
            st.write(f"### Processing Liquidation for Request ID: {reference_id}")

            # Get the corresponding request row
            request_row = data[data["Reference ID"] == reference_id].iloc[0]

            with st.form(f"Liquidation Form {reference_id}"):
                liquidated = st.number_input(
                    "Amount Liquidated", min_value=0.0, max_value=request_row["Amount Requested"], format="%.2f"
                )
                returned = st.number_input(
                    "Amount Returned", min_value=0.0, max_value=request_row["Amount Requested"], format="%.2f"
                )
                invoices = st.text_area("Attach Invoice Links (comma-separated)")

                # Add a submit button inside the form
                submit = st.form_submit_button("Submit Liquidation")

                # Validate and process the form submission
                if submit:
                    if liquidated + returned > request_row["Amount Requested"]:
                        st.error("The total of liquidated and returned amounts exceeds the issued amount.")
                    else:
                        update_liquidation_details(
                            reference_id=reference_id,
                            liquidated=liquidated,
                            returned=returned,
                            invoices=invoices
                        )
                        st.success(f"Liquidation details for Request ID {reference_id} updated successfully.")

                        # Clear the session state and trigger a refresh
                        del st.session_state["liquidation_reference_id"]
                        st.session_state["refresh_key"] = st.session_state.get("refresh_key", 0) + 1
                        st.experimental_set_query_params(refresh_key=st.session_state["refresh_key"])
