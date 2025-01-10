import streamlit as st
import pandas as pd

# Load user profiles
USER_PROFILES_FILE = "user_profiles.csv"

def load_user_profiles():
    """
    Load user profiles from the CSV file.
    """
    return pd.read_csv(USER_PROFILES_FILE)

def login_page():
    """
    Login page for the application.
    """
    st.title("Login")
    st.subheader("Enter your credentials")

    # Login form
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

    if submit_button:
        # Validate user credentials
        user_profiles = load_user_profiles()
        user = user_profiles[
            (user_profiles["Email"] == email) & 
            (user_profiles["Password"] == password)
        ]

        if not user.empty:
            user_info = {
                "user_id": user.iloc[0]["User ID"],
                "name": user.iloc[0]["Name"],
                "role": user.iloc[0]["Role"],
                "allowed_pages": user.iloc[0]["Allowed Pages"].split(","),
            }

            # Store user info in session state
            st.session_state["user_info"] = user_info

            # Trigger a rerun by updating session state
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid email or password. Please try again.")

    # Rerun if the user has successfully logged in
    if st.session_state.get("logged_in"):
        st.session_state["logged_in"] = False  # Reset trigger
        st.experimental_set_query_params()  # Mimic a rerun behavior
