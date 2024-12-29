import streamlit as st
from app_pages.welcome_page import welcome_page
from app_pages.request_form import request_form_page
from app_pages.database_page import database_page
from app_pages.managers_view import managers_view_page
from app_pages.finance_page import finance_page
from utils.database import initialize_database

def main():
    # Initialize the database (create if not exists)
    initialize_database()

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        [
            "Welcome",
            "Request Form",
            "Database",
            "Manager's View",
            "Finance Page"
        ]
    )

    # Navigate to the selected page
    if page == "Welcome":
        welcome_page()
    elif page == "Request Form":
        request_form_page()
    elif page == "Database":
        database_page()
    elif page == "Manager's View":
        managers_view_page()
    elif page == "Finance Page":
        finance_page()

if __name__ == "__main__":
    main()
