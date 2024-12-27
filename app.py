import streamlit as st
import psycopg2
from datetime import datetime

# Database connection
def connect_to_db():
    return psycopg2.connect(
        host="localhost",
        database="E-operation-database",
        user="postgres",
        password="Hama1234"
    )

# Insert data into the database
def insert_request(requester_name, purpose, amount_requested):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO "E-operation-table" ("Requester name", "purpose", "amount requested", "submission date")
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (requester_name, purpose, amount_requested, datetime.now()))
    conn.commit()
    cursor.close()
    conn.close()

# Streamlit app
st.title("Request Form")

with st.form("request_form"):
    st.subheader("Submit a New Request")
    requester_name = st.text_input("Requester Name")
    purpose = st.text_area("Purpose")
    amount_requested = st.number_input("Amount Requested", min_value=0.0, step=0.01)

    # Submit button
    submitted = st.form_submit_button("Submit Request")
    if submitted:
        if requester_name and purpose and amount_requested > 0:
            insert_request(requester_name, purpose, amount_requested)
            st.success("Request submitted successfully!")
        else:
            st.error("Please fill out all fields.")

# Display submitted data
st.subheader("Submitted Requests")
try:
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "E-operation-table"')
    rows = cursor.fetchall()
    for row in rows:
        st.write(f"ID: {row[0]}, Name: {row[1]}, Purpose: {row[2]}, Amount: {row[3]}, Date: {row[4]}")
    cursor.close()
    conn.close()
except Exception as e:
    st.error(f"Error retrieving data: {e}")
