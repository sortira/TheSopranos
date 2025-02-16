import streamlit as st
import sqlite3
import hashlib
from funcs import dashboard
def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hash_password(password)))
    user = c.fetchone()
    conn.close()
    return user

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def app():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state['authenticated'] = True
            st.session_state['username'] = username
            with st.empty():
                dashboard.app()
        else:
            st.error("Invalid credentials")