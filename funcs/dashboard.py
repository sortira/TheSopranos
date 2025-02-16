import streamlit as st
from funcs import home
import sqlite3
def app():
    if st.session_state.get('authenticated', False):
        st.title("Dashboard")
        st.write(f"Welcome {st.session_state['username']}!")
        if st.button("Logout"):
            st.session_state['authenticated'] = False
            st.empty()
            home.app()
    else:
        st.warning("Please login to view the dashboard")
        with st.empty():
            home.app()