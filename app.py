import os
import subprocess
from datetime import datetime
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="NICKYBABES @ 50 • THE JUBILEE MEMORY ARCHIVE",
    page_icon="✨",
    layout="centered"
)

# --- CUSTOM CSS FOR MOBILE & GALLERY ---
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
    .archive-box {
        background-color: #f0fdf4;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        color: #15803d;
        margin-bottom: 20px;
        border: 1px solid #dcfce7;
    }
    .music-box {
        background-color: #f8fafc;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }
    </style>
""", unsafe_allow_html=True)

# --- DIRECTORY SETUP ---
UPLOAD_DIR = "uploaded_media"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# --- HEADER & ARCHIVE STATUS ---
st.title("🎉 NICKYBABES @ 50: THE MEMORY ARCHIVE ✨")
st.markdown("*Reliving 4 days of grace, style, love, and unforgettable celebration!*")

st.markdown('<div class="archive-box">💖 Welcome to the official photo sharing hub! Browse, download, and upload your favorite memories from Nicoline’s 50th Jubilee. 🥂✨</div>', unsafe_allow_html=True)

# --- SPOTIFY PLAYLIST PLAYER (AD-FREE) ---
st.markdown("""
    <div class="music-box">
        <p style="margin: 0 0 5px 0; font-weight: bold; color: #1e293b; font-size: 1rem;">🎶 Nicoline's Celebration Official Playlist</p>
        <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7sbwzGf6xs7nW9r2LtNw9H?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- GALLERY & MEDIA UPLOAD SECTION ---
st.subheader("📸 Event Photo & Video Gallery")
st.markdown("Upload new photos/videos or browse the collection below. Click on any image or use your device options to download/save your favorite moments!")

uploaded_files = st.file_uploader(
    "Upload your photos or videos...", 
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
                subprocess.run(["git", "commit", "-m", f"Auto-upload archive: {uploaded_file.name}"], check=True)
                subprocess.run(["git", "push"], check=True)
            except Exception as e:
                st.warning(f"Saved locally, git sync skipped: {e}")

    st.success("✨ New memories added and saved successfully!")

raw_saved_files = os.listdir(UPLOAD_DIR)
saved_files = [f for f in sorted(raw_saved_files) if not f.startswith(".") and f != "nicoline.jpg"]

if saved_files:
    st.markdown("### 🌟 Shared Memory Collection")
    gallery_cols = st.columns(3)
    for i, filename in enumerate(saved_files):
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
    "Created with ❤️ by <b>Frank Fru</b> for Nicoline Che's 50th Jubilee | "
    "<a href='https://frankfru.com'>frankfru.com</a> | "
    "<a href='https://github.com/chifru19'>GitHub</a> | "
    "<a href='https://www.linkedin.com/in/chifru19'>LinkedIn</a>"
    "</div>",
    unsafe_allow_html=True,
)