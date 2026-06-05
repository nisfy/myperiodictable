import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Tabel Periodik Interaktif", 
    layout="wide", 
    page_icon="🧪"
)

# --- 2. DATASET UTAMA ---
unsur_data = {
    # GOLONGAN IA
    "H": {"Informasi Dasar": {"Nama": "Hidrogen", "Nomor Atom": 1, "Kategori": "Non-logam", "Massa Atom Relatif": 1.008, "Golongan": "IA", "Periode": 1, "Konfigurasi Elektron": "1s¹", "Tahun Ditemukan": 1766}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif pada suhu tinggi"}, "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "0.08988 g/L"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Asfiksian", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Bahan bakar roket, amonia."},
    "Li": {"Informasi Dasar": {"Nama": "Litium", "Nomor Atom": 3, "Kategori": "Logam Alkali", "Massa Atom Relatif": 6.94, "Golongan": "IA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s¹", "Tahun Ditemukan": 1817}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif, mudah teroksidasi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "0.534 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Korosif pada kulit", "Batas Paparan": "0.025 mg/m³"}, "Kegunaan": "Baterai ion-litium."},
    "Na": {"Informasi Dasar": {"Nama": "Natrium", "Nomor Atom": 11, "Kategori": "Logam Alkali", "Massa Atom Relatif": 22.99, "Golongan": "IA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s¹", "Tahun Ditemukan": 1807}, "Sifat Kimia & Fisik": {"Reaktivitas": "Bereaksi eksplosif dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "0.968 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Luka bakar termal/kimia", "Batas Paparan": "2 mg/m³"}, "Kegunaan": "Garam dapur (NaCl)."},
    "K": {"Informasi Dasar": {"Nama": "Kalium", "Nomor Atom": 19, "Kategori": "Logam Alkali", "Massa Atom Relatif": 39.10, "Golongan": "IA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 4s¹", "Tahun Ditemukan": 1807}, "Sifat Kimia & Fisik": {"Reaktivitas": "Menyala spontan saat kontak air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "0.862 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Luka bakar korosif parah", "Batas Paparan": "2 mg/m³"}, "Kegunaan": "Pupuk (NPK), sabun cair."},
    "Rb": {"Informasi Dasar": {"Nama": "Rubidium", "Nomor Atom": 37, "Kategori": "Logam Alkali", "Massa Atom Relatif": 85.47, "Golongan": "IA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 5s¹", "Tahun Ditemukan": 1861}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat eksplosif dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan", "Massa Jenis": "1.53 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Luka bakar", "Batas Paparan": "Belum ada"}, "Kegunaan": "Jam atom."},
    "Cs": {"Informasi Dasar": {"Nama": "Sesium", "Nomor Atom": 55, "Kategori": "Logam Alkali", "Massa Atom Relatif": 132.91, "Golongan": "IA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 6s¹", "Tahun Ditemukan": 1860}, "Sifat Kimia & Fisik": {"Reaktivitas": "Logam basa paling reaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan-Emas", "Massa Jenis": "1.93 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Luka bakar luar biasa", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Cairan pemboran minyak."},
    "Fr": {"Informasi Dasar": {"Nama": "Fransium", "Nomor Atom": 87, "Kategori": "Logam Alkali", "Massa Atom Relatif": 223, "Golongan": "IA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 7s¹", "Tahun Ditemukan": 1939}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diasumsikan sangat eksplosif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Metalik", "Massa Jenis": "1.87 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi tinggi", "Batas Paparan": "Dilarang terpapar"}, "Kegunaan": "Penelitian medis/nuklir."},
    
    # GOLONGAN IIA
    "Be": {"Informasi Dasar": {"Nama": "Berilium", "Nomor Atom": 4, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 9.012, "Golongan": "IIA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s²", "Tahun Ditemukan": 1798}, "Sifat Kimia & Fisik": {"Reaktivitas": "Reaktivitas rendah"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu baja", "Massa Jenis": "1.85 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi", "Piktogram GHS": "☠️, 🫁", "Bahaya Kesehatan": "Karsinogenik (Beriliosis)", "Batas Paparan": "0.0002 mg/m³"}, "Kegunaan": "Komponen pesawat ruang angkasa."},
    "Mg": {"Informasi Dasar": {"Nama": "Magnesium", "Nomor Atom": 12, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 24.305, "Golongan": "IIA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s²", "Tahun Ditemukan": 1755}, "Sifat Kimia & Fisik": {"Reaktivitas": "Terbakar di udara dengan nyala terang"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu mengkilap", "Massa Jenis": "1.74 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Sangat mudah terbakar", "Batas Paparan": "10 mg/m³"}, "Kegunaan": "Velg mobil/pesawat, kembang api."},
    "Ca": {"Informasi Dasar": {"Nama": "Kalsium", "Nomor Atom": 20, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 40.078, "Golongan": "IIA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 4s²", "Tahun Ditemukan": 1808}, "Sifat Kimia & Fisik": {"Reaktivitas": "Cukup reaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan-putih", "Massa Jenis": "1.55 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Korosif pada kulit lembab", "Batas Paparan": "2 mg/m³"}, "Kegunaan": "Bahan baku semen dan beton."},
    "Sr": {"Informasi Dasar": {"Nama": "Stronsium", "Nomor Atom": 38, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 87.62, "Golongan": "IIA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 5s²", "Tahun Ditemukan": 1790}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif di udara"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "2.64 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Isotop Sr-90 radioaktif", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Pewarna merah pada suar."},
    "Ba": {"Informasi Dasar": {"Nama": "Barium", "Nomor Atom": 56, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 137.33, "Golongan": "IIA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 6s²", "Tahun Ditemukan": 1774}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif, mudah teroksidasi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan", "Massa Jenis": "3.51 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Garam larut sangat beracun", "Batas Paparan": "0.5 mg/m³"}, "Kegunaan": "Cairan pengeboran minyak."},
    "Ra": {"Informasi Dasar": {"Nama": "Radium", "Nomor Atom": 88, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 226, "Golongan": "IIA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 7s²", "Tahun Ditemukan": 1898}, "Sifat Kimia & Fisik": {"Reaktivitas": "Memancarkan radiasi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "5.5 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Kanker tulang", "Batas Paparan": "Sangat ketat"}, "Kegunaan": "Penelitian medis."},

    # LOGAM TRANSISI
    "Sc": {"Informasi Dasar": {"Nama": "Skandium", "Nomor Atom": 21, "Kategori": "Logam Transisi", "Massa Atom Relatif": 44.956, "Golongan": "IIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹ 4s²", "Tahun Ditemukan": 1879}, "Sifat Kimia & Fisik": {"Reaktivitas": "Bereaksi dengan asam"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak", "Massa Jenis": "2.98 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi ringan"}, "Kegunaan": "Komponen sepeda balap."},
    "Ti": {"Informasi Dasar": {"Nama": "Titanium", "Nomor Atom": 22, "Kategori": "Logam Transisi", "Massa Atom Relatif": 47.867, "Golongan": "IVB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d² 4s²", "Tahun Ditemukan": 1791}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi tinggi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak Metalik", "Massa Jenis": "4.506 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Inert"}, "Kegunaan": "Implan medis, bodi pesawat."},
    
    # GAS MULIA & NON LOGAM LAIN
    "He": {"Informasi Dasar": {"Nama": "Helium", "Nomor Atom": 2, "Kategori": "Gas Mulia", "Massa Atom Relatif": 4.0026, "Golongan": "VIIIA", "Periode": 1, "Konfigurasi Elektron": "1s²", "Tahun Ditemukan": 1868}, "Sifat Kimia & Fisik": {"Reaktivitas": "Inert (Tidak reaktif)"}, "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "0.1786 g/L"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tidak beracun", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Asfiksian jika murni"}, "Kegunaan": "Balon gas, pendingin MRI."},
}

# --- 3. SKEMA WARNA PASTEL (Sesuai Gambar Contoh) ---
kategori_warna = {
    "Logam Alkali": "#FFB7B2",        # Pink Lembut
    "Logam Alkali Tanah": "#FFDAC1",  # Oranye Muda
    "Logam Transisi": "#FFF4B2",      # Kuning Pastel
    "Non-logam": "#BFFCC6",           # Hijau Pastel
    "Gas Mulia": "#E8AEFF",           # Ungu Pastel
    "Logam Lainnya": "#C3E6FC",       # Biru Pastel
    "Halogen": "#E5FFCC",             # Hijau Neon Lembut
    "Default": "#F1F3F5"
}

# --- 4. CUSTOM CSS THEME PASTEL KAWAI ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@500;700&display=swap');
    
    /* Background Awan Estetik Pastel */
    .stApp {
        background: linear-gradient(135deg, #FFF5F5 0%, #F5F7FF 50%, #FFF0FA 100%);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #F0E6FF !important;
    }
    
    .main-title {
        font-family: 'Fredoka One', cursive;
        color: #5D536B;
        text-align: center;
        font-size: 45px;
        text-shadow: 2px 2px #FFF;
        margin-top: 10px;
    }
    .subtitle {
        font-family: 'Quicksand', sans-serif;
        color: #7D7495;
        text-align: center;
        font-size: 16px;
        margin-bottom: 25px;
    }
    
    /* Card Beranda */
    .welcome-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 10px 25px rgba(180, 160, 200, 0.15);
        border: 3px solid #FFF;
        font-family: 'Quicksand', sans-serif;
    }
    
    /* Tombol Tabel Unsur */
    div.stButton > button {
        width: 100% !important;
        height: 65px !important;
        font-family: 'Quicksand', sans-serif;
        font-weight: 700;
        font-size: 15px !important;
        border-radius: 12px !important;
        border: 2px solid #FFF !important;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.04);
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        transform: scale(1.1) translateY(-3px);
        box-shadow: 0px 8px 16px rgba(0,0,0,0.08);
    }
</style>
""", unsafe_allow_html=True)


# --- 5. NAVIGASI DI SIDEBAR ---
st.sidebar.markdown("## ✨ Menu Navigasi")
pilihan_halaman = st.sidebar.selectbox(
    "Cari dan Pilih Halaman:",
    ["Beranda (Selamat Datang)", "Tabel Periodik Interaktif"]
)
st.sidebar.write("---")
st.sidebar.caption("© 2026 - Aplikasi Tabel Periodik")


# --- 6. LOGIC PEMISAH HALAMAN (IF-ELSE) ---

# --- HALAMAN 1: BERANDA ---
if pilihan_halaman == "Beranda (Selamat Datang)":
    st.markdown('<div class="main-title">👋 Selamat Datang di Ensiklopedia Unsur Kimia</div>', unsafe_allow_html=True)
    st.write("")
    
    col_beranda_kiri, col_beranda_kanan = st.columns([2, 1])
    
    with col_beranda_kiri:
        st.markdown("""
        <div class="welcome-card">
            <p style="font-size: 18px; color: #4A4A4A;">
                Aplikasi ini adalah <b>Tabel Periodik Interaktif</b> yang dirancang khusus untuk membantu 
                kamu mempelajari berbagai unsur kimia dengan mudah, visual, dan menyenangkan!
            </p>
            <h4 style="color: #6C5CE7; font-family:'Fredoka One';">🚀 Melalui aplikasi ini, Anda dapat mengeksplorasi:</h4>
            <ul style="font-size: 16px; line-height: 1.8;">
                <li>📝 <b>Informasi Dasar</b> (Massa atom, konfigurasi elektron, dll)</li>
                <li>⚡ <b>Sifat Kimia & Fisik</b> (Reaktivitas, kelarutan)</li>
                <li>📦 <b>Wujud Fisik</b> (Massa jenis, wujud pada suhu ruang)</li>
                <li>⚠️ <b>Kesehatan & Keselamatan</b> (Piktogram GHS & Tingkat toksisitas)</li>
                <li>💡 <b>Kegunaan</b> (Aplikasi nyata di industri & laboratorium)</li>
            </ul>
            <br>
            <div style="background-color: #E8F0FE; padding: 15px; border-radius: 12px; border-left: 5px solid #1A73E8;">
                📌 <b>Cara Penggunaan:</b> Silakan buka menu dropdown di sebelah kiri (Sidebar) 
                lalu pilih menu <b>"Tabel Periodik Interaktif"</b> untuk mulai belajar!
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_beranda_kanan:
        # Menampilkan emoji sains berukuran besar sebagai pengganti ikon ilustrasi agar estetik
        st.markdown("<h1 style='text-align: center; font-size: 100px; margin-top:20px;'>🔬</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; font-size: 100px;'>🧪</h1>", unsafe_allow_html=True)


# --- HALAMAN 2: TABEL PERIODIK ---
elif pilihan_halaman == "Tabel Periodik Interaktif":
    st.markdown('<div class="main-title">🧪 Tabel Periodik Unsur Kimia Interaktif</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">✨ Klik pada unsur untuk melihat detail informasi MSDS & Karakteristik di bagian bawah ✨</div>', unsafe_allow_html=True)
    
    # Petunjuk Warna/Legend Kategori
    st.write("### 🏷️ Kategori Golongan:")
    cols_legend = st.columns(6)
    cats = ["Logam Alkali", "Logam Alkali Tanah", "Logam Transisi", "Non-logam", "Gas Mulia", "Logam Lainnya"]
    for i, kat in enumerate(cats):
        with cols_legend[i]:
            st.markdown(f'<div style="background-color:{kategori_warna[kat]}; padding:8px; border-radius:10px; text-align:center; font-weight:bold; color:#333; font-size:13px; border: 1px solid #FFF;">{kat}</div>', unsafe_allow_html=True)
    
    st.write("---")
    
    # State Penampung Klik Unsur
    if "selected_element" not in st.session_state:
        st.session_state.selected_element = "H"
        
    # Fungsi Otomatis Pewarnaan Tombol
    def buat_tombol(simbol, kolom_target):
        if simbol in unsur_data:
            kat = unsur_data[simbol]["Informasi Dasar"]["Kategori"]
            warna = kategori_warna.get(kat, kategori_warna["Default"])
            no_atom = unsur_data[simbol]["Informasi Dasar"]["Nomor Atom"]
            
            with kolom_target:
                st.markdown(f"""
                <style>
                    div:has( > button:contains("{simbol}")) > button {{
                        background-color: {warna} !important;
                        color: #2D3436 !important;
                    }}
                </style>
                """, unsafe_allow_html=True)
                if st.button(f"{no_atom}\n{simbol}", key=f"key_{simbol}"):
                    st.session_state.selected_element = simbol
        else:
            with kolom_target:
                st.button(simbol, key=f"blank_{simbol}", disabled=True)

    # Susunan Grid Tabel Periodik
    # Periode 1
    p1 = st.columns(18)
    buat_tombol("H", p1[0])
    buat_tombol("He", p1[17])
    
    # Periode 2
    p2 = st.columns(18)
    buat_tombol("Li", p2[0])
    buat_tombol("Be", p2[1])
    buat_tombol("B", p2[12])
    buat_tombol("C", p2[13])
    buat_tombol("N", p2[14])
    buat_tombol("O", p2[15])
    buat_tombol("F", p2[16])
    buat_tombol("Ne", p2[17])
    
    # Periode 3
    p3 = st.columns(18)
    buat_tombol("Na", p3[0])
    buat_tombol("Mg", p3[1])
    buat_tombol("Al", p3[12])
    buat_tombol("Si", p3[13])
    buat_tombol("P", p3[14])
    buat_tombol("S", p3[15])
    buat_tombol("Cl", p3[16])
    buat_tombol("Ar", p3[17])
    
    # Periode 4
    p4 = st.columns(18)
    buat_tombol("K", p4[0])
    buat_tombol("Ca", p4[1])
    buat_tombol("Sc", p4[2])
    buat_tombol("Ti", p4[3])

    # --- PANEL DETAIL DI BAWAH TABEL ---
    st.write("---")
    terpilih = st.session_state.selected_element
    
    if terpilih in unsur_data:
        dt = unsur_data[terpilih]
        st.markdown(f"### 🔍 Lembar Data Karakteristik & Keselamatan Unsur: <span style='color:#6C5CE7;'>{dt['Informasi Dasar']['Nama']} ({terpilih})</span>", unsafe_allow_html=True)
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.info("📋 **Informasi Dasar**")
            for k, v in dt["Informasi Dasar"].items():
                st.write(f"**{k}:** {v}")
        with c2:
            st.success("⚡ **Sifat Kimia & Fisik**")
            for k, v in dt["Sifat Kimia & Fisik"].items():
                st.write(f"**{k}:** {v}")
        with c3:
            st.warning("📦 **Wujud Fisik**")
            for k, v in dt["Wujud Fisik"].items():
                st.write(f"**{k}:** {v}")
        with c4:
            st.error("⚠️ **Kesehatan & GHS**")
            for k, v in dt["Kesehatan & Keselamatan"].items():
                st.write(f"**{k}:** {v}")
                
        st.markdown(f"<div style='background-color:#FFF; padding:15px; border-radius:10px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);'>💡 <b>Kegunaan Utama di Laboratorium/Industri:</b> {dt['Kegunaan']}</div>", unsafe_allow_html=True)

