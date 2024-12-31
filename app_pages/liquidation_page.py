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
                # Input the liquidated amount
                liquidated = st.number_input(
                    "Amount Liquidated", min_value=0.0, value=0.0, format="%.2f"
                )
                
                # Calculate returned amount dynamically
                returned = request_row["Amount Requested"] - liquidated

                # Display the dynamically calculated returned amount
                st.write(f"Calculated Amount Returned: ${returned:.2f}")

                # Input for attaching invoice links
                invoices = st.text_area("Attach Invoice Links (comma-separated)")

                # Submit button inside the form
                submit = st.form_submit_button("Submit Liquidation")

                # Validate and process the form submission
                if submit:
                    # Update liquidation details
                    update_liquidation_details(
                        reference_id=reference_id,
                        liquidated=liquidated,
                        returned=returned,
                        invoices=invoices
                    )
                    st.success(f"Liquidation details for Request ID {reference_id} updated successfully.")

                    # Clear the session state
                    del st.session_state["liquidation_reference_id"]

                    # Trigger a page refresh
                    st.session_state["refresh_trigger"] = st.session_state.get("refresh_trigger", 0) + 1
                    st.stop()  # Stop the script to trigger a rerun
