import streamlit as st
import psycopg2

# Database connection function
def create_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",  # Replace with your server's IP if not local
            port=5432,         # Default PostgreSQL port
            database="E-operation-database",  # Your database name
            user="postgres",   # Your username
            password="Hama1234"  # Your password
        )
        return conn
    except Exception as e:
        st.error(f"Error connecting to the database: {e}")
        return None

# Insert data into the database
def insert_data(requester_name, purpose, amount_requested):
    conn = create_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                query = """
                INSERT INTO "E-operation-table" ("Requester name", "Purpose", "amount requested", "submission date")
                VALUES (%s, %s, %s, CURRENT_TIMESTAMP)
                """
                cur.execute(query, (requester_name, purpose, amount_requested))
                conn.commit()
                st.success("Request submitted successfully!")
        except Exception as e:
            st.error(f"Error inserting data: {e}")
        finally:
            conn.close()

# Retrieve data from the database
def get_data():
    conn = create_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                query = 'SELECT * FROM "E-operation-table"'
                cur.execute(query)
                rows = cur.fetchall()
                return rows
        except Exception as e:
            st.error(f"Error retrieving data: {e}")
            return []
        finally:
            conn.close()
    return []

# Streamlit app layout
def main():
    st.title("E-Operation Request System")

    menu = ["Submit Request", "View Requests"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Submit Request":
        st.subheader("Submit a New Request")
        requester_name = st.text_input("Requester Name")
        purpose = st.text_area("Purpose of Request")
        amount_requested = st.number_input("Amount Requested", min_value=0.0, step=0.01)

        if st.button("Submit"):
            if requester_name and purpose and amount_requested > 0:
                insert_data(requester_name, purpose, amount_requested)
            else:
                st.warning("Please fill out all fields correctly.")

    elif choice == "View Requests":
        st.subheader("All Submitted Requests")
        data = get_data()
        if data:
            st.write("### Submitted Requests")
            for row in data:
                st.write(f"ID: {row[0]}, Requester: {row[1]}, Purpose: {row[2]}, "
                         f"Amount: {row[3]}, Date: {row[4]}")
        else:
            st.info("No data found.")

if __name__ == "__main__":
    main()
    psql -h localhost -U postgres -d "E-operation-database"
