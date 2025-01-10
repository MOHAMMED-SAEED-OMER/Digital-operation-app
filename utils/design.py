import streamlit as st

def apply_design():
    """
    Apply custom design and styling for the Streamlit app.
    """
    st.markdown("""
        <style>
            /* General app background */
            .appview-container {
                background-color: #f8f9fc;
                color: #333333;
                font-family: 'Arial', sans-serif;
            }

            /* Sidebar customization */
            .css-1d391kg {
                background-color: #0056b3; /* Navy Blue */
                padding: 10px;
            }
            .css-1d391kg .css-qbe2hs {
                color: white;
            }
            .css-1d391kg .css-hxt7ib {
                color: white;
                font-size: 18px;
                font-weight: bold;
            }
            .sidebar-title {
                color: white;
                font-size: 24px;
                text-align: center;
                margin-bottom: 20px;
            }
            .sidebar-subtitle {
                color: white;
                font-size: 16px;
                text-align: center;
                margin-bottom: 10px;
                font-style: italic;
            }

            /* Buttons in the sidebar */
            .css-1d391kg .css-10trblm {
                background-color: #0171f5;
                color: white;
                border: none;
                font-size: 16px;
                font-weight: bold;
                padding: 8px 12px;
                margin: 4px 0;
                border-radius: 5px;
            }
            .css-1d391kg .css-10trblm:hover {
                background-color: #014bb5; /* Darker navy */
            }

            /* Headers in the main app */
            h1 {
                color: #0056b3;
                font-size: 32px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 20px;
            }

            h2 {
                color: #333333;
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 15px;
            }

            h3 {
                color: #444444;
                font-size: 20px;
                font-weight: normal;
                margin-bottom: 10px;
            }

            /* Dataframe and table styles */
            .stDataFrame {
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #ffffff;
                font-size: 14px;
                font-family: 'Arial', sans-serif;
            }

            /* Footer design */
            .footer {
                position: fixed;
                bottom: 0;
                width: 100%;
                background-color: #0056b3;
                color: white;
                text-align: center;
                padding: 10px 0;
                font-size: 14px;
            }
        </style>
    """, unsafe_allow_html=True)

def footer():
    """
    Add a footer for the app.
    """
    st.markdown("""
        <div class="footer">
            Financing and Procurement System | Powered by Streamlit
        </div>
    """, unsafe_allow_html=True)
