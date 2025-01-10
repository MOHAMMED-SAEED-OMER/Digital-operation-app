import streamlit as st
from utils.database import read_data

def database_page():
    st.title("Database")
    st.subheader("View All Requests")

    # Read and display the database
    data = read_data()
    if not data.empty:
        st.dataframe(data)
    else:
        st.warning("No requests found. Submit a request to populate the database.")
