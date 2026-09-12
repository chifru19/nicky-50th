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
    .stImage img {
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
    </style>
""", unsafe_allow_html=True)

# --- DIRECTORY SETUP ---
UPLOAD_DIR = "uploaded_media"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# --- BACKGROUND MUSIC (HIDDEN BACKGROUND PLAYER) ---
st.markdown(
    '<iframe width="0" height="0" scrolling="no" frameborder="no" allow="autoplay" '
    'src="https://www.youtube.com/embed/Tv1ZuDURjSs?autoplay=1&loop=1&playlist=Tv1ZuDURjSs" style="display:none;"></iframe>',
    unsafe_allow_html=True
)

# --- HEADER & COUNTDOWN TIMER ---
st.title("🎉 NICKYBABES @ 50, THE COUNTDOWN IS OFFICIALY ON! 🎉")
st.markdown("*Celebrating 50 years of grace, love & blessings!*")

# Calculate countdown to Thursday, Sept 17, 2026
target_date = datetime(2026, 9, 17, 0, 0, 0)
today = datetime.now()
days_left = (target_date - today).days

if days_left > 0:
    st.markdown(f'<div class="countdown-box">⏳ Only {days_left} Days Left Until the Big Celebration! 🎈</div>', unsafe_allow_html=True)
elif days_left == 0:
    st.markdown('<div class="countdown-box">🚨 The Celebration Starts TODAY! Let the Jubilee Begin! 🥂</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="countdown-box">💖 Hope you had an amazing 50th Jubilee celebration! ✨</div>', unsafe_allow_html=True)

if os.path.exists("nicoline.jpg"):
    st.image("nicoline.jpg", caption="Celebrating Nicoline Che's 50th Jubilee", width='stretch')
else:
    st.info("🖼️ Please place `nicoline.jpg` in the project folder.")

st.markdown("---")

# --- BIRTHDAY PROGRAM SECTION ---
st.subheader("📅 4 Days • 4 Unique Vibes • 1 Unforgettable 50th!")
st.write("### Thursday 17th – Sunday 20th September")

if os.path.exists("program.jpg"):
    st.image("program.jpg", caption="Full Event Program & Dress Codes", width='stretch')

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🕺 Thursday 17th September")
    st.markdown("**Meet & Greet**")
    st.markdown("* **Dress Code:** 70's Dressing")
    st.markdown("* *Think bold, groovy and fabulous!*")
    
    st.markdown("### ⚓ Friday 18th September")
    st.markdown("**Boatride Experience**")
    st.markdown("* **Dress Code:** All White")
    st.markdown("* *Sail in style, all white everything!*")
    
    if os.path.exists("boat_image.jpg"):
        st.image("boat_image.jpg", caption="Espírito Oceânico Boat", width='stretch')
    st.markdown("[🔗 View Official Boat Experience Details](https://algarexperience.com/en/boat/espirito-oceanico-2/)")

with col2:
    st.markdown("### 🥂 Saturday 19th September")
    st.markdown("**Black Tie Event**")
    st.markdown("* **Men:** Black suit, white shirt, black tie")
    st.markdown("* **Women:** Black gala dress or white")

    st.markdown("### 🍖 Sunday 20th September")
    st.markdown("**BBQ Event**")
    st.markdown("* **Dress Code:** Blue Jeans & White Top")

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
            
            # Automatically push uploaded files to GitHub for permanent persistence
            try:
                subprocess.run(["git", "add", file_path], check=False)
                subprocess.run(["git", "commit", "-m", f"Auto-save guest upload: {uploaded_file.name}"], check=False)
                subprocess.run(["git", "push", "origin", "main"], check=False)
            except Exception:
                pass

    st.success("✨ Files uploaded and saved successfully!")

# Display all saved media in the folder persistently
saved_files = os.listdir(UPLOAD_DIR)
if saved_files:
    st.markdown("### 🌟 Shared Gallery Collection")
    gallery_cols = st.columns(3)
    for i, filename in enumerate(saved_files):
        if filename.startswith('.'):
            continue
        file_path = os.path.join(UPLOAD_DIR, filename)
        col = gallery_cols[i % 3]
        with col:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                st.image(file_path, caption=filename, width='stretch')
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
