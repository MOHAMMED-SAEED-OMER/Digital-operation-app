import streamlit as st

def apply_design():
    """
    Apply custom design and styling for the Streamlit app.
    """
    st.markdown("""
        <style>
            /* General App Styling */
            .app-header {
                display: none; /* Hides the global header */
            }

            /* Sidebar styling */
            .css-1d391kg {
                background-color: #f7f9fc;
            }

            /* Sidebar title styling */
            .sidebar-title {
                color: #333;
                font-size: 22px;
                text-align: center;
                margin-bottom: 20px;
            }

            /* Button styles */
            .menu-button {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                margin: 5px 0;
            }

            .menu-button:hover {
                background-color: #0056b3;
            }

            /* Centered text */
            .center-text {
                text-align: center;
                font-family: Arial, sans-serif;
                color: #555;
            }
        </style>
    """, unsafe_allow_html=True)
def enhanced_navigation_bar():
    """
    Create an enhanced navigation bar with added functionality and better UI.
    """
    # Sidebar Title
    st.sidebar.markdown("<h2 class='sidebar-title'>Navigation</h2>", unsafe_allow_html=True)

    # Welcome Message with Role
    user_name = st.session_state['user_info']['name'].capitalize()
    user_role = st.session_state['user_info'].get('role', 'Member').capitalize()
    st.sidebar.markdown(f"""
        <p style="text-align: center; font-size: 18px;">Welcome, <strong>{user_name}</strong>!</p>
        <p style="text-align: center; color: #555;">Role: <strong>{user_role}</strong></p>
    """, unsafe_allow_html=True)

    # Description for Hasar Organization
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.markdown("""
        <h3 style='text-align: center;'>Hasar Organization</h3>
        <p style='text-align: center; color: #555;'>For Climate Action and Sustainability</p>
    """, unsafe_allow_html=True)

    # Useful Links
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.markdown("<h3 style='text-align: center;'>Quick Links</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("""
        <ul style="list-style-type: none; padding-left: 0;">
            <li><a href="https://hasar.org/" target="_blank" style="text-decoration: none;">🌐 Visit Our Website</a></li>
            <li><a href="https://www.facebook.com/Hasar.org" target="_blank" style="text-decoration: none;">📘 Facebook</a></li>
            <li><a href="https://www.instagram.com/hasarorganization/" target="_blank" style="text-decoration: none;">📸 Instagram</a></li>
        </ul>
    """, unsafe_allow_html=True)

    # Contact Support
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.markdown("<h3 style='text-align: center;'>Contact Us</h3>", unsafe_allow_html=True)
    st.sidebar.markdown(f"""
        <div class="center-text">
            📧 Email: <a href="mailto:mohammed.saeed@hasariraq.onmicrosoft.com">m.saeed@hasariraq.com</a><br>
            📞 Phone: +9647507810474
        </div>
    """, unsafe_allow_html=True)

    # Logout Button
    if st.sidebar.button("Log Out", key="logout", help="Log out of the application"):
        st.session_state["user_info"] = None
        st.experimental_rerun()

    # Footer
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.markdown("""
        <div class="center-text" style="font-size: 12px;">
            &copy; 2025 Hasar Organization. All rights reserved.
        </div>
    """, unsafe_allow_html=True)
