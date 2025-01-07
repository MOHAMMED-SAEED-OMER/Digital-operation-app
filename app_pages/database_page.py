import streamlit as st
from utils.database import read_data

def database_page():
    st.title("Database")
    st.subheader("View All Transactions")

    # Read the database
    data = read_data()

    if not data.empty:
        # Provide filtering options
        st.sidebar.subheader("Filter Options")
        trx_type = st.sidebar.selectbox("Transaction Type", ["All", "Expense", "Income"], index=0)
        project_name = st.sidebar.text_input("Project Name (leave blank for all)")
        budget_line = st.sidebar.text_input("Budget Line (leave blank for all)")

        # Apply filters
        if trx_type != "All":
            data = data[data["Transaction Type"] == trx_type]
        if project_name.strip():
            data = data[data["Project Name"].str.contains(project_name.strip(), case=False, na=False)]
        if budget_line.strip():
            data = data[data["Budget Line"].str.contains(budget_line.strip(), case=False, na=False)]

        # Display the filtered data
        if not data.empty:
            st.dataframe(data)
        else:
            st.warning("No transactions match the selected filters.")
    else:
        st.warning("No transactions found. Add transactions to populate the database.")
