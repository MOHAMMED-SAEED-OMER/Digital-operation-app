import streamlit as st

def apply_design():
    """
    Apply custom design and styling for the Streamlit app.
    """
    # Add custom CSS styles
    st.markdown("""
        <style>
            /* General background */
            .css-1v3fvcr {
                background-color: #f0f2f6;
            }

            /* Sidebar */
            .sidebar .sidebar-content {
                background-color: #4CAF50;
                color: white;
            }

            /* Buttons */
            .stButton > button {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                border: none;
                padding: 10px;
                font-size: 16px;
            }
            .stButton > button:hover {
                background-color: #45a049;
            }

            /* Centered text */
            .center-text {
                text-align: center;
                font-family: 'Arial', sans-serif;
                color: #333;
            }
        </style>
    """, unsafe_allow_html=True)

    # Add any global markdown or design-specific headers
    st.markdown("<h1 class='center-text'>Welcome to the E-Operation App</h1>", unsafe_allow_html=True)
    st.markdown("<p class='center-text'>Streamline your operational processes efficiently.</p>", unsafe_allow_html=True)
