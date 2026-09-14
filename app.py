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
target_date = datetime(2026, 9, 17, 0, 0, 0)
today = datetime.now()
days_left = (target_date.date() - today.date()).days

if days_left > 0:
    st.markdown(f'<div class="countdown-box">⏳ Only {days_left} Days Left Until the Big Celebration! 🎈</div>', unsafe_allow_html=True)
elif days_left == 0:
    st.markdown('<div class="countdown-box">🚨 The Celebration Starts TODAY! Let the Jubilee Begin! 🥂</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="countdown-box">💖 Hope you had an amazing 50th Jubilee celebration! ✨</div>', unsafe_allow_html=True)

# --- HERO BIRTHDAY VIDEO ---
if os.path.exists("hero_video.mp4"):
    st.video("hero_video.mp4")
elif os.path.exists("nicoline.jpg"):
    st.image("nicoline.jpg", caption="Celebrating Nicoline Che's 50th Jubilee", use_container_width=True)
else:
    st.info("🖼️ Please place `hero_video.mp4` or `nicoline.jpg` in the project folder.")

st.markdown("---")

# --- BIRTHDAY PROGRAM & DETAILED ADDRESSES SECTION ---
st.subheader("📅 4 Days • 4 Unique Vibes • 1 Unforgettable 50th!")
st.write("### Thursday 17th – Sunday 20th September")

if os.path.exists("program_details.jpg"):
    st.image("program_details.jpg", caption="Nickybabes 50th Birthday Official Program & Addresses", use_container_width=True)
elif os.path.exists("program.jpg"):
    st.image("program.jpg", caption="Full Event Program & Dress Codes", use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🕺 Thursday 17th September")
    st.markdown("**FUNKY 70'S • Meet & Greet**")
    st.markdown("* 📍 **Address:** R. Hora da Pedra, 8200 Albufeira, Portugal")
    st.markdown("* ⏰ **Start Time:** 19:00 PM")
    st.markdown("* 🚗 **Travel:** 7 Mins Drive from W Algarve")
    st.markdown("* 👗 **Dress Code:** Think 70's Vibes! Bright, Bold & Fun")
    
    st.markdown("### ⚓ Friday 18th September")
    st.markdown("**ALL WHITE • Boatride**")
    st.markdown("* 📍 **Address:** AlgarveExperience, Marina de Albufeira, Passeio dos Oceanos, Lote 3 Loja 7, 8200-394 Albufeira, Portugal")
    st.markdown("* ⏰ **Time:** Meetup at Marina at 16:00")
    st.markdown("* 👗 **Dress Code:** All White Everything! Clean, Chic & Elegant")
    
    if os.path.exists("boat_image.jpg"):
        st.image("boat_image.jpg", caption="Espírito Oceânico Catamaran", use_container_width=True)
    st.markdown("[🔗 View Official Boat Experience Details](https://algarexperience.com/en/boat/espirito-oceanico-2/)")

with col2:
    st.markdown("### 🥂 Saturday 19th September")
    st.markdown("**BLACK TIE • Gala & After Party**")
    st.markdown("* 📍 **Address:** W Algarve, Estrada da Galé Sesmarias - CX Postal 290, H, 8200-385 Albufeira, Portugal")
    st.markdown("* ⏰ **Garden Fountain Gala:** 15:30 – 22:30")
    st.markdown("* 🎧 **After Party (W Studios):** 22:30 – 02:00")
    st.markdown("* 👗 **Dress Code:** Black Tie Elegance! Classy, Sophisticated & Timeless")

    st.markdown("### 🍖 Sunday 20th September")
    st.markdown("**SUNDAY BBQ**")
    st.markdown("* 📍 **Address:** R. Hora da Pedra, 8200 Albufeira, Portugal")
    st.markdown("* ⏰ **Start Time:** 15:00 PM")
    st.markdown("* 🚗 **Travel:** 7 Mins Drive from W Algarve")
    st.markdown("* 👗 **Dress Code:** White Top & Blue Jeans (Casual, Cool & Comfortable)")

st.markdown("---")

# --- GALLERY & MEDIA UPLOAD SECTION ---
st.subheader("📸 Memories & Gallery Upload")
st.markdown("Upload photos/videos or share a YouTube link to celebrate Nicky's 50th Jubilee!")

uploaded_files = st.file_uploader(
    "Choose photos or videos...", 
    type=["jpg", "jpeg", "png", "mp4", "mov", "avi"], 
    accept_multiple_files=True
)

youtube_url = st.text_input("🔗 Or paste a YouTube Video Link here:")

if youtube_url:
    try:
        st.video(youtube_url)
    except Exception as e:
        st.error("Please enter a valid YouTube URL.")

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        if not os.path.exists(file_path):
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            try:
                subprocess.run(["git", "add", file_path], check=True)
                subprocess.run(["git", "commit", "-m", f"Auto-upload: {uploaded_file.name}"], check=True)
                subprocess.run(["git", "push"], check=True)
            except Exception as e:
                st.warning(f"Saved locally, git sync skipped: {e}")

    st.success("✨ Files uploaded and saved successfully!")

# Display all saved media in the folder persistently
import re

def get_clean_basename(f_name):
    name, ext = os.path.splitext(f_name)
    clean_name = re.sub(r"\s*\(\d+\)$", "", name)
    return clean_name + ext

import re
def get_clean_basename(f_name):
    name, ext = os.path.splitext(f_name)
    clean_name = re.sub(r"\\s*\\(\\d+\\)$", "", name)
    return clean_name + ext

raw_saved_files = os.listdir(UPLOAD_DIR)
seen_bases = set()
saved_files = []
for filename in sorted(raw_saved_files):
    if filename.startswith(".") or filename == "nicoline.jpg":
        continue
    base = get_clean_basename(filename)
    if base not in seen_bases:
        seen_bases.add(base)
        saved_files.append(filename)
seen_bases = set()
saved_files = []
for filename in sorted(raw_saved_files):
    if filename.startswith("."):
        continue
    base = get_clean_basename(filename)
    if base not in seen_bases:
        seen_bases.add(base)
        saved_files.append(filename)

if saved_files:
    st.markdown("### 🌟 Shared Gallery Collection")
    gallery_cols = st.columns(3)
    for i, filename in enumerate(saved_files):
        if filename.startswith('.') or filename == "nicoline.jpg":
            continue
        file_path = os.path.join(UPLOAD_DIR, filename)
        col = gallery_cols[i % 3]
        with col:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                st.image(file_path, caption=filename, use_container_width=True)
            elif filename.lower().endswith(('.mp4', '.mov', '.avi')):
                st.video(file_path)

st.markdown("---")

# --- FOOTER ---
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 0.9rem;'>"
    "Created with ❤️ by <b>Chi Barison Fru</b> for Nicoline Che's 50th Jubilee | "
    "<a href='https://frankfru.com'>frankfru.com</a> | "
    "<a href='https://github.com/chifru19'>GitHub</a> | "
    "<a href='https://www.linkedin.com/in/frank-fru/'>LinkedIn</a>"
    "</div>",
    unsafe_allow_html=True,
)
