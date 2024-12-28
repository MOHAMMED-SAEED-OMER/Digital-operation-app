import streamlit as st
import pandas as pd
import os

# Constants
DATABASE_FILE = "database.csv"

def load_data():
    if not os.path.exists(DATABASE_FILE):
        # Create the CSV file with headers if it doesn't exist
        with open(DATABASE_FILE, "w") as file:
            file.write("Requester Name,Purpose,Amount Requested,Submission Date\n")
    return pd.read_csv(DATABASE_FILE)

def save_data(data):
    data.to_csv(DATABASE_FILE, index=False)

def welcome_page():
    st.title("Welcome to the E-operation App")
    st.write("This application allows you to manage requests and track their details.")

def request_form_page():
    st.title("Submit a New Request")

    with st.form("request_form"):
        requester_name = st.text_input("Requester Name")
        purpose = st.text_area("Purpose of Request")
        amount_requested = st.number_input("Amount Requested", min_value=0.0, format="%.2f")
        submission_date = st.date_input("Submission Date")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if requester_name and purpose and amount_requested > 0:
                new_request = pd.DataFrame({
                    "Requester Name": [requester_name],
                    "Purpose": [purpose],
                    "Amount Requested": [amount_requested],
                    "Submission Date": [submission_date]
                })
                data = load_data()
                data = pd.concat([data, new_request], ignore_index=True)
                save_data(data)
                st.success("Request submitted successfully!")
            else:
                st.error("Please fill in all fields correctly.")

def database_page():
    st.title("Database of Requests")
    data = load_data()

    if data.empty:
        st.write("No requests have been submitted yet.")
    else:
        st.dataframe(data)
        st.download_button(
            label="Download CSV",
            data=data.to_csv(index=False),
            file_name="database.csv",
            mime="text/csv"
        )

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Welcome", "Request Form", "Database"])

    if page == "Welcome":
        welcome_page()
    elif page == "Request Form":
        request_form_page()
    elif page == "Database":
        database_page()

if __name__ == "__main__":
    main()
