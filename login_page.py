import streamlit as st
import pandas as pd

def login_page():
    """
    Login page for the application.
    """
    # Apply custom styles for the login page
    st.markdown("""
        <style>
            .login-container {
                text-align: center;
                margin-top: 30px;
            }
            .login-header {
                font-size: 32px;
                font-weight: bold;
                color: #0056b3;
                margin-top: 10px;
                margin-bottom: 5px;
            }
            .login-subtitle {
                font-size: 18px;
                color: #444444;
                margin-bottom: 20px;
            }
            .contact-info {
                text-align: center;
                font-size: 14px;
                color: #666666;
                margin-top: 20px;
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

    # Add the image using Streamlit's st.image()
    image_path = "Cover-photo.png"  # Ensure the image file is in the same directory or update the path
    st.image(image_path, use_column_width=True)

    # Add titles
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
