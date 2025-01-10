import streamlit as st

def apply_design():
    """
    Apply custom design and styling for the Streamlit app.
    """
    st.markdown("""
        <style>
            /* General Background */
            .css-1v3fvcr {
                background-color: #f4f7fc;  /* Light gray background */
            }

            /* Sidebar Customization */
            .css-1d391kg {
                background-color: #2e7d32;  /* Dark green for sidebar */
                padding: 20px;
            }
            .css-1d391kg .css-qbe2hs {
                color: white;  /* Sidebar text color */
            }
            .css-1d391kg .css-hxt7ib {
                color: white;
                font-size: 18px;
                font-family: Arial, sans-serif;
                font-weight: bold;
            }

            /* Sidebar Title */
            .sidebar-title {
                color: white;
                font-size: 24px;
                text-align: center;
                font-family: Arial, sans-serif;
                margin-bottom: 20px;
            }

            /* Tabs Customization */
            div[data-testid="stHorizontalBlock"] {
                border-bottom: 2px solid #2e7d32; /* Green border under tabs */
                margin-bottom: 10px;
            }
            div[data-testid="stHorizontalBlock"] > div > div {
                border: 1px solid #2e7d32;  /* Green border around tabs */
                border-radius: 10px;
                padding: 5px;
                font-family: Arial, sans-serif;
                font-weight: bold;
                background-color: #ffffff;  /* White background for tabs */
                margin-right: 10px;
            }
            div[data-testid="stHorizontalBlock"] > div > div:hover {
                background-color: #f1f8f2; /* Light green hover effect */
            }
            div[data-testid="stHorizontalBlock"] > div > div[aria-selected="true"] {
                background-color: #2e7d32; /* Highlighted tab color */
                color: white;
            }

            /* Headers */
            h1 {
                color: #2e7d32; /* Green headers */
                font-family: 'Arial', sans-serif;
                font-weight: bold;
                text-align: center;
                margin-top: 0px;
            }

            /* Buttons */
            button {
                font-family: Arial, sans-serif;
                font-size: 16px;
                padding: 10px 20px;
                background-color: #2e7d32; /* Button background green */
                color: white; /* Button text color */
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #256528; /* Darker green on hover */
            }

            /* Adjust container width for cleaner layout */
            .block-container {
                padding: 20px;
                max-width: 1200px;
                margin: auto;
            }
        </style>
    """, unsafe_allow_html=True)
