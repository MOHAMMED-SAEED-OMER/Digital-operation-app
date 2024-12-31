import streamlit as st
from app_pages.welcome_page import welcome_page
from app_pages.request_form import request_form_page
from app_pages.database_page import database_page
from app_pages.managers_view import managers_view_page
from app_pages.issue_funds_page import issue_funds_page
from app_pages.liquidation_page import liquidation_page
from app_pages.edit_page import edit_page
from utils.database import initialize_database
from utils.design import apply_design

def main():
    # Apply design settings
    apply_design()

    # Initialize the database (create if not exists)
    initialize_database()

    # Sidebar navigation
    st.sidebar.markdown("<div class='sidebar-title'>Navigation</div>", unsafe_allow_html=True)
    page = "Welcome"  # Default page

    # Sidebar menu buttons
    if st.sidebar.button("🏠 Welcome"):
        page = "Welcome"
    if st.sidebar.button("📝 Request Form"):
        page = "Request Form"
    if st.sidebar.button("📂 Database"):
        page = "Database"
    if st.sidebar.button("🕵️ Manager's View"):
        page = "Manager's View"
    if st.sidebar.button("💵 Issue Funds"):
        page = "Issue Funds"
    if st.sidebar.button("✅ Liquidation"):
        page = "Liquidation"
    if st.sidebar.button("✏️ Edit Page"):
        page = "Edit Page"

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

if __name__ == "__main__":
    main()
