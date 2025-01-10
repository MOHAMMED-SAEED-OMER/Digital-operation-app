import streamlit as st
import pandas as pd

def login_page():
    """
    Login page with a stylish background and centralized login form.
    """
    # Apply custom styles for the login page
    st.markdown("""
        <style>
            body {
                background-color: #f7f7f7;
                font-family: Arial, sans-serif;
            }
            .background-container {
                background-image: linear-gradient(to bottom, #0056b3, #78c0e0);
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
            }
            .login-container {
                text-align: center;
                padding: 20px;
                margin: auto;
                margin-top: 100px;
                width: 350px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            }
            .logo-container img {
                width: 80px; /* Adjust logo size */
                height: auto;
                margin-top: -50px;
                margin-bottom: 10px;
            }
            .login-header {
                font-size: 28px;
                font-weight: bold;
                color: #0056b3;
                margin-bottom: 10px;
            }
            .login-subtitle {
                font-size: 14px;
                color: #666666;
                margin-bottom: 20px;
            }
            .contact-info {
                margin-top: 20px;
                font-size: 12px;
                color: #444444;
            }
            .contact-info a {
                color: #0056b3;
                text-decoration: none;
            }
            .contact-info a:hover {
                text-decoration: underline;
            }
            .login-button {
                background-color: #0056b3;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 14px;
            }
            .login-button:hover {
                background-color: #004494;
            }
        </style>
    """, unsafe_allow_html=True)

    # Background container
    st.markdown('<div class="background-container"></div>', unsafe_allow_html=True)

    # Login container
    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    # Logo
    st.markdown("""
        <div class="logo-container">
            <img src="Hasar Official Approved Logo in 2023-2.png" alt="Hasar Logo">
        </div>
    """, unsafe_allow_html=True)

    # Title and subtitle
    st.markdown("""
        <div class="login-header">Hasar Organization</div>
        <div class="login-subtitle">Electronic Financing and Procurement System</div>
    """, unsafe_allow_html=True)

    # Login form
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login", key="login_button", help="Enter your credentials to log in."):
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

    # Contact information
    st.markdown("""
        <div class="contact-info">
            <p><strong>Website:</strong> <a href="https://www.hasar.org" target="_blank">www.hasar.org</a></p>
            <p><strong>Address:</strong> Iraq, Erbil, 120m Street</p>
            <p><strong>Phone:</strong> +9647807810474</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # Close login-container
