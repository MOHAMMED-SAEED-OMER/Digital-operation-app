import streamlit as st

def enhanced_navigation_bar():
    """
    Create an enhanced navigation bar with added functionality and better UI.
    """
    # Sidebar Title
    st.sidebar.markdown("<h2 class='sidebar-title'>Navigation</h2>", unsafe_allow_html=True)

    # Welcome Message
    user_name = st.session_state['user_info']['name'].capitalize()
    st.sidebar.markdown(f"Welcome, **{user_name}**!", unsafe_allow_html=True)

    # Useful Links
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.markdown("<h3 style='text-align: center;'>Quick Links</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("""
        <ul style="list-style-type: none; padding-left: 0;">
            <li><a href="https://www.google.com" target="_blank" style="text-decoration: none;">Google</a></li>
            <li><a href="https://www.streamlit.io" target="_blank" style="text-decoration: none;">Streamlit Docs</a></li>
            <li><a href="https://github.com" target="_blank" style="text-decoration: none;">GitHub</a></li>
        </ul>
    """, unsafe_allow_html=True)

    # Logout Button
    if st.sidebar.button("Log Out", key="logout", help="Log out of the application"):
        st.session_state["user_info"] = None
        st.experimental_rerun()

    # Add more functionality
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.markdown("<h3 style='text-align: center;'>Contact Us</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("""
        <div class="center-text">
            📧 Email: <a href="mailto:support@yourapp.com">support@yourapp.com</a><br>
            📞 Phone: +1-234-567-890
        </div>
    """, unsafe_allow_html=True)

    # Footer
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    st.sidebar.markdown("""
        <div class="center-text" style="font-size: 12px;">
            &copy; 2025 Your Company. All rights reserved.
        </div>
    """, unsafe_allow_html=True)
