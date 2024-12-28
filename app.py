from app_pages.welcome_page import welcome_page
from app_pages.request_form import request_form_page
from app_pages.database_page import database_page
from utils.database import initialize_database


def main():
    # Initialize the database
    initialize_database()

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Welcome", "Request Form", "Database"])

    # Navigate to the selected page
    if page == "Welcome":
        welcome_page()
    elif page == "Request Form":
        request_form_page()
    elif page == "Database":
        database_page()

if __name__ == "__main__":
    main()
