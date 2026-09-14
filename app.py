import os
import subprocess
from datetime import datetime
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="NICKYBABES @ 50, THE COUNTDOWN IS OFFICIALY ON!",
    page_icon="✨",
    layout="centered"
)

# --- CUSTOM CSS FOR MOBILE & COUNTDOWN ---
st.markdown("""
    <style>
    .stImage img, .stVideo video {
        border-radius: 10px;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .countdown-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        color: #ff4b4b;
        margin-bottom: 20px;
    }
    .music-box {
        background-color: #f0fdf4;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid #dcfce7;
    }
    </style>
""", unsafe_allow_html=True)

# --- DIRECTORY SETUP ---
UPLOAD_DIR = "uploaded_media"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# --- HEADER & COUNTDOWN TIMER ---
st.title("🎉 NICKYBABES @ 50, THE COUNTDOWN IS OFFICIALY ON! 🎉")
st.markdown("*Celebrating 50 years of grace, love & blessings!*")

# --- SPOTIFY PLAYLIST PLAYER (AD-FREE) ---
st.markdown("""
    <div class="music-box">
        <p style="margin: 0 0 5px 0; font-weight: bold; color: #15803d; font-size: 1rem;">🎶 Nicoline's Celebration Playlist (Ad-Free)</p>
        <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7sbwzGf6xs7nW9r2LtNw9H?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    </div>
""", unsafe_allow_html=True)

# Calculate countdown to Thursday, Sept 17, 2026
from datetime import date
# Exact calendar day difference for Sept 17, 2026 celebration
days_left = (date(2026, 9, 17) - date.today()).days