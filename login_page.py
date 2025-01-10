import streamlit as st
import pandas as pd

def login_page():
    """
    Login page for the application with a dynamic background and organization details.
    """
    # Apply custom styles for the login page
    st.markdown("""
        <style>
            body {
                background: linear-gradient(135deg, #f3f4f6, #e0e7ff);
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
            }
            .login-container {
                text-align: center;
                margin-top: 80px;
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
                margin-bottom: 40px;
            }
            .contact-info {
                text-align: center;
                font-size: 14px;
                color: #666666;
                margin-top: 40px;
            }
            .contact-info a {
                color: #0056b3;
                text-decoration: none;
            }
            .contact-info a:hover {
                text-decoration: underline;
            }
            .logo-container {
                position: absolute;
                top: 20px;
                right: 20px;
            }
            .logo-container img {
                width: 150px;
                height: auto;
            }
            .background {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-image: url('background-image.png'); /* Use your dynamic image */
                background-size: cover;
                background-position: center;
                z-index: -1;
            }
            .overlay {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(255, 255, 255, 0.8); /* Light overlay for text readability */
                z-index: -1;
            }
        </style>
    """, unsafe_allow_html=True)

    # Add background image and overlay
    st.markdown("""
        <div class="background"></div>
        <div class="overlay"></div>
    """, unsafe_allow_html=True)

    # Add the logo at the top-right
    st.markdown("""
        <div class="logo-container">
            <img src="Hasar Official Approved Logo in 2023-2.png" alt="Hasar Logo">
        </div>
    """, unsafe_allow_html=True)

    # Add the main title and subtitle
    st.markdown("""
        <div class="login-container">
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
    st.markdown(f"""
        <div class="contact-info">
            <p>Website: <a href="https://www.hasar.org" target="_blank">www.hasar.org</a></p>
            <p>Address: Iraq, Erbil, 120m Street</p>
            <p>Phone: +9647807810474</p>
        </div>
    """, unsafe_allow_html=True)
