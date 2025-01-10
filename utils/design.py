import streamlit as st

def apply_design():
    st.markdown("""
        <style>
            /* General background */
            body {
                margin: 0;
                padding: 0;
                overflow-x: hidden;
            }

            /* Sidebar styling */
            .css-1d391kg {
                background-color: #2e7d32;
                color: white;
            }

            /* Sticky navigation bar at the top */
            .css-18e3th9 {
                position: sticky;
                top: 0;
                z-index: 100;
                background-color: #2e7d32;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }

            /* Make headings more prominent */
            h1, h2, h3, h4, h5, h6 {
                font-family: Arial, sans-serif;
            }

            /* Buttons */
            button {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                font-size: 16px;
                cursor: pointer;
                border-radius: 5px;
            }

            button:hover {
                background-color: #45a049;
            }

            /* Footer or additional content */
            .footer {
                text-align: center;
                margin-top: 20px;
                color: #666;
                font-size: 14px;
            }
        </style>
    """, unsafe_allow_html=True)
