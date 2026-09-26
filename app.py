import os
import subprocess
import zipfile
import io
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
    .guestbook-card {
        background-color: #f8fafc;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 10px;
        border: 1px solid #e2e8f0;
    }
    </style>
""", unsafe_allow_html=True)

# --- DIRECTORY SETUP ---
UPLOAD_DIR = "uploaded_media"
GUESTBOOK_FILE = "guestbook_wishes.txt"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# --- HEADER & ARCHIVE STATUS ---
st.title("🎉 NICKYBABES @ 50: THE MEMORY ARCHIVE ✨")
st.markdown("*Reliving 4 days of grace, style, love, and unforgettable celebration!*")

st.markdown('<div class="archive-box">💖 Welcome to the official memory hub! Browse, filter by event days, download, upload memories, and leave your wishes. 🥂✨</div>', unsafe_allow_html=True)

# --- HIGHLIGHT YOUTUBE VIDEO ---
st.subheader("🎬 Celebration Highlight Video")
st.video("https://www.youtube.com/watch?v=3cqJRqPMMvU")

st.markdown("---")

# --- GUESTBOOK / WISHES WALL SECTION ---
st.subheader("💌 Guestbook & Birthday Wishes")
st.markdown("Leave a heartfelt message, birthday wish, or memory for Nicoline!")

with st.form("guestbook_form"):
    guest_name = st.text_input("Your Name / Family")
    guest_wish = st.text_area("Your Birthday Wish or Memory")
    submit_wish = st.form_submit_button("Send Wish 💖")
    
    if submit_wish and guest_name and guest_wish:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(GUESTBOOK_FILE, "a") as f:
            f.write(f"**{guest_name}** ({timestamp}): {guest_wish}\n---\n")
        st.success("Thank you! Your wish has been added to the digital guestbook.")

if os.path.exists(GUESTBOOK_FILE):
    with st.expander("📖 Read Digital Guestbook Cards"):
        with open(GUESTBOOK_FILE, "r") as f:
            wishes_content = f.read()
        for entry in wishes_content.split("---"):
            if entry.strip():
                st.markdown(f'<div class="guestbook-card">{entry.strip()}</div>', unsafe_allow_html=True)

st.markdown("---")

# --- GALLERY & MEDIA UPLOAD SECTION ---
st.subheader("📸 Event Photo & Video Gallery")
st.markdown("Sort by event days, download single items, or download the entire archive in one click!")

# --- DOWNLOAD ALL AS ZIP ---
raw_saved_files = os.listdir(UPLOAD_DIR)
saved_files = [f for f in sorted(raw_saved_files) if not f.startswith(".") and f != "nicoline.jpg"]

if saved_files:
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for filename in saved_files:
            file_path = os.path.join(UPLOAD_DIR, filename)
            zip_file.write(file_path, arcname=filename)
    zip_buffer.seek(0)
    
    st.download_button(
        label="📦 Download All Media as ZIP (Entire Archive)",
        data=zip_buffer,
        file_name="Nickybabes_50th_Jubilee_Archive.zip",
        mime="application/zip",
        key="download_all_zip"
    )

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
            try:
                if uploaded_file.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                    img = Image.open(file_path)
                    img = ImageOps.exif_transpose(img)
                    img.save(file_path)
                
                subprocess.run(["git", "add", file_path], check=True)
                subprocess.run(["git", "commit", "-m", f"Auto-upload archive: {uploaded_file.name}"], check=True)
                subprocess.run(["git", "push"], check=True)
            except Exception as e:
                st.warning(f"Saved locally, git sync skipped: {e}")

    st.success("✨ New memories added and saved successfully!")

# --- CATEGORY / DAY FILTER TABS ---
raw_saved_files = os.listdir(UPLOAD_DIR)
saved_files = [f for f in sorted(raw_saved_files) if not f.startswith(".") and f != "nicoline.jpg"]

if saved_files:
    st.markdown("### 🌟 Shared Memory Collection")
    
    tab_all, tab_70s, tab_boat, tab_gala, tab_bbq = st.tabs([
        "✨ All Memories", 
        "🕺 70s Meet & Greet", 
        "⚓ Boat Ride", 
        "🥂 Gala & Party", 
        "🍖 Sunday BBQ"
    ])
    
    def render_gallery(file_subset):
        if not file_subset:
            st.info("No media found in this category yet.")
            return
        gallery_cols = st.columns(3)
        for i, filename in enumerate(file_subset):
            file_path = os.path.join(UPLOAD_DIR, filename)
            col = gallery_cols[i % 3]
            with col:
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        img = Image.open(file_path)
                        img = ImageOps.exif_transpose(img)
                        st.image(img, caption=filename, width='stretch')
                        
                        # Fullscreen Lightbox expander view
                        with st.expander("🔍 Fullscreen View"):
                            st.image(img, caption=filename, width='stretch')
                    except Exception:
                        st.image(file_path, caption=filename, width='stretch')
                    
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

    with tab_all:
        render_gallery(saved_files)
        
    with tab_70s:
        # Filter files or show all if general
        render_gallery([f for f in saved_files if "70" in f.lower() or "meet" in f.lower()])
        
    with tab_boat:
        render_gallery([f for f in saved_files if "boat" in f.lower() or "marina" in f.lower() or "ocean" in f.lower()])
        
    with tab_gala:
        render_gallery([f for f in saved_files if "gala" in f.lower() or "black" in f.lower() or "w_" in f.lower()])
        
    with tab_bbq:
        render_gallery([f for f in saved_files if "bbq" in f.lower() or "sunday" in f.lower() or "hora" in f.lower()])

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
