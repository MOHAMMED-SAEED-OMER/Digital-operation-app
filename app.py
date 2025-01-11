import streamlit as st
from app_pages.welcome_page import welcome_page
from app_pages.request_form import request_form_page
from app_pages.database_page import database_page
from app_pages.managers_view import managers_view_page
from app_pages.issue_funds_page import issue_funds_page
from app_pages.liquidation_page import liquidation_page
from app_pages.edit_page import edit_page
from login_page import login_page
from utils.database import initialize_database

def main():
    # Initialize the database
    initialize_database()

    # Check if user is logged in
    if "user_info" not in st.session_state:
        st.session_state["user_info"] = None

    if st.session_state["user_info"] is None:
        login_page()
    else:
        st.sidebar.title("Navigation")
        st.sidebar.markdown(f"Welcome, **{st.session_state['user_info']['name']}**!")

        # Logout button
        if st.sidebar.button("Log Out"):
            st.session_state["user_info"] = None
            st.experimental_rerun()

        # Tab-based navigation
        pages = {
            "Welcome": welcome_page,
            "Request Form": request_form_page,
            "Database": database_page,
            "Manager's View": managers_view_page,
            "Issue Funds": issue_funds_page,
            "Liquidation": liquidation_page,
            "Edit Page": edit_page,
        }

        selected_page = st.sidebar.radio("Choose a page", list(pages.keys()))
        pages[selected_page]()

if __name__ == "__main__":
    main()
