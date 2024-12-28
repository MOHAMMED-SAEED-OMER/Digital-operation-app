import streamlit as st
import pandas as pd
import os

# Path to the database file
DATABASE_FILE = "database.csv"

# Initialize the database
if not os.path.exists(DATABASE_FILE):
    df = pd.DataFrame(columns=["Requester Name", "Purpose", "Amount Requested", "Submission Date"])
    df.to_csv(DATABASE_FILE, index=False)

# Load the database
def load_database():
    return pd.read_csv(DATABASE_FILE)

# Save the request to the database
def save_request(requester_name, purpose, amount_requested, submission_date):
    df = load_database()
    new_row = {
        "Requester Name": requester_name,
        "Purpose": purpose,
        "Amount Requested": amount_requested,
        "Submission Date": submission_date,
    }
    df = df.append(new_row, ignore_index=True)
    df.to_csv(DATABASE_FILE, index=False)

# Streamlit app layout
def main():
    st.title("E-Operation Request System")

    # Sidebar menu
    menu = ["Welcome", "Request Form", "Database"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Welcome":
        st.header("Welcome to the E-Operation Request System!")
        st.write("Navigate through the pages using the sidebar.")
        st.image("https://via.placeholder.com/600x300", caption="E-Operation System")

    elif choice == "Request Form":
        st.header("Submit a New Request")
        requester_name = st.text_input("Requester Name")
        purpose = st.text_area("Purpose of Request")
        amount_requested = st.number_input("Amount Requested", min_value=0.0, step=0.01)
        submission_date = st.date_input("Submission Date")

        if st.button("Submit"):
            if requester_name and purpose and amount_requested > 0:
                save_request(requester_name, purpose, amount_requested, submission_date)
                st.success("Request submitted successfully!")
            else:
                st.warning("Please fill out all fields correctly.")

    elif choice == "Database":
        st.header("View All Submitted Requests")
        df = load_database()
        st.dataframe(df)

if __name__ == "__main__":
    main()
