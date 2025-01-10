import streamlit as st

def welcome_page():
    # Welcome content section
    st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <h2>Welcome to the E-Operation App</h2>
            <p style="font-size: 18px; line-height: 1.6; color: #4CAF50;">
                Streamline your organization's financing and procurement processes with our user-friendly platform.
                Submit, track, and manage all your requests effortlessly in one place.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Features section
    st.markdown("""
        <div style="margin-top: 40px; padding: 20px; background-color: #f1f8f2; border-radius: 10px;">
            <h3 style="color: #2e7d32;">Key Features</h3>
            <ul style="font-size: 16px; line-height: 1.8; color: #333;">
                <li><strong>Submit Requests:</strong> Use the form to submit new financing or procurement requests.</li>
                <li><strong>Track Progress:</strong> View and monitor the status of submitted requests in the database.</li>
                <li><strong>Manager's View:</strong> Approve or decline requests with ease.</li>
                <li><strong>Liquidation Processing:</strong> Simplify liquidation tasks with our integrated tools.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Call-to-Action Footer
    st.markdown("""
        <div class="footer">
            <p style="font-size: 16px; color: #333;">
                Ready to get started? Navigate through the sidebar to explore all features tailored to your role.
            </p>
        </div>
    """, unsafe_allow_html=True)
