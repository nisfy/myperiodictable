"""
🏠 Ensiklopedia Unsur Kimia - Proyek Kelompok 13
Politeknik AKA Bogor

Multi-Halaman Streamlit dengan Tema Kawaii Chemistry
"""

import streamlit as st
import pandas as pd
import time

# ============================================
# 🔧 KONFIGURASI HALAMAN
# ============================================
st.set_page_config(
    page_title="Ensiklopedia Unsur Kimia",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# 📦 DATA UNSUR PERIODIK (Tabel Pendek)
# ============================================

# ============================================
# 🎨 WARNA KATEGORI (Kawaii Chemistry)
# ============================================
CATEGORY_COLORS = {
    "Logam Alkali": "#FFB6C1",
    "Logam Alkali Tanah": "#FFD6A5",
    "Logam Transisi": "#FFF3B0",
    "Logam Lainnya": "#CDEAC0",
    "Metaloid": "#B5EAEA",
    "Nonlogam": "#BDE0FE",
    "Halogen": "#D8B4FE",
    "Gas Mulia": "#F8C8DC",
    "Lantanida": "#DCC6FF",
    "Aktinida": "#F4C2E7",
}

# ============================================
# 📋 LEGENDA KATEGORI
# ============================================
LEGEND_MARKDOWN = """
### 🎨 Legenda Warna Kategori
"""

for category, color in CATEGORY_COLORS.items():
    LEGEND_MARKDOWN += f"""
<span style="background-color: {color}; padding: 5px 12px; border-radius: 15px; margin: 3px;">
  <span style="color: #333;">●</span> {category}
</span>
"""

# ============================================
# 🎭 LOADING SCREEN
# ============================================
def show_loading_screen():
    """Tampilkan loading screen dengan GIF"""
    loading_container = st.empty()
    
    with loading_container.container():
        st.markdown("""
        <div style="text-align: center; padding: 50px;">
            <h2>🧪 Memuat Ensiklopedia Unsur Kimia...</h2>
            <br>
            <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHFsNXM0aHF5bGhlNjgzYm14eW05dzUwOXMwdWp4ZXF6ZXUybW0wZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/BZyYk1m8x1B3GMH1V1/giphy.gif" 
                 width="200" 
                 style="border-radius: 20px; box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
            <br><br>
            <p style="color: #888;">✨ Harap tunggu sebentar...</p>
        </div>
        """, unsafe_allow_html=True)
    
    time.sleep(2)  # Loading 2 detik
    loading_container.empty()

# ============================================
# 🎨 CSS KUSTOM KUWAII CHEMISTRY
# ============================================
CUSTOM_CSS = """
<style>
    /* Import Font */
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');
    
    /* Background Utama */
    .stApp {
        background: linear-gradient(135deg, #FFF6FB 0%, #F3EEFF 50%, #EAF8FF 100%);
        font-family: 'Quicksand', sans-serif;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #F4ECFF 0%, #E8F4FF 100%);
    }
    
    /* Judul Utama */
    h1, h2, h3 {
        font-family: 'Quicksand', sans-serif;
        color: #6B4C9A;
    }
    
    /* Dekorasi Bintang */
    .decoration-star {
        position: fixed;
        font-size: 24px;
        animation: twinkle 2s infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes twinkle {
        0%, 100% { opacity: 0.5; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.2); }
    }
    
    /* Kotak Unsur */
    .element-card {
        border-radius: 12px;
        padding: 10px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .element-card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    /* Button style */
    .stButton > button {
        border-radius: 12px;
        background: linear-gradient(135deg, #D8B4FE, #B5EAEA);
        border: none;
        color: #333;
        font-weight: 600;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 20px rgba(216, 180, 254, 0.4);
    }
    
    /* Container style */
    .main-content {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 20px;
        padding: 30px;
        margin: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.05);
    }
    
    /* Card style */
    .info-card {
        background: white;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    
    /* Team card */
    .team-card {
        background: linear-gradient(135deg, #FFF6FB, #F3EEFF);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        border: 2px solid #F8C8DC;
        margin: 10px;
    }
    
    /* Emoji decorations */
    .decoration-emoji {
        position: fixed;
        font-size: 30px;
        opacity: 0.3;
        pointer-events: none;
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    
    /* Loading animation */
    .loading-gif {
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
</style>
"""

# ============================================
# 🏠 HALAMAN BERANDA
# ============================================
def show_beranda():
    """Halaman Beranda / Home"""
    
    # CSS Khusus Beranda
    st.markdown("""
    <style>
        .home-title {
            font-size: 48px;
            font-weight: 700;
            text-align: center;
            background: linear-gradient(135deg, #FFB6C1, #D8B4FE, #B5EAEA);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        
        .home-subtitle {
            font-size: 24px;
            text-align: center;
            color: #888;
            margin-bottom: 30px;
        }
        
        .welcome-box {
            background: linear-gradient(135deg, rgba(255,246,251,0.9), rgba(243,238,255,0.9));
            border-radius: 24px;
            padding: 40px;
            margin: 20px 0;
            border: 3px solid #F8C8DC;
        }
        
        .feature-box {
            background: white;
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            box-shadow: 0 8px 30px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
        }
        
        .feature-box:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.12);
        }
        
        .feature-icon {
            font-size: 50px;
            margin-bottom: 15px;
        }
        
        .section-title {
            font-size: 28px;
            color: #6B4C9A;
            margin: 30px 0 20px 0;
            padding-bottom: 10px;
            border-bottom: 3px solid #D8B4FE;
        }
        
        .team-member {
            background: linear-gradient(135deg, #FFF6FB, #EAF8FF);
            border-radius: 16px;
            padding: 20px;
            margin: 10px;
            text-align: center;
            border: 2px solid #BDE0FE;
            transition: all 0.3s ease;
        }
        
        .team-member:hover {
            transform: scale(1.03);
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .decoration-float {
            animation: float 4s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # ============================================
    # JUDUL & SELAMAT DATANG
    # ============================================
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1 class="home-title">🧪 Ensiklopedia Unsur Kimia ✨</h1>
        <p class="home-subtitle">Jelajahi dunia kimia dengan cara yang lucu dan menarik!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dekorasi melayang
    cols = st.columns([1, 4, 1])
    with cols[1]:
        st.markdown("""
        <div style="text-align: center; font-size: 60px;" class="decoration-float">
            🧬 🔬 💖 ✨ 🧪 ☁️
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ============================================
    # DESKRIPSI APLIKASI
    # ============================================
    st.markdown("""
    <div class="welcome-box">
        <h2 style="text-align: center; color: #6B4C9A; margin-bottom: 20px;">
            🌸 Selamat Datang di Ensiklopedia Unsur Kimia 🌸
        </h2>
        
        <p style="font-size: 18px; text-align: center; line-height: 1.8; color: #555;">
            Aplikasi ini adalah <strong>panduan interaktif</strong> untuk mempelajari 
            <strong>tabel periodik unsur</strong> dengan tampilan yang 
            <strong>kawaii dan aesthetic</strong>! 🎀
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ============================================
    # TUJUAN, MANFAAT, FITUR
    # ============================================
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🎯</div>
            <h3>Tujuan</h3>
            <p style="color: #666;">
                🎯 Tujuan Aplikasi
                - Menyediakan informasi unsur-unsur kimia secara lengkap dan mudah dipahami.
                - Membantu mahasiswa, siswa, dan pengguna umum mempelajari tabel periodik unsur secara interaktif.
                - Mempermudah pencarian data unsur kimia seperti nomor atom, massa atom, konfigurasi elektron, sifat fisika, dan sifat kimia.
                - Menjadi media pembelajaran digital yang menarik dan modern dalam bidang kimia.
                - Meningkatkan pemahaman pengguna mengenai karakteristik dan kegunaan berbagai unsur kimia.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">💡</div>
            <h3>Manfaat</h3>
            <p style="color: #666;">
                💡 Manfaat Aplikasi
                - Memudahkan pengguna mengakses informasi unsur kimia dengan cepat dan praktis.
                - Membantu proses pembelajaran kimia secara mandiri maupun di lingkungan pendidikan.
                - Menyajikan data unsur kimia dalam tampilan yang interaktif dan mudah dipahami.
                - Menambah wawasan mengenai sifat, kegunaan, serta aspek keselamatan dari setiap unsur kimia.
                - Mendukung kegiatan belajar, penelitian, dan praktikum yang berkaitan dengan ilmu kimia.
                - Menjadi sumber referensi digital yang dapat diakses kapan saja dan di mana saja.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
