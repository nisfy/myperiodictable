import streamlit as st

# 1. Konfigurasi Halaman (Wajib di bagian paling atas)
st.set_page_config(page_title="Beranda - Tabel Periodik", layout="wide", page_icon="🏠")

# 2. Custom CSS untuk Warna dan Font Estetik (Tema Pastel)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@500;700&display=swap');
    
    /* Warna Background Aplikasi */
    .stApp {
        background: linear-gradient(135deg, #FDFBFB 0%, #EBEDEE 100%);
    }
    
    /* Desain Judul Utama */
    .main-title {
        font-family: 'Fredoka One', cursive;
        color: #6C5B7B;
        text-align: center;
        font-size: 45px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.05);
        margin-top: 20px;
    }
    
    /* Desain Subjudul */
    .subtitle {
        font-family: 'Quicksand', sans-serif;
        color: #99B898;
        text-align: center;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 30px;
    }
    
    /* Box Konten Kiri */
    .content-box {
        background-color: #FFFFFF; 
        padding: 25px; 
        border-radius: 15px; 
        box-shadow: 0px 4px 12px rgba(0,0,0,0.03); 
        font-family: 'Quicksand'; 
        color: #4A4A4A;
    }
    
    /* Box Visual Kanan */
    .visual-box {
        background-color: #FFEFFF; 
        border-radius: 15px; 
        padding: 35px; 
        text-align: center; 
        box-shadow: 0px 4px 12px rgba(0,0,0,0.03);
    }
</style>
""", unsafe_allow_html=True)

# 3. Tampilan Elemen Judul di Beranda
st.markdown('<div class="main-title">👋 Selamat Datang di Ensiklopedia Unsur Kimia</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Media Pembelajaran Interaktif untuk Menjelajahi Karakteristik Unsur Dunia</div>', unsafe_allow_html=True)

# 4. Pembagian Grid Layout Menggunakan Kolom (Rasio 2:1)
col_kiri, col_kanan = st.columns([2, 1])

with col_kiri:
    st.markdown("""
    <div class="content-box">
        <p style="font-size: 16px; line-height: 1.6;">
            Aplikasi ini adalah <b>Tabel Periodik Interaktif</b> berdesain pastel modern yang dirancang khusus untuk membantu Anda mempelajari berbagai klasifikasi unsur kimia secara efisien, visual, dan menyenangkan.
        </p>
        <h4 style="color: #6C5B7B; margin-top: 15px;">🧪 Melalui aplikasi ini, Anda dapat mengeksplorasi data komprehensif:</h4>
        <ul style="line-height: 1.8; font-weight: 500; font-size: 15px;">
            <li>📄 <b>Informasi Dasar:</b> Nomor atom, nomor massa, konfigurasi elektron, dan tahun penemuan unsur.</li>
            <li>⚡ <b>Sifat Kimia & Fisik:</b> Karakteristik tingkat reaktivitas dan stabilitas unsur.</li>
            <li>📦 <b>Wujud Fisik:</b> Deteksi warna, massa jenis, dan bentuk zat pada suhu ruang (25°C).</li>
            <li>⚠️ <b>Kesehatan & Keselamatan (MSDS):</b> Simbol piktogram GHS, bahaya kesehatan, dan batas paparan udara.</li>
            <li>💡 <b>Kegunaan Nyata:</b> Pemanfaatan material unsur dalam industri sains dan kehidupan sehari-hari.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Jarak spacer
    # Kotak Info Petunjuk yang Eye-Catching
    st.info("💡 **Petunjuk Penggunaan:** Gunakan menu navigasi di bar samping (**Sidebar**) untuk beralih halaman dan mulai menjelajahi tabel periodik!")

with col_kanan:
    # Grafis Mini Laboratorium Menggunakan Kombinasi Emoji yang Lucu
    st.markdown("""
    <div class="visual-box">
        <div style="font-size: 75px; animation: float 3s ease-in-out infinite;">🔬</div>
        <div style="font-size: 65px; margin-top: -20px; margin-left: 45px;">🧪</div>
        <div style="font-size: 55px; margin-top: -30px; margin-right: 55px;">⚛️</div>
        <p style="font-family: 'Fredoka One'; color: #6C5B7B; margin-top: 20px; font-size: 22px; letter-spacing: 1px;">ANALISIS KIMIA</p>
        <hr style="border: 0; height: 1px; background: #6C5B7B; opacity: 0.2; margin: 15px 0;">
        <p style="font-family: 'Quicksand'; font-weight: 700; color: #A8A7A7; font-size: 13px;">COHORT AKA '25</p>
    </div>
    """, unsafe_allow_html=True)
