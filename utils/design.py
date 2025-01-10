import streamlit as st

def apply_design():
    """
    Apply custom design and styling for the Streamlit app.
    """
    # Add custom CSS styles for app design
    st.markdown("""
        <style>
            /* General App Styling */
            .app-header {
                display: none; /* Hides the global header */
            }

            /* Background for the sidebar */
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
