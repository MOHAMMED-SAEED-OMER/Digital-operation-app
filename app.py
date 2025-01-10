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
        # Logged-in user interface
        st.sidebar.title("Navigation")
        st.sidebar.markdown(f"Welcome, **{st.session_state['user_info']['name']}**!")

        # Logout button
        if st.sidebar.button("Log Out"):
            st.session_state["user_info"] = None
            if hasattr(st, "set_query_params"):
                st.set_query_params(refresh=True)
            else:
                st.experimental_set_query_params(refresh=True)
            st.stop()

        # Tab-based navigation
        allowed_pages = st.session_state["user_info"]["allowed_pages"]
        tabs = st.tabs(allowed_pages)

        for i, tab in enumerate(tabs):
            with tab:
                page = allowed_pages[i]
                if page == "Welcome":
                    st.markdown("<h1>Welcome</h1>", unsafe_allow_html=True)
                    welcome_page()
                elif page == "Request Form":
                    st.markdown("<h1>Submit a New Request</h1>", unsafe_allow_html=True)
                    request_form_page()
                elif page == "Database":
                    st.markdown("<h1>Database</h1>", unsafe_allow_html=True)
                    database_page()
                elif page == "Manager's View":
                    st.markdown("<h1>Manager's View</h1>", unsafe_allow_html=True)
                    managers_view_page()
                elif page == "Issue Funds":
                    st.markdown("<h1>Issue Funds</h1>", unsafe_allow_html=True)
                    issue_funds_page()
                elif page == "Liquidation":
                    st.markdown("<h1>Liquidation</h1>", unsafe_allow_html=True)
                    liquidation_page()
                elif page == "Edit Page":
                    st.markdown("<h1>Edit Database</h1>", unsafe_allow_html=True)
                    edit_page()

if __name__ == "__main__":
    main()
