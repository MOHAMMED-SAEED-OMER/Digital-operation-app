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
        st.markdown("<h1 class='center-text'>Welcome to the E-Operation App</h1>", unsafe_allow_html=True)
        welcome_page()
    elif page == "Request Form":
        st.markdown("<h1 class='center-text'>Submit a New Request</h1>", unsafe_allow_html=True)
        request_form_page()
    elif page == "Database":
        st.markdown("<h1 class='center-text'>View Database</h1>", unsafe_allow_html=True)
        database_page()
    elif page == "Manager's View":
        st.markdown("<h1 class='center-text'>Manager's Approval</h1>", unsafe_allow_html=True)
        managers_view_page()
    elif page == "Issue Funds":
        st.markdown("<h1 class='center-text'>Issue Funds</h1>", unsafe_allow_html=True)
        issue_funds_page()
    elif page == "Liquidation":
        st.markdown("<h1 class='center-text'>Process Liquidation</h1>", unsafe_allow_html=True)
        liquidation_page()
    elif page == "Edit Page":
        st.markdown("<h1 class='center-text'>Edit Database</h1>", unsafe_allow_html=True)
        edit_page()

if __name__ == "__main__":
    main()
