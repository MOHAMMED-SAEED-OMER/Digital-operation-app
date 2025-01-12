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
from utils.design import apply_design, enhanced_navigation_bar

def main():
    # Apply custom design (optional)
    apply_design()

    # Initialize the database (create if not exists)
    initialize_database()

    # Check if user is logged in
    if "user_info" not in st.session_state:
        st.session_state["user_info"] = None

    if st.session_state["user_info"] is None:
        login_page()
    else:
        # Enhanced navigation bar
        enhanced_navigation_bar()

        # Tab-based navigation
        allowed_pages = st.session_state["user_info"]["allowed_pages"]
        tabs = st.tabs(allowed_pages)

        for i, tab in enumerate(tabs):
            with tab:
                page = allowed_pages[i]
                if page == "Welcome":
                    welcome_page()  # Use the title defined in `welcome_page.py`
                elif page == "Request Form":
                    request_form_page()  # Use the title defined in `request_form.py`
                elif page == "Database":
                    database_page()  # Use the title defined in `database_page.py`
                elif page == "Manager's View":
                    managers_view_page()  # Use the title defined in `managers_view.py`
                elif page == "Issue Funds":
                    issue_funds_page()  # Use the title defined in `issue_funds_page.py`
                elif page == "Liquidation":
                    liquidation_page()  # Use the title defined in `liquidation_page.py`
                elif page == "Edit Page":
                    edit_page()  # Use the title defined in `edit_page.py`

if __name__ == "__main__":
    main()
