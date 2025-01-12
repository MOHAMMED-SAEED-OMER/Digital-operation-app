import streamlit as st
from utils.database import read_data

def database_page():
    st.markdown("""
        <style>
            .dataframe-container {
                max-height: 500px;
                overflow-y: auto;
                margin-top: 20px;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("📂 Database")
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h2 style="color: #2E8B57; font-family: Arial, sans-serif;">View All Requests</h2>
            <p style="color: #555; font-size: 16px;">Search, filter, and explore requests stored in the database.</p>
        </div>
    """, unsafe_allow_html=True)

    # Read the data
    data = read_data()

    if not data.empty:
        # Add search functionality
        search_query = st.text_input("🔍 Search by Requester Name or Reference ID:", "")
        if search_query:
            filtered_data = data[
                data["Requester Name"].str.contains(search_query, case=False, na=False) |
                data["Reference ID"].str.contains(search_query, case=False, na=False)
            ]
        else:
            filtered_data = data

        # Add filters for status and finance status
        with st.expander("🔧 Advanced Filters"):
            col1, col2 = st.columns(2)
            with col1:
                status_filter = st.selectbox(
                    "Filter by Status:",
                    options=["All"] + data["Status"].dropna().unique().tolist(),
                    index=0
                )
            with col2:
                finance_status_filter = st.selectbox(
                    "Filter by Finance Status:",
                    options=["All"] + data["Finance Status"].dropna().unique().tolist(),
                    index=0
                )

            # Apply filters
            if status_filter != "All":
                filtered_data = filtered_data[filtered_data["Status"] == status_filter]
            if finance_status_filter != "All":
                filtered_data = filtered_data[filtered_data["Finance Status"] == finance_status_filter]

        # Show total results count
        st.markdown(f"### 📊 {len(filtered_data)} Results Found")

        # Display the data in a scrollable container
        st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
        st.dataframe(filtered_data, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Allow export to CSV
        csv_data = filtered_data.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Export Filtered Data to CSV",
            data=csv_data,
            file_name="filtered_requests.csv",
            mime="text/csv"
        )
    else:
        st.warning("⚠️ No requests found. Submit a request to populate the database.")
