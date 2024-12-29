from app_pages.finance_page import finance_page

def main():
    initialize_database()

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["Welcome", "Request Form", "Database", "Manager's View", "Finance Page"]
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
