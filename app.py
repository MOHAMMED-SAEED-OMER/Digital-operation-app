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

    # Initialize session state for page navigation
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Welcome"  # Default page

    # Sidebar navigation
    st.sidebar.markdown("<div class='sidebar-title'>Navigation</div>", unsafe_allow_html=True)
    pages = {
        "🏠 Welcome": "Welcome",
        "📝 Request Form": "Request Form",
        "📂 Database": "Database",
        "🕵️ Manager's View": "Manager's View",
        "💵 Issue Funds": "Issue Funds",
        "✅ Liquidation": "Liquidation",
        "✏️ Edit Page": "Edit Page",
    }

    # Navigation through sidebar buttons
    for label, page in pages.items():
        if st.sidebar.button(label, key=page):
            st.session_state["current_page"] = page

    # Navigate to the selected page
    current_page = st.session_state["current_page"]
    if current_page == "Welcome":
        st.markdown("<h1 class='center-text'>Welcome to the E-Operation App</h1>", unsafe_allow_html=True)
        welcome_page()
    elif current_page == "Request Form":
        st.markdown("<h1 class='center-text'>Submit a New Request</h1>", unsafe_allow_html=True)
        request_form_page()
    elif current_page == "Database":
        st.markdown("<h1 class='center-text'>View Database</h1>", unsafe_allow_html=True)
        database_page()
    elif current_page == "Manager's View":
        st.markdown("<h1 class='center-text'>Manager's Approval</h1>", unsafe_allow_html=True)
        managers_view_page()
    elif current_page == "Issue Funds":
        st.markdown("<h1 class='center-text'>Issue Funds</h1>", unsafe_allow_html=True)
        issue_funds_page()
    elif current_page == "Liquidation":
        st.markdown("<h1 class='center-text'>Process Liquidation</h1>", unsafe_allow_html=True)
        liquidation_page()
    elif current_page == "Edit Page":
        st.markdown("<h1 class='center-text'>Edit Database</h1>", unsafe_allow_html=True)
        edit_page()

if __name__ == "__main__":
    main()
