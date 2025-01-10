import streamlit as st
import pandas as pd

def login_page():
    st.title("Login")

    # Load user profiles
    user_profiles = pd.read_csv("user_profiles.csv")

    # Input fields for login
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Validate user credentials
        user = user_profiles[
            (user_profiles["Email"] == email) & (user_profiles["Password"] == password)
        ]
        if not user.empty:
            # Login successful
            st.session_state["user_info"] = {
                "name": user.iloc[0]["Name"],
                "role": user.iloc[0]["Role"],
                "allowed_pages": user.iloc[0]["Allowed Pages"].split(","),
            }
            # Update query parameters to refresh the page
            if hasattr(st, "set_query_params"):
                st.set_query_params()  # Use the updated method
            else:
                st.experimental_set_query_params()  # Fallback for older versions
            st.experimental_rerun()
        else:
            st.error("Invalid email or password. Please try again.")
