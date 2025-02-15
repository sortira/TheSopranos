import streamlit as st
import sqlite3

def create_db():
    conn = sqlite3.connect("accessibility.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS accessibility (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            motor_disability INTEGER,
            audio_guide INTEGER,
            sign_language INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_rating(location, motor, audio, sign):
    conn = sqlite3.connect("accessibility.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO accessibility (location, motor_disability, audio_guide, sign_language)
        VALUES (?, ?, ?, ?)
    ''', (location, motor, audio, sign))
    conn.commit()
    conn.close()

def get_average_ratings(location):
    conn = sqlite3.connect("accessibility.db")
    c = conn.cursor()
    c.execute('''
        SELECT AVG(motor_disability), AVG(audio_guide), AVG(sign_language)
        FROM accessibility WHERE location = ?
    ''', (location,))
    result = c.fetchone()
    conn.close()
    return result if result else (None, None, None)

def app():
    st.title("Accessibility Ratings Database")
    create_db()
    
    st.header("Submit a New Rating")
    location = st.text_input("Enter Location:")
    motor = st.slider("Motor Disability Accessibility (1-5)", 1, 5, 3)
    audio = st.slider("Audio Guide Availability (1-5)", 1, 5, 3)
    sign = st.slider("Sign Language Support (1-5)", 1, 5, 3)
    
    if st.button("Submit Rating") and location:
        insert_rating(location, motor, audio, sign)
        st.success("Rating submitted successfully!")
    
    st.header("Lookup Accessibility Ratings")
    lookup_location = st.text_input("Enter Location to Search:")
    if st.button("Search") and lookup_location:
        motor_avg, audio_avg, sign_avg = get_average_ratings(lookup_location)
        if motor_avg is not None:
            st.write(f"**Motor Disability Accessibility:** {motor_avg:.1f} ⭐")
            st.write(f"**Audio Guide Availability:** {audio_avg:.1f} ⭐")
            st.write(f"**Sign Language Support:** {sign_avg:.1f} ⭐")
        else:
            st.write("No ratings found for this location.")