import os
import subprocess
from datetime import datetime
import streamlit as st
from PIL import Image, ImageOps

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
    .wish-box {
        background-color: #fef2f2;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 10px;
        border: 1px solid #fee2e2;
        color: #991b1b;
    }
    </style>
""", unsafe_allow_html=True)

# --- DIRECTORY SETUP ---
UPLOAD_DIR = "uploaded_media"
os.makedirs(UPLOAD_DIR, exist_ok=True)
GUESTBOOK_FILE = "guestbook.txt"

# --- HEADER & ARCHIVE STATUS ---
st.title("🎉 NICKYBABES @ 50: THE MEMORY ARCHIVE ✨")
st.markdown("*Reliving 4 days of grace, style, love, and unforgettable celebration!*")

st.markdown('<div class="archive-box">💖 Welcome to the official photo sharing hub! Browse, download, and upload your favorite memories from Nicoline’s 50th Jubilee. 🥂✨</div>', unsafe_allow_html=True)

# --- YOUTUBE HIGHLIGHT VIDEO SECTION ---
st.subheader("🎬 Celebration Highlight Video")
st.video("https://youtu.be/3cqJRqPMMvU")

st.markdown("---")

# --- DIGITAL GUESTBOOK & WISHES WALL ---
st.subheader("💌 Digital Guestbook & Wishes Wall")
st.markdown("Leave a heartfelt birthday wish or personal memory for Nicoline below!")

with st.form("guestbook_form", clear_on_submit=True):
    guest_name = st.text_input("Your Name / Family")
    guest_message = st.text_area("Your Birthday Wish or Message")
    submit_wish = st.form_submit_button("💖 Send Wish")
    
    if submit_wish:
        if guest_name.strip() and guest_message.strip():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            with open(GUESTBOOK_FILE, "a", encoding="utf-8") as f:
                f.write(f"**{guest_name}** ({timestamp}):\n{guest_message}\n---\n")
            st.success("✨ Your wish has been added to the Guestbook!")
        else:
            st.warning("Please enter both your name and a message before submitting.")

# Display saved wishes
if os.path.exists(GUESTBOOK_FILE):
    with st.expander("📖 Read All Guestbook Wishes", expanded=True):
        with open(GUESTBOOK_FILE, "r", encoding="utf-8") as f:
            wishes_content = f.read()
        wishes = wishes_content.split("---")
        for wish in reversed(wishes):
            if wish.strip():
                st.markdown(f'<div class="wish-box">{wish.strip()}</div>', unsafe_allow_html=True)

st.markdown("---")

# --- GALLERY & MEDIA UPLOAD SECTION ---
st.subheader("📸 Event Photo & Video Gallery")
st.markdown("Upload new memories or browse the collection below. Use the **Download** button under any photo or video to save it directly to your device!")

uploaded_files = st.file_uploader(
    "Upload your photos or videos...", 
    type=["jpg", "jpeg", "png", "mp4", "mov", "avi"], 
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        if not os.path.exists(file_path):
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Auto-rotate image based on EXIF orientation if it's an image
            if uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    img = Image.open(file_path)
                    img = ImageOps.exif_transpose(img)
                    img.save(file_path)
                except Exception:
                    pass

            try:
                subprocess.run(["git", "add", file_path], check=True)
                subprocess.run(["git", "commit", -m, f"Auto-upload archive: {uploaded_file.name}"], check=True)
                subprocess.run(["git", "push"], check=True)
            except Exception as e:
                st.warning(f"Saved locally, git sync skipped: {e}")

    st.success("✨ New memories added and saved successfully!")

raw_saved_files = os.listdir(UPLOAD_DIR)
saved_files = sorted(list(set([f for f in raw_saved_files if not f.startswith(".") and f != "nicoline.jpg"])))

if saved_files:
    st.markdown("### 🌟 Shared Memory Collection")
    gallery_cols = st.columns(3)
    for i, filename in enumerate(saved_files):
        file_path = os.path.join(UPLOAD_DIR, filename)
        col = gallery_cols[i % 3]
        with col:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    pil_img = Image.open(file_path)
                    pil_img = ImageOps.exif_transpose(pil_img)
                    st.image(pil_img, caption=filename, use_container_width=True)
                except Exception:
                    st.image(file_path, caption=filename, use_container_width=True)

                with open(file_path, "rb") as file:
                    st.download_button(
                        label="📥 Download Photo",
                        data=file,
                        file_name=filename,
                        mime="image/jpeg",
                        key=f"dl_{filename}"
                    )
            elif filename.lower().endswith(('.mp4', '.mov', '.avi')):
                st.video(file_path)
                with open(file_path, "rb") as file:
                    st.download_button(
                        label="📥 Download Video",
                        data=file,
                        file_name=filename,
                        mime="video/mp4",
                        key=f"dl_{filename}"
                    )

st.markdown("---")

# --- FOOTER ---
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 0.9rem;'>"
    "Created with ❤️ by <b>Chi Barison Fru</b> for Nicoline Che's 50th Jubilee | "
    "<a href='https://frankfru.com'>frankfru.com</a> | "
    "<a href='https://github.com/chifru19'>GitHub</a> | "
    "<a href='https://www.linkedin.com/in/chifru19'>LinkedIn</a>"
    "</div>",
    unsafe_allow_html=True,
)
