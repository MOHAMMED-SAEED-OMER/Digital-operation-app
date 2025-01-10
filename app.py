import streamlit as st
from app_pages.welcome_page import welcome_page
from app_pages.request_form import request_form_page
from app_pages.database_page import database_page
from app_pages.managers_view import managers_view_page
from app_pages.issue_funds_page import issue_funds_page
from app_pages.liquidation_page import liquidation_page
from app_pages.edit_page import edit_page
from utils.database import initialize_database
from login_page import login_page

def main():
    # Initialize the database (create if not exists)
    initialize_database()

    # Check if the user is logged in
    if "user_info" not in st.session_state:
        login_page()
        return

    user_info = st.session_state["user_info"]
    allowed_pages = user_info["allowed_pages"]

    # Sidebar navigation
    st.sidebar.title(f"Welcome, {user_info['name']}!")
    page = st.sidebar.radio(
        "Go to",
        options=allowed_pages,
    )

    # Map pages to their respective functions
    page_map = {
        "Welcome": welcome_page,
        "Request Form": request_form_page,
        "Database": database_page,
        "Manager's View": managers_view_page,
        "Issue Funds": issue_funds_page,
        "Liquidation": liquidation_page,
        "Edit Page": edit_page,
    }

    # Navigate to the selected page
    if page in page_map:
        page_map[page]()

    # Add a logout button
    if st.sidebar.button("Logout"):
        del st.session_state["user_info"]
        st.experimental_rerun()

if __name__ == "__main__":
    main()
