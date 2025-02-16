import streamlit as st
import sqlite3
import hashlib
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hash_password(password)))
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def app():
    st.title("Signup")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Signup"):
        add_user(username, password)
        st.success("Signup successful! Please log in.")