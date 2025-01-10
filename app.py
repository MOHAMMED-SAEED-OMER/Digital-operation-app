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
from utils.design import apply_design, footer

def main():
    # Apply custom design
    apply_design()

    # Initialize the database (create if not exists)
    initialize_database()

    # Check if user is logged in
    if "user_info" not in st.session_state:
        st.session_state["user_info"] = None

    if st.session_state["user_info"] is None:
        login_page()
    else:
        # Logged-in user interface
        st.sidebar.title("Navigation")
        st.sidebar.markdown(f"Welcome, **{st.session_state['user_info']['name']}**!")
        
        # Logout button
        if st.sidebar.button("Log Out"):
            st.session_state["user_info"] = None
            st.experimental_set_query_params()  # Clear query params
            st.experimental_rerun()

        # Sidebar navigation
        allowed_pages = st.session_state["user_info"]["allowed_pages"]
        page = st.sidebar.radio(
            "Go to",
            allowed_pages
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
        elif page == "Issue Funds":
            issue_funds_page()
        elif page == "Liquidation":
            liquidation_page()
        elif page == "Edit Page":
            edit_page()

    # Add footer to the app
    footer()

if __name__ == "__main__":
    main()
