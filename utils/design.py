import streamlit as st

def apply_design():
    """
    Apply custom design and styling for the Streamlit app.
    """
    # Add custom CSS styles for sidebar and general app design
    st.markdown("""
        <style>
            /* General background */
            .css-1v3fvcr {
                background-color: #f0f2f6;
            }

            /* Sidebar customization */
            .css-1d391kg {
                background-color: #4CAF50;
                padding: 10px;
            }
            .css-1d391kg .css-qbe2hs {
                color: white;
            }
            .css-1d391kg .css-hxt7ib {
                color: white;
                font-size: 18px;
            }
            .sidebar-title {
                color: white;
                font-size: 24px;
                text-align: center;
                font-family: Arial, sans-serif;
                margin-bottom: 20px;
            }

            /* Button styles */
            .menu-button {
                background-color: #45a049;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                font-size: 16px;
                font-family: Arial, sans-serif;
                cursor: pointer;
                border-radius: 5px;
                margin: 5px;
                display: block;
                width: 100%;
            }
            .menu-button:hover {
                background-color: #3e8e41;
            }

            /* Centered text */
            .center-text {
                text-align: center;
                font-family: 'Arial', sans-serif;
                color: #333;
            }
        </style>
    """, unsafe_allow_html=True)
