import streamlit as st
import pandas as pd

USER_PROFILES_FILE = "user_profiles.csv"  # Path to the user profiles CSV file

def login_page():
    st.title("Login")
    st.subheader("Enter your credentials to access the app")

    # Load user profiles
    if not USER_PROFILES_FILE:
        st.error("User profiles database not found!")
        return

    user_profiles = pd.read_csv(USER_PROFILES_FILE)

    # Login form
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

    if login_button:
        # Authenticate user
        user = user_profiles[
            (user_profiles["Email"] == email) & (user_profiles["Password"] == password)
        ]

        if not user.empty:
            user_info = {
                "name": user.iloc[0]["Name"],
                "role": user.iloc[0]["Role"],
                "allowed_pages": user.iloc[0]["Allowed Pages"].split(","),
            }
            st.session_state["user_info"] = user_info
            st.success(f"Welcome {user_info['name']}! Redirecting to the app...")
            st.experimental_rerun()
        else:
            st.error("Invalid email or password. Please try again.")
