import streamlit as st
import pandas as pd

# ============ KONFIGURASI HALAMAN ============
st.set_page_config(
    page_title="Tabel Periodik Interaktif - Kelompok 13",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============ CSS KAWAII PASTEL ============
st.markdown("""
<style>
    /* Background & Font */
    body {
        background: linear-gradient(135deg, #ffeef8 0%, #e8f4f8 50%, #f0e8f8 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #ffeef8 0%, #e8f4f8 50%, #f0e8f8 100%);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fff5f9 0%, #f0e8f8 100%);
        border-right: 3px solid #ffb6d9;
    }
    
    /* Judul Utama */
    .main-title {
        text-align: center;
        font-size: 3.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #ff6b9d 0%, #c44569 50%, #9d4edd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 2px 2px 4px rgba(255,107,157,0.1);
        margin: 20px 0;
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 1.3rem;
        color: #7209b7;
        font-weight: 500;
        margin-bottom: 30px;
    }
    
    /* Info Box */
    .info-box {
        background: rgba(255, 182, 217, 0.15);
        border: 2px solid #ffb6d9;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(255, 107, 157, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# ========== DATA KATEGORI WARNA PASTEL ===========
COLOR_MAP = {
    "Logam Alkali": "#FFB6C1",
    "Logam Alkali Tanah": "#FFD6A5",
    "Logam Transisi": "#FFF3B0",
    "Logam Transisi (Superberat)": "#FFF3B0",
    "Logam Pasca-Transisi": "#CDEAC0",
    "Logam Pasca-Transisi (Superberat)": "#CDEAC0",
    "Metaloid": "#B5EAEA",
    "Non-logam": "#BDE0FE",
    "Non-logam (Halogen)": "#D8B4FE",
    "Gas Mulia": "#F8C8DC",
    "Lantanida": "#DCC6FF",
    "Aktinida": "#F4C2E7"
}

# ============ SIDEBAR NAVIGASI ============
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 20px; background: linear-gradient(135deg, #ffb6d9, #d4a5ff); border-radius: 15px; margin-bottom: 20px;">
        <h1 style="color: white; margin: 0; font-size: 2em;">⚛️ TABEL PERIODIK</h1>
        <p style="color: white; margin: 5px 0 0 0; font-size: 0.9em;">Kelompok 13</p>
    </div>
    """, unsafe_allow_html=True)

    if "halaman" in st.query_params:
        if st.query_params["halaman"] == "Tabel":
            st.session_state.halaman = "🔬 Tabel Periodik"
    
    if "halaman" not in st.session_state:
        st.session_state.halaman = "🏠 Beranda"

    halaman_options = ["🏠 Beranda", "🔬 Tabel Periodik", "👥 Profil Tim"]
    halaman_index = halaman_options.index(st.session_state.halaman) if st.session_state.halaman in halaman_options else 0
    
    halaman = st.radio(
        "📑 Pilih Halaman:",
        halaman_options,
        index=halaman_index,
        label_visibility="collapsed"
    )

    st.session_state.halaman = halaman

    with st.expander("👥 Anggota Kelompok", expanded=True):
        anggota = [
            {"nama": "Hayu Raihanun", "nim": "2560641"},
            {"nama": "Niken Sri Utari", "nim": "2560727"},
            {"nama": "Nisfy Sabrina Flowerridha S", "nim": "2560728"},
            {"nama": "Raifan Syahdan Putra R", "nim": "2560742"}
        ]

        for member in anggota:
            st.markdown(f"**{member['nama']}**  \n`{member['nim']}`")

    st.divider()
    st.caption("© 2024 Kelompok 13 | Politeknik AKA Bogor")

# ============ CONDITIONAL RENDERING HALAMAN ============
if halaman == "🏠 Beranda":
    st.markdown('<p class="main-title">⚛️ Tabel Periodik Interaktif</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Jelajahi Unsur Kimia Dengan Mudah & Menyenangkan ✨</p>', unsafe_allow_html=True)

    
    st.markdown("""
    <div class="info-box">
    
    ### 🎯 Selamat Datang!
    
    Aplikasi **Tabel Periodik Interaktif** ini dirancang khusus untuk membantu pelajar, guru, dan peneliti dalam mempelajari unsur-unsur kimia dengan cara yang menyenangkan dan interaktif!
    
    #### 📊 Fitur Unggulan:
    - ✨ **118 Unsur Lengkap**
    - 📋 **5 Tab Informasi** - Data komprehensif setiap unsur
    - 🎨 **Desain Kawaii Pastel** - User experience yang menyenangkan
    - 🔍 **Tabel Interaktif** - Klik unsur untuk detail lengkap
    - 🧪 **Kategori Unsur** - Logam, Non-logam, Metaloid, Gas Mulia, dll
    
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Total Unsur", "118", "+4 Superberat")
    with col2:
        st.metric("🧪 Kategori", "7 Jenis", "Logam, Non-logam, Gas Mulia")
    with col3:
        st.metric("📚 Tab Info", "5 Detail Unsur", "Informasi Lengkap")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ffb6d9, #d4a5ff); border-radius: 15px; padding: 25px; text-align: center; color: white; margin: 20px 0;">
        <h3 style="margin-top: 0;">🚀 Mulai Penjelajahan Anda Sekarang!</h3>
        <p>Pilih <b>"🔬 Tabel Periodik"</b> di sidebar untuk melihat grid interaktif tabel periodik lengkap.</p>
    </div>
    """, unsafe_allow_html=True)

elif halaman == "👥 Profil Tim":
    st.markdown('<p class="main-title">👥 Profil Tim Kelompok 13</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Anggota Tim Proyek Tabel Periodik Interaktif</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    tim = [
        {"nama": "Hayu Raihanun", "nim": "2560641"},
        {"nama": "Niken Sri Uttari", "nim": "2560727"},
        {"nama": "Nisfy Sabrina Flowerridha Supriyadi", "nim": "2560728"},
        {"nama": "Raifan Syahdan Putra Raya", "nim": "2560742"}
    ]
    
    for i, member in enumerate(tim):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #fff5f9, #f0e8f8); border: 2px solid #ffb6d9; border-radius: 10px; padding: 20px; margin: 10px 0;">
                <h3 style="color: #ff6b9d; margin-top: 0;">{member['nama']}</h3>
                <p style="color: #7209b7; font-weight: bold; margin: 5px 0;">NIM: {member['nim']}</p>
            </div>
            """, unsafe_allow_html=True)

else:  # Halaman Tabel Periodik
    st.markdown('<p class="main-title">🔬 Tabel Periodik Unsur Kimia</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Klik pada unsur untuk melihat detail lengkap</p>', unsafe_allow_html=True)

    st.markdown("#### 🎨 Petunjuk Kategori Unsur:")
    legend_cols = st.columns(6)
    categories = list(COLOR_MAP.keys())

    for idx, cat in enumerate(categories):
        col_idx = idx % 5
        with legend_cols[col_idx]:
            st.markdown(
                f'<div style="background-color:{COLOR_MAP[cat]}; padding:6px; border-radius:8px; text-align:center; '
                f'font-size:0.8rem; font-weight:bold; color:#4A3E56; margin-bottom:5px; border: 1px solid rgba(0,0,0,0.05);">'
                f'{cat}</div>', 
                unsafe_allow_html=True
            )
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # DATASET MINIMAL
    unsur_data = {
        "H": {"Informasi Dasar": {"Nama": "Hidrogen", "Nomor Atom": 1, "Kategori": "Non-logam"}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Gas"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah"}, "Kegunaan": "Bahan bakar roket."},
        "He": {"Informasi Dasar": {"Nama": "Helium", "Nomor Atom": 2, "Kategori": "Gas Mulia"}, "Sifat Kimia & Fisik": {"Reaktivitas": "Inert"}, "Wujud Fisik": {"Wujud (25°C)": "Gas"}, "Kesehatan & Keselamatan": {"Toksisitas": "Non-toksik"}, "Kegunaan": "Pengisi balon."},
        "Li": {"Informasi Dasar": {"Nama": "Litium", "Nomor Atom": 3, "Kategori": "Logam Alkali"}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang"}, "Kegunaan": "Baterai ion-litium."},
    }
    
    st.title("Tabel Periodik Unsur Kimia Interaktif ⚛️")
    st.write("Klik pada unsur untuk melihat detailnya.")

    if "element" in st.query_params:
        st.session_state.unsur_terpilih = st.query_params["element"]
    elif 'unsur_terpilih' not in st.session_state:
        st.session_state.unsur_terpilih = 'H'

    # TABEL PERIODIK SIMPLE (Hanya periode 1-3 untuk demo)
    grid_tabel = [
        ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
        ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
    ]

    for baris in grid_tabel:
        kolom = st.columns(18, gap="small")

        for i, unsur in enumerate(baris):
            with kolom[i]:
                if unsur != "":
                    if unsur in unsur_data:
                        data_unsur = unsur_data[unsur]
                        kategori_unsur = data_unsur["Informasi Dasar"].get("Kategori", "")
                        warna_bg = COLOR_MAP.get(kategori_unsur, "#FFFFFF")

                        st.markdown(
                            f"""
                            <a href="?halaman=Tabel&element={unsur}" target="_self" style="text-decoration:none; display:block;">
                                <div style="
                                    background-color:{warna_bg};
                                    border-radius:8px;
                                    padding:0;
                                    text-align:center;
                                    height:95px;
                                    width:100%;
                                    display:flex;
                                    flex-direction:column;
                                    justify-content:center;
                                    align-items:center;
                                    cursor:pointer;
                                    border:2px solid rgba(0,0,0,0.05);
                                    box-sizing:border-box;
                                    box-shadow:0 2px 5px rgba(0,0,0,0.08);
                                    overflow:hidden;
                                ">
                                    <h3 style="margin:3px 0; padding:0 4px; font-size:1.3rem; font-weight:bold; color:#333; line-height:1.1; white-space:nowrap; text-overflow:ellipsis; overflow:hidden; width:100%;">{unsur}</h3>
                                    <p style="margin:1px 0; padding:0 4px; font-size:0.65rem; color:rgba(0,0,0,0.65); line-height:1; white-space:nowrap;">{data_unsur['Informasi Dasar']['Nomor Atom']}</p>
                                </div>
                            </a>
                            """,
                            unsafe_allow_html=True
                        )
                else:
                    st.markdown(
                        f"""
                        <div style="
                            background-color:transparent;
                            height:95px;
                            width:100%;
                            box-sizing:border-box;
                        ">
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
    
    st.markdown("---")
    
    if st.session_state.unsur_terpilih in unsur_data:
        unsur_aktif = unsur_data[st.session_state.unsur_terpilih]
    
        st.header(f"🔎 Detail Unsur: {unsur_aktif['Informasi Dasar']['Nama']} ({st.session_state.unsur_terpilih})")
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "Informasi Dasar", "Sifat Kimia & Fisik", "Wujud Fisik", "Kesehatan & Keselamatan", "Kegunaan"
        ])
    
        with tab1:
            df_dasar = pd.DataFrame(list(unsur_aktif["Informasi Dasar"].items()), columns=["Properti", "Nilai"])
            st.dataframe(df_dasar, hide_index=True, use_container_width=True)

        with tab2:
            for key, value in unsur_aktif["Sifat Kimia & Fisik"].items():
                st.markdown(f"**{key}:** {value}")

        with tab3:
            for key, value in unsur_aktif["Wujud Fisik"].items():
                st.markdown(f"**{key}:** {value}")

        with tab4:
            for key, value in unsur_aktif["Kesehatan & Keselamatan"].items():
                st.markdown(f"**{key}:** {value}")

        with tab5:
            st.success(unsur_aktif.get("Kegunaan", "Belum ada data kegunaan."))
