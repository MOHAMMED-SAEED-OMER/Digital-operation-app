import streamlit as st

def welcome_page():
    st.title("Welcome to the E-Operation App")
    st.markdown("""
        - **Submit Requests:** Use the form to submit a new request.
        - **View Database:** View all submitted requests.
    """)

