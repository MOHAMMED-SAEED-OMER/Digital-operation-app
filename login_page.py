import streamlit as st
import pandas as pd

def login_page():
    """
    Login page for the application with enhanced visuals.
    """
    # Apply custom styles for the login page
    st.markdown("""
        <style>
            body {
                background-color: #f7f7f7;
                font-family: Arial, sans-serif;
            }
            .login-container {
                text-align: center;
                margin-top: 50px;
            }
            .login-header {
                font-size: 36px;
                font-weight: bold;
                color: #0056b3;
                margin-top: 20px;
                margin-bottom: 10px;
            }
            .login-subtitle {
                font-size: 18px;
                color: #666666;
                margin-bottom: 20px;
            }
            .login-form {
                margin: 30px auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 10px;
                max-width: 400px;
                background-color: #ffffff;
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
            }
            .login-button {
                background-color: #0056b3;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                margin-top: 10px;
            }
            .login-button:hover {
                background-color: #004494;
            }
            .contact-info {
                margin-top: 30px;
                font-size: 14px;
                color: #444444;
                text-align: center;
            }
            .contact-info a {
                color: #0056b3;
                text-decoration: none;
            }
            .contact-info a:hover {
                text-decoration: underline;
            }
            .logo-container {
                text-align: right;
                margin-top: -50px;
                margin-right: 10px;
                position: relative;
            }
            .logo-container img {
                width: 120px; /* Adjust logo size */
                height: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    # Display the logo at the top-right
    st.markdown("""
        <div class="logo-container">
            <img src="Hasar Official Approved Logo in 2023-2.png" alt="Hasar Logo">
        </div>
    """, unsafe_allow_html=True)

    # Main title and subtitle
    st.markdown("""
        <div class="login-container">
            <div class="login-header">Hasar Organization for Climate Action</div>
            <div class="login-subtitle">Electronic Financing and Procurement System</div>
        </div>
    """, unsafe_allow_html=True)

    # Login form
    st.markdown("""
        <div class="login-form">
            <h3>Login</h3>
    """, unsafe_allow_html=True)
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login", key="login_button"):
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

    st.markdown("</div>", unsafe_allow_html=True)  # Close login-form

    # Contact information
    st.markdown(f"""
        <div class="contact-info">
            <p><strong>Website:</strong> <a href="https://www.hasar.org" target="_blank">www.hasar.org</a></p>
            <p><strong>Address:</strong> Iraq, Erbil, 120m Street</p>
            <p><strong>Phone:</strong> +9647807810474</p>
        </div>
    """, unsafe_allow_html=True)
