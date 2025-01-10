import streamlit as st
import pandas as pd

def login_page():
    """
    Login page for the application.
    """
    # Apply a custom header with the organization logo and title
    st.markdown("""
        <style>
            .login-container {
                text-align: center;
                margin-top: 50px;
            }
            .login-header {
                font-size: 32px;
                font-weight: bold;
                color: #0056b3;
                margin-top: 20px;
                margin-bottom: 10px;
            }
            .login-subtitle {
                font-size: 18px;
                color: #444444;
                margin-bottom: 30px;
            }
            .contact-info {
                text-align: center;
                font-size: 14px;
                color: #666666;
                margin-top: 30px;
            }
            .contact-info a {
                color: #0056b3;
                text-decoration: none;
            }
            .contact-info a:hover {
                text-decoration: underline;
            }
        </style>
    """, unsafe_allow_html=True)

    # Add the logo and titles
    st.markdown("""
        <div class="login-container">
            <img src="logo.png" alt="Organization Logo" style="max-width: 200px; height: auto;">
            <div class="login-header">Hasar Organization for Climate Action</div>
            <div class="login-subtitle">Electronic Financing and Procurement System</div>
        </div>
    """, unsafe_allow_html=True)

    # Login form
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Load user profiles
        user_profiles = pd.read_csv("user_profiles.csv")

        # Validate credentials
        user = user_profiles[(user_profiles["Email"] == email) & (user_profiles["Password"] == password)]
        if not user.empty:
            st.session_state["user_info"] = {
                "name": user.iloc[0]["Name"],
                "role": user.iloc[0]["Role"],
                "allowed_pages": user.iloc[0]["Allowed Pages"].split(",")
            }
            st.success("Login successful! Redirecting...")
            st.experimental_rerun()
        else:
            st.error("Invalid email or password. Please try again.")

    # Add contact information
    st.markdown("""
        <div class="contact-info">
            <p>Website: <a href="https://www.hasar.org" target="_blank">www.hasar.org</a></p>
            <p>Address: 123 Climate Action Street, Erbil, Kurdistan Region, Iraq</p>
            <p>Phone: +964-750-123-4567</p>
        </div>
    """, unsafe_allow_html=True)
