import streamlit as st
import random

st.set_page_config(page_title="📜 Random Quote Generator", page_icon="✨")

st.title("📜 Random Quote Generator")

# Some sample quotes
quotes = [
    "The best way to predict the future is to invent it. – Alan Kay",
    "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Happiness depends upon ourselves. – Aristotle",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt"
]

if st.button("✨ Generate Quote"):
    st.success(random.choice(quotes))
