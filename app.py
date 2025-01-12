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
from utils.design import apply_design  # If design customization exists

def enhanced_navigation_bar():
    """
    Create an enhanced navigation bar with added functionality and better UI.
    """
    # Sidebar Title
    st.sidebar.markdown("<h2 class='sidebar-title'>Navigation</h2>", unsafe_allow_html=True)

    # Welcome Message
    user_name = st.session_state['user_info']['name'].capitalize()
    st.sidebar.markdown(f"Welcome, **{user_name}**!", unsafe_allow_html=True)

    # Useful Links
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.markdown("<h3 style='text-align: center;'>Quick Links</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("""
        <ul style="list-style-type: none; padding-left: 0;">
            <li><a href="https://www.google.com" target="_blank" style="text-decoration: none;">Google</a></li>
            <li><a href="https://www.streamlit.io" target="_blank" style="text-decoration: none;">Streamlit Docs</a></li>
            <li><a href="https://github.com" target="_blank" style="text-decoration: none;">GitHub</a></li>
        </ul>
    """, unsafe_allow_html=True)

    # Logout Button
    if st.sidebar.button("Log Out", key="logout", help="Log out of the application"):
        st.session_state["user_info"] = None
        st.experimental_rerun()

    # Add more functionality
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.markdown("<h3 style='text-align: center;'>Contact Us</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("""
        <div class="center-text">
            📧 Email: <a href="mailto:support@yourapp.com">support@yourapp.com</a><br>
            📞 Phone: +1-234-567-890
        </div>
    """, unsafe_allow_html=True)

    # Footer
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.markdown("""
        <div class="center-text" style="font-size: 12px;">
            &copy; 2025 Your Company. All rights reserved.
        </div>
    """, unsafe_allow_html=True)

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
