import streamlit as st
import pandas as pd
import bcrypt
from utils.database import read_user_profiles

def login_page():
    st.title("Login")

    # User input
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Submit button
    if st.button("Login"):
        # Read user profiles
        user_profiles = read_user_profiles()

        # Validate user
        user = user_profiles[user_profiles["Email"] == email]
        if not user.empty:
            hashed_password = user.iloc[0]["Password"]
            if bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")):
                st.success(f"Welcome, {user.iloc[0]['Name']}!")
                st.session_state["logged_in"] = True
                st.session_state["user"] = {
                    "name": user.iloc[0]["Name"],
                    "role": user.iloc[0]["Role"],
                    "allowed_pages": user.iloc[0]["Allowed Pages"].split(","),
                }
                st.experimental_rerun()  # Refresh page after login
            else:
                st.error("Invalid password.")
        else:
            st.error("Invalid email or user does not exist.")
