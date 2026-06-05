import streamlit as st

# --- 1. KONFIGURASI HALAMAN (Wajib di bagian paling atas) ---
st.set_page_config(page_title="Tabel Periodik Interaktif", layout="wide", page_icon="🧪")

# --- 2. DATASET LENGKAP MILIKMU (DIPERTAHANKAN 100% TANPA DIKURANGI) ---
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

    # GOLONGAN IIIB (3)
    "Sc": {"Informasi Dasar": {"Nama": "Skandium", "Nomor Atom": 21, "Kategori": "Logam Transisi", "Massa Atom Relatif": 44.956, "Golongan": "IIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹ 4s²", "Tahun Ditemukan": 1879}, "Sifat Kimia & Fisik": {"Reaktivitas": "Bereaksi dengan asam, mudah teroksidasi di udara"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "2.985 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Debu mudah terbakar", "Batas Paparan": "Belum ditetapkan"}, "Kegunaan": "Paduan aluminium untuk kerangka sepeda dan tongkat bisbol."},
    "Y": {"Informasi Dasar": {"Nama": "Itrium", "Nomor Atom": 39, "Kategori": "Logam Transisi", "Massa Atom Relatif": 88.906, "Golongan": "IIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹ 5s²", "Tahun Ditemukan": 1794}, "Sifat Kimia & Fisik": {"Reaktivitas": "Stabil di udara kering, bereaksi dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "4.472 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (debu)", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Penyakit paru-paru akibat inhalasi debu", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Fosfor merah pada layar TV tabung, laser garnet, superkonduktor."},
    
    # GOLONGAN IVB (4)
    "Ti": {"Informasi Dasar": {"Nama": "Titanium", "Nomor Atom": 22, "Kategori": "Logam Transisi", "Massa Atom Relatif": 47.867, "Golongan": "IVB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d² 4s²", "Tahun Ditemukan": 1791}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat tahan korosi (membentuk lapisan oksida pelindung)"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik", "Massa Jenis": "4.506 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Secara biologis inert, sangat aman untuk tubuh", "Batas Paparan": "10 mg/m³ (debu)"}, "Kegunaan": "Implan medis/tulang, bodi pesawat terbang, pigmen putih (TiO2)."},
    "Zr": {"Informasi Dasar": {"Nama": "Zirkonium", "Nomor Atom": 40, "Kategori": "Logam Transisi", "Massa Atom Relatif": 91.224, "Golongan": "IVB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d² 5s²", "Tahun Ditemukan": 1789}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi tinggi, tidak bereaksi dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keputihan", "Massa Jenis": "6.52 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Bubuk halus mudah menyala secara spontan di udara", "Batas Paparan": "5 mg/m³"}, "Kegunaan": "Selongsong bahan bakar reaktor nuklir, permata sintetis (Cubic Zirconia)."},
    "Hf": {"Informasi Dasar": {"Nama": "Hafnium", "Nomor Atom": 72, "Kategori": "Logam Transisi", "Massa Atom Relatif": 178.49, "Golongan": "IVB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d² 6s²", "Tahun Ditemukan": 1923}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat mirip zirkonium, menyerap neutron sangat baik"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu baja", "Massa Jenis": "13.31 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Bubuknya mudah terbakar/eksplosif", "Batas Paparan": "0.5 mg/m³"}, "Kegunaan": "Batang kendali reaktor nuklir, mikroprosesor (chip komputer)."},

    # GOLONGAN VB (5)
    "V": {"Informasi Dasar": {"Nama": "Vanadium", "Nomor Atom": 23, "Kategori": "Logam Transisi", "Massa Atom Relatif": 50.941, "Golongan": "VB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d³ 4s²", "Tahun Ditemukan": 1801}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan terhadap basa, asam sulfat, dan asam klorida"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan muda", "Massa Jenis": "6.11 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (senyawanya)", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Beracun jika terhirup (V2O5)", "Batas Paparan": "0.05 mg/m³"}, "Kegunaan": "Campuran baja tahan karat (perkakas, kunci pas, as roda)."},
    "Nb": {"Informasi Dasar": {"Nama": "Niobium", "Nomor Atom": 41, "Kategori": "Logam Transisi", "Massa Atom Relatif": 92.906, "Golongan": "VB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁴ 5s¹", "Tahun Ditemukan": 1801}, "Sifat Kimia & Fisik": {"Reaktivitas": "Inert pada suhu ruang, mengoksidasi pada suhu tinggi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu metalik", "Massa Jenis": "8.57 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi mata dan kulit (debu)", "Batas Paparan": "Belum ada standar khusus"}, "Kegunaan": "Baja paduan untuk pipa gas, superkonduktor dalam pemindai MRI."},
    "Ta": {"Informasi Dasar": {"Nama": "Tantalum", "Nomor Atom": 73, "Kategori": "Logam Transisi", "Massa Atom Relatif": 180.95, "Golongan": "VB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d³ 6s²", "Tahun Ditemukan": 1802}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat tahan terhadap serangan zat kimia pada suhu di bawah 150°C"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu kebiruan terang", "Massa Jenis": "16.69 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Biokompatibel (tidak bereaksi dengan cairan tubuh)", "Batas Paparan": "5 mg/m³"}, "Kegunaan": "Kapasitor pada ponsel pintar (smartphone), peralatan bedah."},

    # GOLONGAN VIB (6)
    "Cr": {"Informasi Dasar": {"Nama": "Kromium", "Nomor Atom": 24, "Kategori": "Logam Transisi", "Massa Atom Relatif": 51.996, "Golongan": "VIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁵ 4s¹", "Tahun Ditemukan": 1797}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat tahan korosi, tidak bereaksi dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik keras", "Massa Jenis": "7.19 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi (Kromium Heksavalen / Cr VI)", "Piktogram GHS": "☠️, 🫁", "Bahaya Kesehatan": "Cr(VI) sangat karsinogenik dan mematikan. Cr(III) esensial bagi tubuh.", "Batas Paparan": "0.005 mg/m³ (Cr VI)"}, "Kegunaan": "Baja tahan karat (stainless steel), pelapisan krom pelindung kendaraan."},
    "Mo": {"Informasi Dasar": {"Nama": "Molibdenum", "Nomor Atom": 42, "Kategori": "Logam Transisi", "Massa Atom Relatif": 95.95, "Golongan": "VIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁵ 5s¹", "Tahun Ditemukan": 1778}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tidak larut dalam asam klorida dan asam fluorida"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan", "Massa Jenis": "10.28 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Toksisitas rendah, tetapi hindari paparan kronis debunya", "Batas Paparan": "10 mg/m³"}, "Kegunaan": "Filamen listrik, paduan pemanas untuk mesin jet, pupuk tanaman."},
    "W": {"Informasi Dasar": {"Nama": "Tungsten (Wolfram)", "Nomor Atom": 74, "Kategori": "Logam Transisi", "Massa Atom Relatif": 183.84, "Golongan": "VIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁴ 6s²", "Tahun Ditemukan": 1783}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat kuat dan inert; titik lebur tertinggi di antara semua logam"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keabu-abuan", "Massa Jenis": "19.25 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Aman untuk dipegang, tetapi senyawa terlarutnya sedikit beracun", "Batas Paparan": "5 mg/m³"}, "Kegunaan": "Filamen bola lampu pijar, mata bor berat bermaterial Tungsten Carbide."},

    # GOLONGAN VIIB (7)
    "Mn": {"Informasi Dasar": {"Nama": "Mangan", "Nomor Atom": 25, "Kategori": "Logam Transisi", "Massa Atom Relatif": 54.938, "Golongan": "VIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁵ 4s²", "Tahun Ditemukan": 1774}, "Sifat Kimia & Fisik": {"Reaktivitas": "Perlahan teroksidasi di udara, berkarat di air seperti besi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan padat", "Massa Jenis": "7.21 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️, 🫁", "Bahaya Kesehatan": "Inhalasi debu terus-menerus memicu kerusakan saraf pusat (Manganisme).", "Batas Paparan": "0.02 mg/m³"}, "Kegunaan": "Paduan rel kereta api (baja keras), baterai alkaline."},
    "Tc": {"Informasi Dasar": {"Nama": "Teknesium", "Nomor Atom": 43, "Kategori": "Logam Transisi", "Massa Atom Relatif": 98, "Golongan": "VIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁵ 5s²", "Tahun Ditemukan": 1937}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi, larut dalam asam nitrat"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu metalik", "Massa Jenis": "11.5 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Semua isotop bersifat radioaktif", "Batas Paparan": "Ditangani di lab radioisotop"}, "Kegunaan": "Pelacak radiodiagnostik tulang dan alat ukur pemindai medis (Isotop Tc-99m)."},
    "Re": {"Informasi Dasar": {"Nama": "Renum", "Nomor Atom": 75, "Kategori": "Logam Transisi", "Massa Atom Relatif": 186.21, "Golongan": "VIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁵ 6s²", "Tahun Ditemukan": 1925}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi parah, stabil secara mekanik pada suhu ekstrim"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan cerah", "Massa Jenis": "21.02 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Tidak berbahaya dalam wujud aslinya", "Batas Paparan": "Belum ditentukan"}, "Kegunaan": "Superalloy suhu tinggi untuk mesin pesawat tempur jet."},

    # GOLONGAN VIIIB (8, 9, 10)
    "Fe": {"Informasi Dasar": {"Nama": "Besi", "Nomor Atom": 26, "Kategori": "Logam Transisi", "Massa Atom Relatif": 55.845, "Golongan": "VIIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁶ 4s²", "Tahun Ditemukan": "Zaman Kuno"}, "Sifat Kimia & Fisik": {"Reaktivitas": "Mudah berkarat saat terkena kelembapan dan oksigen"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak berkilau keabu-abuan", "Massa Jenis": "7.874 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah (Penting bagi darah)", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Kelebihan zat besi menyebabkan kerusakan hati (Hemokromatosis).", "Batas Paparan": "5 mg/m³ (sebagai asap oksida)"}, "Kegunaan": "Tulang punggung infrastruktur (baja, jembatan, bangunan, hemoglobin darah)."},
    "Ru": {"Informasi Dasar": {"Nama": "Rutenium", "Nomor Atom": 44, "Kategori": "Logam Transisi", "Massa Atom Relatif": 101.07, "Golongan": "VIIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁷ 5s¹", "Tahun Ditemukan": 1844}, "Sifat Kimia & Fisik": {"Reaktivitas": "Inert pada sebagian besar bahan kimia, sangat keras"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih metalik keperakan", "Massa Jenis": "12.45 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (Senyawa)", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Rutenium tetroksida (RuO4) sangat beracun dan menodai kulit.", "Batas Paparan": "Belum ada"}, "Kegunaan": "Kontak listrik tahan aus, ujung pulpen mahal (dicampur platinum/osmium)."},
    "Os": {"Informasi Dasar": {"Nama": "Osmium", "Nomor Atom": 76, "Kategori": "Logam Transisi", "Massa Atom Relatif": 190.23, "Golongan": "VIIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁶ 6s²", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat keras dan rapuh, bereaksi lambat dengan oksigen"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih metalik kebiruan", "Massa Jenis": "22.59 g/cm³ (Unsur paling padat di Bumi)"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi (Oksidanya)", "Piktogram GHS": "☠️, 🫁", "Bahaya Kesehatan": "Osmium tetroksida menguap di udara, menyebabkan kebutaan dan kematian.", "Batas Paparan": "0.002 mg/m³"}, "Kegunaan": "Jarum pemutar piringan hitam, poros instrumen (karena kekerasannya yang ekstrim)."},
    "Co": {"Informasi Dasar": {"Nama": "Kobal", "Nomor Atom": 27, "Kategori": "Logam Transisi", "Massa Atom Relatif": 58.933, "Golongan": "VIIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁷ 4s²", "Tahun Ditemukan": 1735}, "Sifat Kimia & Fisik": {"Reaktivitas": "Feromagnetik, bereaksi pelan dengan udara basah"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak abu-abu mengkilap", "Massa Jenis": "8.90 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️, 🫁", "Bahaya Kesehatan": "Iritan paru-paru dan karsinogen potensial; penting untuk Vitamin B12.", "Batas Paparan": "0.02 mg/m³"}, "Kegunaan": "Baterai Lithium-ion (EV, smartphone), paduan turbin gas suhu tinggi."},
    "Rh": {"Informasi Dasar": {"Nama": "Rodium", "Nomor Atom": 45, "Kategori": "Logam Transisi", "Massa Atom Relatif": 102.91, "Golongan": "VIIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁸ 5s¹", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Salah satu logam mulia paling tidak reaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan, memantulkan cahaya kuat", "Massa Jenis": "12.41 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah (Sebagai logam murni)", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Tidak berbahaya dalam wujud aslinya", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Konverter katalitik mobil (pembersih asap knalpot), perhiasan mahal."},
    "Ir": {"Informasi Dasar": {"Nama": "Iridium", "Nomor Atom": 77, "Kategori": "Logam Transisi", "Massa Atom Relatif": 192.22, "Golongan": "VIIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁷ 6s²", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Logam paling tahan korosi di dunia"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih kekuningan terang", "Massa Jenis": "22.56 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Serbuk iridium bisa menjadi iritan sekunder, bentuk balok sangat aman.", "Batas Paparan": "Belum ditetapkan"}, "Kegunaan": "Busi berperforma tinggi, ujung kompas, standar meteran dan kilogram awal."},
    "Ni": {"Informasi Dasar": {"Nama": "Nikel", "Nomor Atom": 28, "Kategori": "Logam Transisi", "Massa Atom Relatif": 58.693, "Golongan": "VIIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁸ 4s²", "Tahun Ditemukan": 1751}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi tinggi (feromagnetik ringan)"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan sedikit kuning emas", "Massa Jenis": "8.908 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️, 🫁", "Bahaya Kesehatan": "Pemicu alergi kontak tersering pada perhiasan tiruan, debu bersifat karsinogen.", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Baterai rechargable, paduan koin, pelapisan pelindung, baja stainless."},
    "Pd": {"Informasi Dasar": {"Nama": "Paladium", "Nomor Atom": 46, "Kategori": "Logam Transisi", "Massa Atom Relatif": 106.42, "Golongan": "VIIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹⁰", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Mampu menyerap gas hidrogen hingga 900 kali volume dirinya"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan baja", "Massa Jenis": "12.02 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Logam aslinya aman, senyawanya dapat menyebabkan iritasi mata.", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Konverter katalitik pengurang emisi mobil, perhiasan emas putih, elektronik."},
    "Pt": {"Informasi Dasar": {"Nama": "Platina", "Nomor Atom": 78, "Kategori": "Logam Transisi", "Massa Atom Relatif": 195.08, "Golongan": "VIIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁹ 6s¹", "Tahun Ditemukan": 1735}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat lembam (inert), tidak berkarat pada suhu berapa pun"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih metalik", "Massa Jenis": "21.45 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Non-toksik dalam bentuk logam. Beberapa senyawa digunakan sebagai obat kemoterapi.", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Perhiasan elit, obat kemoterapi (Cisplatin), alat pacu jantung."},

    # SUPERBERAT PERIODE 7
    "Rf": {"Informasi Dasar": {"Nama": "Rutherfordium", "Nomor Atom": 104, "Kategori": "Logam Transisi", "Massa Atom Relatif": "267", "Golongan": "IVB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d² 7s²", "Tahun Ditemukan": 1964}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip Hafnium"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Metalik", "Massa Jenis": "23.2 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi tinggi", "Batas Paparan": "N/A"}, "Kegunaan": "Penelitian sains nuklir."},
    "Db": {"Informasi Dasar": {"Nama": "Dubnium", "Nomor Atom": 105, "Kategori": "Logam Transisi", "Massa Atom Relatif": "268", "Golongan": "VB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d³ 7s²", "Tahun Ditemukan": 1967}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip Tantalum"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Metalik", "Massa Jenis": "29.3 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi tinggi", "Batas Paparan": "N/A"}, "Kegunaan": "Penelitian sains murni."},
    "Sg": {"Informasi Dasar": {"Nama": "Seaborgium", "Nomor Atom": 106, "Kategori": "Logam Transisi", "Massa Atom Relatif": "269", "Golongan": "VIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁴ 7s²", "Tahun Ditemukan": 1974}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip Tungsten"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Metalik", "Massa Jenis": "35.0 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi tinggi", "Batas Paparan": "N/A"}, "Kegunaan": "Penelitian ilmiah."},
    "Bh": {"Informasi Dasar": {"Nama": "Bohrium", "Nomor Atom": 107, "Kategori": "Logam Transisi", "Massa Atom Relatif": "270", "Golongan": "VIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁵ 7s²", "Tahun Ditemukan": 1981}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip Renium"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Metalik", "Massa Jenis": "37.1 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi tinggi", "Batas Paparan": "N/A"}, "Kegunaan": "Penelitian ilmiah."},
    "Hs": {"Informasi Dasar": {"Nama": "Hassium", "Nomor Atom": 108, "Kategori": "Logam Transisi", "Massa Atom Relatif": "277", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁶ 7s²", "Tahun Ditemukan": 1984}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diketahui membentuk HsO4"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Metalik", "Massa Jenis": "40.7 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi tinggi", "Batas Paparan": "N/A"}, "Kegunaan": "Penelitian ilmiah murni."},
    "Mt": {"Informasi Dasar": {"Nama": "Meitnerium", "Nomor Atom": 109, "Kategori": "Logam Transisi", "Massa Atom Relatif": "278", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁷ 7s²", "Tahun Ditemukan": 1982}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip Iridium"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Metalik", "Massa Jenis": "37.4 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi tinggi", "Batas Paparan": "N/A"}, "Kegunaan": "Studi fisika nuklir."},
    "Ds": {"Informasi Dasar": {"Nama": "Darmstadtium", "Nomor Atom": 110, "Kategori": "Logam Transisi", "Massa Atom Relatif": "281", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁸ 7s²", "Tahun Ditemukan": 1994}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip Platina"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Metalik", "Massa Jenis": "34.8 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi tinggi", "Batas Paparan": "N/A"}, "Kegunaan": "Studi laboratorium khusus."},

    # BLOK-F (LANTANIDA & AKTINIDA CADANGAN)
    "La": {"Informasi Dasar": {"Nama": "Lantanum", "Nomor Atom": 57, "Kategori": "Lantanida", "Massa Atom Relatif": 138.91, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 5d¹ 6s²", "Tahun Ditemukan": 1839}, "Sifat Kimia & Fisik": {"Reaktivitas": "Cukup reaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "6.16 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi mata", "Batas Paparan": "N/A"}, "Kegunaan": "Kaca lensa kamera optik tinggi."},
    "Ce": {"Informasi Dasar": {"Nama": "Serium", "Nomor Atom": 58, "Kategori": "Lantanida", "Massa Atom Relatif": 140.12, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹ 5d¹ 6s²", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Mudah teroksidasi udara"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu besi", "Massa Jenis": "6.77 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Percikan api jika digores", "Batas Paparan": "N/A"}, "Kegunaan": "Batu korek api gas mekanik."},
    "Pr": {"Informasi Dasar": {"Nama": "Praseodium", "Nomor Atom": 59, "Kategori": "Lantanida", "Massa Atom Relatif": 140.91, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f³ 6s²", "Tahun Ditemukan": 1885}, "Sifat Kimia & Fisik": {"Reaktivitas": "Perlahan korosi di udara"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Kuning kehijauan", "Massa Jenis": "6.77 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi ringan", "Batas Paparan": "N/A"}, "Kegunaan": "Pewarna kuning gelas pelindung las."},
    "Nd": {"Informasi Dasar": {"Nama": "Neodifium", "Nomor Atom": 60, "Kategori": "Lantanida", "Massa Atom Relatif": 144.24, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁴ 6s²", "Tahun Ditemukan": 1885}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat cepat teroksidasi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik muda", "Massa Jenis": "7.01 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi mata", "Batas Paparan": "N/A"}, "Kegunaan": "Magnet Neodymium permanen paling kuat."},
    "Pm": {"Informasi Dasar": {"Nama": "Prometium", "Nomor Atom": 61, "Kategori": "Lantanida", "Massa Atom Relatif": 145, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁵ 6s²", "Tahun Ditemukan": 1945}, "Sifat Kimia & Fisik": {"Reaktivitas": "Radioaktif meluruh"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Metalik memancarkan pendar", "Massa Jenis": "7.26 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi nuklir", "Batas Paparan": "N/A"}, "Kegunaan": "Baterai nuklir ukuran mikro."},
    "Sm": {"Informasi Dasar": {"Nama": "Samarium", "Nomor Atom": 62, "Kategori": "Lantanida", "Massa Atom Relatif": 150.36, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁶ 6s²", "Tahun Ditemukan": 1879}, "Sifat Kimia & Fisik": {"Reaktivitas": "Stabil di udara kering"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "7.52 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi", "Batas Paparan": "N/A"}, "Kegunaan": "Magnet suhu tinggi Samarium-Kobalt."},
    "Eu": {"Informasi Dasar": {"Nama": "Europium", "Nomor Atom": 63, "Kategori": "Lantanida", "Massa Atom Relatif": 151.96, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁷ 6s²", "Tahun Ditemukan": 1901}, "Sifat Kimia & Fisik": {"Reaktivitas": "Paling reaktif di golongan lantanida"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "5.24 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Mudah menyala jika bubuk", "Batas Paparan": "N/A"}, "Kegunaan": "Zat fosfor penanda anti-pemalsuan uang Euro."},
    "Gd": {"Informasi Dasar": {"Nama": "Gadolinium", "Nomor Atom": 64, "Kategori": "Lantanida", "Massa Atom Relatif": 157.25, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁷ 5d¹ 6s²", "Tahun Ditemukan": 1880}, "Sifat Kimia & Fisik": {"Reaktivitas": "Feromagnetik di suhu dingin"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "7.90 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi parah", "Batas Paparan": "N/A"}, "Kegunaan": "Agen kontras visual mesin MRI."},
    "Tb": {"Informasi Dasar": {"Nama": "Terbium", "Nomor Atom": 65, "Kategori": "Lantanida", "Massa Atom Relatif": 158.93, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁹ 6s²", "Tahun Ditemukan": 1843}, "Sifat Kimia & Fisik": {"Reaktivitas": "Cukup stabil"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik", "Massa Jenis": "8.23 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi", "Batas Paparan": "N/A"}, "Kegunaan": "Fosfor hijau layar gawai (smartphone)."},
    "Dy": {"Informasi Dasar": {"Nama": "Disprosium", "Nomor Atom": 66, "Kategori": "Lantanida", "Massa Atom Relatif": 162.50, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁰ 6s²", "Tahun Ditemukan": 1886}, "Sifat Kimia & Fisik": {"Reaktivitas": "Larut cepat dalam asam encer"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "8.54 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi", "Batas Paparan": "N/A"}, "Kegunaan": "Penguat ketahanan magnet EV mobil listrik."},
    "Ho": {"Informasi Dasar": {"Nama": "Holmium", "Nomor Atom": 67, "Kategori": "Lantanida", "Massa Atom Relatif": 164.93, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹¹ 6s²", "Tahun Ditemukan": 1878}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sifat magnetik tertinggi dari semua unsur"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan soft", "Massa Jenis": "8.79 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi", "Batas Paparan": "N/A"}, "Kegunaan": "Pole piece magnet superkonduktor."},
    "Er": {"Informasi Dasar": {"Nama": "Erbium", "Nomor Atom": 68, "Kategori": "Lantanida", "Massa Atom Relatif": 167.26, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹² 6s²", "Tahun Ditemukan": 1843}, "Sifat Kimia & Fisik": {"Reaktivitas": "Teroksidasi lambat"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan berkilau", "Massa Jenis": "9.06 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi", "Batas Paparan": "N/A"}, "Kegunaan": "Penguat sinyal kabel serat optik internet."},
    "Tm": {"Informasi Dasar": {"Nama": "Tulium", "Nomor Atom": 69, "Kategori": "Lantanida", "Massa Atom Relatif": 168.93, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹³ 6s²", "Tahun Ditemukan": 1879}, "Sifat Kimia & Fisik": {"Reaktivitas": "Langka dan mahal"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan", "Massa Jenis": "9.32 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi", "Batas Paparan": "N/A"}, "Kegunaan": "Sumber radiasi mesin X-Ray portabel."},
    "Yb": {"Informasi Dasar": {"Nama": "Iterbium", "Nomor Atom": 70, "Kategori": "Lantanida", "Massa Atom Relatif": 173.05, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 6s²", "Tahun Ditemukan": 1878}, "Sifat Kimia & Fisik": {"Reaktivitas": "Bereaksi lambat dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan mengkilap", "Massa Jenis": "6.90 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi mata dan kulit", "Batas Paparan": "N/A"}, "Kegunaan": "Jam atom dengan tingkat akurasi ekstrem."},
    "Lu": {"Informasi Dasar": {"Nama": "Lutesium", "Nomor Atom": 71, "Kategori": "Lantanida", "Massa Atom Relatif": 174.97, "Golongan": "Blok-f", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d¹ 6s²", "Tahun Ditemukan": 1907}, "Sifat Kimia & Fisik": {"Reaktivitas": "Paling keras di deret lantanida"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan padat", "Massa Jenis": "9.84 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi", "Batas Paparan": "N/A"}, "Kegunaan": "Katalis industri pengolahan minyak bumi."},

    "Ac": {"Informasi Dasar": {"Nama": "Aktinium", "Nomor Atom": 89, "Kategori": "Aktinida", "Massa Atom Relatif": 227, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 6d¹ 7s²", "Tahun Ditemukan": 1899}, "Sifat Kimia & Fisik": {"Reaktivitas": "Radioaktif ekstrem, menyala biru di gelap"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik", "Massa Jenis": "10.07 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Kerusakan jaringan akibat radiasi", "Batas Paparan": "N/A"}, "Kegunaan": "Terapi radiasi kanker medis khusus."},
    "Th": {"Informasi Dasar": {"Nama": "Torium", "Nomor Atom": 90, "Kategori": "Aktinida", "Massa Atom Relatif": 232.04, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 6d² 7s²", "Tahun Ditemukan": 1828}, "Sifat Kimia & Fisik": {"Reaktivitas": "Lemah radioaktif, terbakar jika bubuk"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan-abu teroksidasi hitam", "Massa Jenis": "11.72 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif & Beracun", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Kanker paru-paru jika terhirup", "Batas Paparan": "N/A"}, "Kegunaan": "Kandidat bahan bakar reaktor nuklir masa depan."},
    "Pa": {"Informasi Dasar": {"Nama": "Protaktinium", "Nomor Atom": 91, "Kategori": "Aktinida", "Massa Atom Relatif": 231.04, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f² 6d¹ 7s²", "Tahun Ditemukan": 1913}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat beracun dan radioaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan terang", "Massa Jenis": "15.37 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Toksisitas radiologi fatal", "Batas Paparan": "N/A"}, "Kegunaan": "Penelitian geologi penanggalan sedimen."},
    "U": {"Informasi Dasar": {"Nama": "Uranium", "Nomor Atom": 92, "Kategori": "Aktinida", "Massa Atom Relatif": 238.03, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f³ 6d¹ 7s²", "Tahun Ditemukan": 1789}, "Sifat Kimia & Fisik": {"Reaktivitas": "Logam berat padat dan radioaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik kelabu", "Massa Jenis": "19.05 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi & Radioaktif", "Piktogram GHS": "☢️, ☠️", "Bahaya Kesehatan": "Gagal ginjal kronis & mutasi sel", "Batas Paparan": "0.2 mg/m³"}, "Kegunaan": "Bahan bakar utama PLTN (Pembangkit Listrik Tenaga Nuklir)."},
    "Np": {"Informasi Dasar": {"Nama": "Neptunium", "Nomor Atom": 93, "Kategori": "Aktinida", "Massa Atom Relatif": 237, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f⁴ 6d¹ 7s²", "Tahun Ditemukan": 1940}, "Sifat Kimia & Fisik": {"Reaktivitas": "Reaktif, produk sampingan reaktor uranium"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik", "Massa Jenis": "20.45 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Akumulasi di tulang", "Batas Paparan": "N/A"}, "Kegunaan": "Detektor instrumen neutron dosis tinggi."},
    "Pu": {"Informasi Dasar": {"Nama": "Plutonium", "Nomor Atom": 94, "Kategori": "Aktinida", "Massa Atom Relatif": 244, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f⁶ 7s²", "Tahun Ditemukan": 1940}, "Sifat Kimia & Fisik": {"Reaktivitas": "Dapat memicu reaksi fisi berantai spontan"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan kusam kekuningan", "Massa Jenis": "19.84 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Mematikan", "Piktogram GHS": "☢️, ☠️", "Bahaya Kesehatan": "Sangat karsinogenik sekalipun partikel mikro", "Batas Paparan": "Ketat luar biasa"}, "Kegunaan": "Hulu ledak energi nuklir, generator daya wahana luar angkasa Voyager."},
    "Am": {"Informasi Dasar": {"Nama": "Amerisium", "Nomor Atom": 95, "Kategori": "Aktinida", "Massa Atom Relatif": 243, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f⁷ 7s²", "Tahun Ditemukan": 1944}, "Sifat Kimia & Fisik": {"Reaktivitas": "Logam sintetis buatan manusia"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan berkilau", "Massa Jenis": "13.67 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi alfa internal", "Batas Paparan": "N/A"}, "Kegunaan": "Komponen sensor detektor asap kebakaran rumah."},
    "Cm": {"Informasi Dasar": {"Nama": "Kurium", "Nomor Atom": 96, "Kategori": "Aktinida", "Massa Atom Relatif": 247, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f⁷ 6d¹ 7s²", "Tahun Ditemukan": 1944}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat korosif oleh oksigen"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak mengkilap", "Massa Jenis": "13.51 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif Berat", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Destruksi sumsum tulang", "Batas Paparan": "N/A"}, "Kegunaan": "Sumber partikel alfa misi luar angkasa robot Mars Rover."},
    "Bk": {"Informasi Dasar": {"Nama": "Berkelium", "Nomor Atom": 97, "Kategori": "Aktinida", "Massa Atom Relatif": 247, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f⁹ 7s²", "Tahun Ditemukan": 1949}, "Sifat Kimia & Fisik": {"Reaktivitas": "Larut dalam asam mineral"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik", "Massa Jenis": "14.78 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi sel", "Batas Paparan": "N/A"}, "Kegunaan": "Target sintesis unsur baru superberat."},
    "Cf": {"Informasi Dasar": {"Nama": "Kalifornium", "Nomor Atom": 98, "Kategori": "Aktinida", "Massa Atom Relatif": 251, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁰ 7s²", "Tahun Ditemukan": 1950}, "Sifat Kimia & Fisik": {"Reaktivitas": "Pemancar neutron yang sangat kuat"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik", "Massa Jenis": "15.1 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Berbahaya", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Kerusakan bio-organik masif", "Batas Paparan": "N/A"}, "Kegunaan": "Pemicu awal reaktor nuklir, analisis batubara bumi."},
    "Es": {"Informasi Dasar": {"Nama": "Einsteinium", "Nomor Atom": 99, "Kategori": "Aktinida", "Massa Atom Relatif": 252, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹¹ 7s²", "Tahun Ditemukan": 1952}, "Sifat Kimia & Fisik": {"Reaktivitas": "Pertama kali ditemukan di puing bom hidrogen"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak", "Massa Jenis": "8.84 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi destruktif", "Batas Paparan": "N/A"}, "Kegunaan": "Penelitian murni studi kimia unsur transuranium."},
    "Fm": {"Informasi Dasar": {"Nama": "Fermium", "Nomor Atom": 100, "Kategori": "Aktinida", "Massa Atom Relatif": 257, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹² 7s²", "Tahun Ditemukan": 1952}, "Sifat Kimia & Fisik": {"Reaktivitas": "Hanya diperoleh dalam jumlah mikroskopis"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Prediksi)", "Warna": "Metalik (Prediksi)", "Massa Jenis": "N/A"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi ionisasi", "Batas Paparan": "N/A"}, "Kegunaan": "Penelitian ilmiah terbatas fisika energi tinggi."},
    "Md": {"Informasi Dasar": {"Nama": "Mendelevium", "Nomor Atom": 101, "Kategori": "Aktinida", "Massa Atom Relatif": 258, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹³ 7s²", "Tahun Ditemukan": 1955}, "Sifat Kimia & Fisik": {"Reaktivitas": "Cukup stabil dalam larutan air sebagai Md(II)"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Prediksi)", "Warna": "Metalik (Prediksi)", "Massa Jenis": "N/A"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi", "Batas Paparan": "N/A"}, "Kegunaan": "Penelitian teoretis struktur inti atom."},
    "No": {"Informasi Dasar": {"Nama": "Nobelium", "Nomor Atom": 102, "Kategori": "Aktinida", "Massa Atom Relatif": 259, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 7s²", "Tahun Ditemukan": 1966}, "Sifat Kimia & Fisik": {"Reaktivitas": "Meluruh dengan waktu paruh menit"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Prediksi)", "Warna": "Metalik (Prediksi)", "Massa Jenis": "N/A"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi ekstrem", "Batas Paparan": "N/A"}, "Kegunaan": "Penelitian ilmiah."},
    "Lr": {"Informasi Dasar": {"Nama": "Lawrensium", "Nomor Atom": 103, "Kategori": "Aktinida", "Massa Atom Relatif": 266, "Golongan": "Blok-f", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 7s² 7p¹", "Tahun Ditemukan": 1961}, "Sifat Kimia & Fisik": {"Reaktivitas": "Unsur terakhir di kelompok Aktinida"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Prediksi)", "Warna": "Metalik (Prediksi)", "Massa Jenis": "N/A"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi", "Batas Paparan": "N/A"}, "Kegunaan": "Penelitian ilmiah struktur nukleus."},
}

# --- 3. SKEMA WARNA PASTEL (Sama Persis Seperti Foto Referensi) ---
kategori_warna = {
    "Logam Alkali": "#FFB7B2",         # Pink Muda Lembut
    "Logam Alkali Tanah": "#FFDAC1",   # Jingga Pastel Kental
    "Logam Transisi": "#FFEFFF",       # Kuning Pastel Cerah
    "Lantanida": "#E8AEFF",           # Ungu Pastel Lantanida
    "Aktinida": "#FFC6FF",            # Merah Muda Soft Aktinida
    "Non-logam": "#BFFCC6",            # Hijau Pastel Segar
    "Default": "#ECEFF1"               # Abu-abu Netral untuk Element kosong
}

# --- 4. CUSTOM CSS TEMA AWAN & LABORATORIUM IMUT ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@500;700&display=swap');
    
    /* Global App Background Styling */
    .stApp {{
        background: linear-gradient(135deg, #FDFBFB 0%, #EBEDEE 100%);
    }}
    
    .main-title {{
        font-family: 'Fredoka One', cursive;
        color: #6C5B7B;
        text-align: center;
        font-size: 45px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.05);
        margin-top: 15px;
    }}
    .subtitle {{
        font-family: 'Quicksand', sans-serif;
        color: #99B898;
        text-align: center;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 30px;
    }}
    
    /* Mengubah Desain Semua Tombol Unsur Streamlit */
    div.stButton > button {{
        width: 100% !important;
        height: 60px !important;
        font-family: 'Quicksand', sans-serif;
        font-weight: 700;
        font-size: 14px !important;
        border-radius: 12px !important;
        border: 2px solid #FFF !important;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.04);
        transition: all 0.2s ease-in-out;
        white-space: pre-line;
    }}
    div.stButton > button:hover {{
        transform: scale(1.12);
        box-shadow: 0px 8px 16px rgba(0,0,0,0.08);
        border: 2px solid #6C5B7B !important;
    }}
</style>
""", unsafe_allow_html=True)


# --- 5. NAVIGASI BAR MENU DI SEBELAH KIRI (SIDEBAR ROUTING) ---
st.sidebar.markdown("## 🧭 Navigasi Menu")
menu_terpilih = st.sidebar.selectbox(
    "Silakan pilih halaman untuk dibuka:",
    ["🏠 Beranda (Selamat Datang)", "🧪 Tabel Periodik Interaktif"]
)
st.sidebar.write("---")
st.sidebar.caption("© 2026 - Aplikasi Tabel Periodik Kimia Analisis")


# =========================================================================
# HALAMAN 1: BERANDA (ROUTING SELECTION 1)
# =========================================================================
if menu_terpilih == "🏠 Beranda (Selamat Datang)":
    
    # Judul Beranda yang Menarik & Estetik
    st.markdown('<div class="main-title">👋 Selamat Datang di Ensiklopedia Unsur Kimia</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Media Pembelajaran Interaktif Untuk Menjelajahi Karakteristik Unsur Dunia</div>', unsafe_allow_html=True)
    
    # Layout pembagian visual Beranda menggunakan Kolom
    col_kiri, col_kanan = st.columns([2, 1])
    
    with col_kiri:
        st.markdown(f"""
        <div style="background-color: #FFFFFF; padding: 25px; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.03); font-family: 'Quicksand'; color: #4A4A4A;">
            <p style="font-size: 16px; line-height: 1.6;">
                Aplikasi ini adalah <b>Tabel Periodik Interaktif</b> berdesain pastel modern yang dirancang khusus untuk membantu Anda mempelajari berbagai klasifikasi unsur kimia secara efisien, visual, dan menyenangkan.
            </p>
            <h4 style="color: #6C5B7B; margin-top: 15px;">🧪 Melalui aplikasi ini, Anda dapat mengeksplorasi data komprehensif:</h4>
            <ul style="line-height: 1.8; font-weight: 500;">
                <li>📄 <b>Informasi Dasar:</b> Nomor atom, nomor massa, konfigurasi elektron, tahun penemuan.</li>
                <li>⚡ <b>Sifat Kimia & Fisik:</b> Tingkat reaktivitas dan stabilitas unsur.</li>
                <li>📦 <b>Wujud Fisik:</b> Deteksi warna, massa jenis, bentuk zat pada suhu ruang (25°C).</li>
                <li>⚠️ <b>Kesehatan & Keselamatan (MSDS):</b> Simbol piktogram GHS, bahaya kesehatan, dan batas paparan udara.</li>
                <li>💡 <b>Kegunaan Nyata:</b> Pemanfaatan material unsur dalam industri sains dan kehidupan sehari-hari.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Info Box Cara Penggunaan yang Cantik
        st.info("💡 **Cara Penggunaan:** Silakan buka menu dropdown di sebelah kiri (**Sidebar**) lalu alihkan pilihan Anda ke menu **🧪 Tabel Periodik Interaktif** untuk mulai menjelajahi tabel kimia!")

    with col_kanan:
        # Menampilkan Grafis Laboratorium Sederhana Lewat Emojis yang Menarik
        st.markdown("""
        <div style="background-color: #FFEFFF; border-radius: 15px; padding: 30px; text-align: center; box-shadow: 0px 4px 12px rgba(0,0,0,0.03);">
            <div style="font-size: 70px;">🔬</div>
            <div style="font-size: 60px; margin-top: -20px; margin-left: 40px;">🧪</div>
            <div style="font-size: 50px; margin-top: -30px; margin-right: 50px;">⚛️</div>
            <p style="font-family: 'Fredoka One'; color: #6C5B7B; margin-top: 15px; font-size: 20px;">Analisis Kimia</p>
        </div>
        """, unsafe_allow_html=True)


# =========================================================================
# HALAMAN 2: TABEL PERIODIK INTERAKTIF (ROUTING SELECTION 2)
# =========================================================================
elif menu_terpilih == "🧪 Tabel Periodik Interaktif":
    
    st.markdown('<div class="main-title">🧪 Tabel Periodik Unsur Kimia Interaktif</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">✨ Klik pada tombol unsur (warna dapat diklik) untuk memunculkan lembar data MSDS lengkap di bawah ✨</div>', unsafe_allow_html=True)
    
    # --- PETUNJUK INDIKATOR WARNA KATEGORI (LEGEND) ---
    st.markdown("##### 🏷️ Petunjuk Kelompok Kategori:")
    cols_legend = st.columns(6)
    categories = ["Logam Alkali", "Logam Alkali Tanah", "Logam Transisi", "Lantanida", "Aktinida", "Non-logam"]
    for idx, kat in enumerate(categories):
        with cols_legend[idx]:
            st.markdown(f'<div style="background-color:{kategori_warna[kat]}; padding:8px 5px; border-radius:8px; text-align:center; font-weight:700; font-family:\'Quicksand\'; font-size:13px; color:#4A4A4A; box-shadow: 0px 2px 4px rgba(0,0,0,0.02);">{kat}</div>', unsafe_allow_html=True)
    
    st.write("---")

    # Session State Memory agar data unsur terpilih bertahan di layar saat di-klik
    if "selected_element" not in st.session_state:
        st.session_state.selected_element = "H"

    # Fungsi otomatis menyuntikkan warna kustom pastel ke tombol Streamlit
    def buat_tombol_unsur(simbol, col_container):
        if simbol in unsur_data:
            kat = unsur_data[simbol]["Informasi Dasar"]["Kategori"]
            warna = kategori_warna.get(kat, kategori_warna["Default"])
            nomor_atom = unsur_data[simbol]["Informasi Dasar"]["Nomor Atom"]
            
            with col_container:
                st.markdown(f"""
                <style>
                    div:has( > button:contains("{nomor_atom}\\n{simbol}")) > button {{
                        background-color: {warna} !important;
                        color: #333333 !important;
                    }}
                </style>
                """, unsafe_allow_html=True)
                
                if st.button(f"{nomor_atom}\n{simbol}", key=f"btn_{simbol}"):
                    st.session_state.selected_element = simbol
        else:
            # Mengisi grid kosong di tabel periodik dengan kotak disabilitas
            with col_container:
                st.markdown(f"""
                <style>
                    div:has( > button:contains("{simbol}")) > button {{
                        background-color: #ECEFF1 !important;
                        color: #B0BEC5 !important;
                    }}
                </style>
                """, unsafe_allow_html=True)
                st.button(simbol, key=f"btn_blank_{simbol}", disabled=True)

    # --- MEMBUAT BARIS-BARIS TABEL PERIODIK GRIDS (18 KOLOM STANDAR IUPAC) ---
    
    # Periode 1
    rows1 = st.columns(18)
    buat_tombol_unsur("H", rows1[0])
    for c in range(1, 17):
        st.write("") # Spacer tengah kosong
    buat_tombol_unsur("He", rows1[17])

    # Periode 2
    rows2 = st.columns(18)
    buat_tombol_unsur("Li", rows2[0])
    buat_tombol_unsur("Be", rows2[1])
    for c in range(2, 12):
        st.write("")
    buat_tombol_unsur("B", rows2[12])
    buat_tombol_unsur("C", rows2[13])
    buat_tombol_unsur("N", rows2[14])
    buat_tombol_unsur("O", rows2[15])
    buat_tombol_unsur("F", rows2[16])
    buat_tombol_unsur("Ne", rows2[17])

    # Periode 3
    rows3 = st.columns(18)
    buat_tombol_unsur("Na", rows3[0])
    buat_tombol_unsur("Mg", rows3[1])
    for c in range(2, 12):
        st.write("")
    buat_tombol_unsur("Al", rows3[12])
    buat_tombol_unsur("Si", rows3[13])
    buat_tombol_unsur("P", rows3[14])
    buat_tombol_unsur("S", rows3[15])
    buat_tombol_unsur("Cl", rows3[16])
    buat_tombol_unsur("Ar", rows3[17])

    # Periode 4
    rows4 = st.columns(18)
    buat_tombol_unsur("K", rows4[0])
    buat_tombol_unsur("Ca", rows4[1])
    buat_tombol_unsur("Sc", rows4[2])
    buat_tombol_unsur("Ti", rows4[3])
    buat_tombol_unsur("V", rows4[4])
    buat_tombol_unsur("Cr", rows4[5])
    buat_tombol_unsur("Mn", rows4[6])
    buat_tombol_unsur("Fe", rows4[7])
    buat_tombol_unsur("Co", rows4[8])
    buat_tombol_unsur("Ni", rows4[9])
    buat_tombol_unsur("Cu", rows4[10])
    buat_tombol_unsur("Zn", rows4[11])
    buat_tombol_unsur("Ga", rows4[12])
    buat_tombol_unsur("Ge", rows4[13])
    buat_tombol_unsur("As", rows4[14])
    buat_tombol_unsur("Se", rows4[15])
    buat_tombol_unsur("Br", rows4[16])
    buat_tombol_unsur("Kr", rows4[17])

    # Periode 5
    rows5 = st.columns(18)
    buat_tombol_unsur("Rb", rows5[0])
    buat_tombol_unsur("Sr", rows5[1])
    buat_tombol_unsur("Y", rows5[2])
    buat_tombol_unsur("Zr", rows5[3])
    buat_tombol_unsur("Nb", rows5[4])
    buat_tombol_unsur("Mo", rows5[5])
    buat_tombol_unsur("Tc", rows5[6])
    buat_tombol_unsur("Ru", rows5[7])
    buat_tombol_unsur("Rh", rows5[8])
    buat_tombol_unsur("Pd", rows5[9])
    buat_tombol_unsur("Ag", rows5[10])
    buat_tombol_unsur("Cd", rows5[11])
    buat_tombol_unsur("In", rows5[12])
    buat_tombol_unsur("Sn", rows5[13])
    buat_tombol_unsur("Sb", rows5[14])
    buat_tombol_unsur("Te", rows5[15])
    buat_tombol_unsur("I", rows5[16])
    buat_tombol_unsur("Xe", rows5[17])

    # Periode 6
    rows6 = st.columns(18)
    buat_tombol_unsur("Cs", rows6[0])
    buat_tombol_unsur("Ba", rows6[1])
    buat_tombol_unsur("*", rows6[2]) # Tanda Blok Lantanida
    buat_tombol_unsur("Hf", rows6[3])
    buat_tombol_unsur("Ta", rows6[4])
    buat_tombol_unsur("W", rows6[5])
    buat_tombol_unsur("Re", rows6[6])
    buat_tombol_unsur("Os", rows6[7])
    buat_tombol_unsur("Ir", rows6[8])
    buat_tombol_unsur("Pt", rows6[9])
    buat_tombol_unsur("Au", rows6[10])
    buat_tombol_unsur("Hg", rows6[11])
    buat_tombol_unsur("Tl", rows6[12])
    buat_tombol_unsur("Pb", rows6[13])
    buat_tombol_unsur("Bi", rows6[14])
    buat_tombol_unsur("Po", rows6[15])
    buat_tombol_unsur("At", rows6[16])
    buat_tombol_unsur("Rn", rows6[17])

    # Periode 7
    rows7 = st.columns(18)
    buat_tombol_unsur("Fr", rows7[0])
    buat_tombol_unsur("Ra", rows7[1])
    buat_tombol_unsur("**", rows7[2]) # Tanda Blok Aktinida
    buat_tombol_unsur("Rf", rows7[3])
    buat_tombol_unsur("Db", rows7[4])
    buat_tombol_unsur("Sg", rows7[5])
    buat_tombol_unsur("Bh", rows7[6])
    buat_tombol_unsur("Hs", rows7[7])
    buat_tombol_unsur("Mt", rows7[8])
    buat_tombol_unsur("Ds", rows7[9])
    buat_tombol_unsur("Rg", rows7[10])
    buat_tombol_unsur("Cn", rows7[11])
    buat_tombol_unsur("Nh", rows7[12])
    buat_tombol_unsur("Fl", rows7[13])
    buat_tombol_unsur("Mc", rows7[14])
    buat_tombol_unsur("Lv", rows7[15])
    buat_tombol_unsur("Ts", rows7[16])
    buat_tombol_unsur("Og", rows7[17])

    # BARIS TERPISAH: BLOK-F (Lantanida & Aktinida)
    st.write("")
    st.markdown("⚙️ **Blok-f (Deret Lantanida & Aktinida)**")
    
    # Deret Lantanida (Periode 6 Luar)
    row_lantanida = st.columns(18)
    st.markdown("<style>div:has(> button:contains('La')) > button { font-size:12px!important; }</style>", unsafe_allow_html=True)
    # Kosongkan 2 Kolom pertama agar lurus secara visual sesuai estetika tabel periodik
    for idx, el in enumerate(["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]):
        buat_tombol_unsur(el, row_lantanida[idx + 2])
        
    # Deret Aktinida (Periode 7 Luar)
    row_aktinida = st.columns(18)
    for idx, el in enumerate(["Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]):
        buat_tombol_unsur(el, row_aktinida[idx + 2])


    # --- 6. CONTAINER TAMPILAN LEMBAR DATA UNSUR YANG DIKLIK ---
    st.write("---")
    terpilih = st.session_state.selected_element

    if terpilih in unsur_data:
        data = unsur_data[terpilih]
        st.markdown(f"### 🔍 Lembar Data Karakteristik Unsur: **{data['Informasi Dasar']['Nama']} ({terpilih})**")
        
        # Grid Pembagian 4 Kelompok Informasi Khusus Kimia Analisis
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            st.markdown("""<div style='background-color:#E8F0FE; padding:12px; border-radius:10px; font-weight:700; color:#1A73E8; margin-bottom:10px;'>📋 Informasi Dasar</div>""", unsafe_allow_html=True)
            for k, v in data["Informasi Dasar"].items():
                st.write(f"🔹 **{k}:** {v}")
                
        with c2:
            st.markdown("""<div style='background-color:#E6F4EA; padding:12px; border-radius:10px; font-weight:700; color:#137333; margin-bottom:10px;'>⚡ Sifat Kimia & Fisik</div>""", unsafe_allow_html=True)
            for k, v in data["Sifat Kimia & Fisik"].items():
                st.write(f"🍀 **{k}:** {v}")
                
        with c3:
            st.markdown("""<div style='background-color:#FEF7E0; padding:12px; border-radius:10px; font-weight:700; color:#B06000; margin-bottom:10px;'>📦 Wujud Fisik (Suhu Kamar)</div>""", unsafe_allow_html=True)
            for k, v in data["Wujud Fisik"].items():
                st.write(f"🔸 **{k}:** {v}")
                
        with c4:
            st.markdown("""<div style='background-color:#FCE8E6; padding:12px; border-radius:10px; font-weight:700; color:#C5221F; margin-bottom:10px;'>⚠️ Kesehatan & Keselamatan</div>""", unsafe_allow_html=True)
            for k, v in data["Kesehatan & Keselamatan"].items():
                st.write(f"🛑 **{k}:** {v}")
        
        st.markdown(f"""
        <div style="background-color: #F8F9FA; border-left: 5px solid #6C5B7B; padding: 15px; border-radius: 4px; margin-top: 15px; font-family: 'Quicksand';">
            💡 <b>Aplikasi / Kegunaan Utama:</b> {data['Kegunaan']}
        </div>
        """, unsafe_allow_html=True)
