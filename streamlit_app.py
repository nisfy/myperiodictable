import streamlit as st
import pandas as pd

# Konfigurasi Halaman (Lebar Penuh agar tabel muat)
st.set_page_config(page_title="Tabel Periodik Interaktif", layout="wide", page_icon="🧪")

# --- DATASET (GOLONGAN IA, IIA, s.d TRANSISI SUPERBERAT) ---
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

    # GOLONGAN IIIB
    "Sc": {"Informasi Dasar": {"Nama": "Skandium", "Nomor Atom": 21, "Kategori": "Logam Transisi", "Massa Atom Relatif": 44.956, "Golongan": "IIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹ 4s²", "Tahun Ditemukan": 1879}, "Sifat Kimia & Fisik": {"Reaktivitas": "Bereaksi dengan asam, mudah teroksidasi di udara"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "2.985 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Debu mudah terbakar", "Batas Paparan": "Belum ditetapkan"}, "Kegunaan": "Paduan aluminium untuk kerangka sepeda."},
    "Y": {"Informasi Dasar": {"Nama": "Itrium", "Nomor Atom": 39, "Kategori": "Logam Transisi", "Massa Atom Relatif": 88.906, "Golongan": "IIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹ 5s²", "Tahun Ditemukan": 1794}, "Sifat Kimia & Fisik": {"Reaktivitas": "Stabil di udara kering, bereaksi dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "4.472 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (debu)", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Penyakit paru-paru akibat inhalasi debu", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Fosfor merah pada layar TV tabung, laser."},
    
    # GOLONGAN IVB
    "Ti": {"Informasi Dasar": {"Nama": "Titanium", "Nomor Atom": 22, "Kategori": "Logam Transisi", "Massa Atom Relatif": 47.867, "Golongan": "IVB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d² 4s²", "Tahun Ditemukan": 1791}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat tahan korosi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik", "Massa Jenis": "4.506 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Secara biologis inert", "Batas Paparan": "10 mg/m³"}, "Kegunaan": "Implan medis, bodi pesawat."},
    "Zr": {"Informasi Dasar": {"Nama": "Zirkonium", "Nomor Atom": 40, "Kategori": "Logam Transisi", "Massa Atom Relatif": 91.224, "Golongan": "IVB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d² 5s²", "Tahun Ditemukan": 1789}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi tinggi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keputihan", "Massa Jenis": "6.52 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Bubuk halus mudah menyala", "Batas Paparan": "5 mg/m³"}, "Kegunaan": "Selongsong bahan bakar nuklir."},
    "Hf": {"Informasi Dasar": {"Nama": "Hafnium", "Nomor Atom": 72, "Kategori": "Logam Transisi", "Massa Atom Relatif": 178.49, "Golongan": "IVB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d² 6s²", "Tahun Ditemukan": 1923}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat mirip zirkonium"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu baja", "Massa Jenis": "13.31 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Bubuknya mudah terbakar", "Batas Paparan": "0.5 mg/m³"}, "Kegunaan": "Batang kendali reaktor nuklir."},

    # GOLONGAN VB
    "V": {"Informasi Dasar": {"Nama": "Vanadium", "Nomor Atom": 23, "Kategori": "Logam Transisi", "Massa Atom Relatif": 50.941, "Golongan": "VB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d³ 4s²", "Tahun Ditemukan": 1801}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan asam klorida dan basa"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan", "Massa Jenis": "6.11 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Beracun jika terhirup", "Batas Paparan": "0.05 mg/m³"}, "Kegunaan": "Campuran baja tahan karat."},
    "Nb": {"Informasi Dasar": {"Nama": "Niobium", "Nomor Atom": 41, "Kategori": "Logam Transisi", "Massa Atom Relatif": 92.906, "Golongan": "VB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁴ 5s¹", "Tahun Ditemukan": 1801}, "Sifat Kimia & Fisik": {"Reaktivitas": "Inert pada suhu ruang"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu metalik", "Massa Jenis": "8.57 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi mata dan kulit", "Batas Paparan": "Belum ada"}, "Kegunaan": "Baja paduan pipa gas, MRI."},
    "Ta": {"Informasi Dasar": {"Nama": "Tantalum", "Nomor Atom": 73, "Kategori": "Logam Transisi", "Massa Atom Relatif": 180.95, "Golongan": "VB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d³ 6s²", "Tahun Ditemukan": 1802}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat tahan serangan kimia"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu kebiruan", "Massa Jenis": "16.69 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Biokompatibel dengan tubuh", "Batas Paparan": "5 mg/m³"}, "Kegunaan": "Kapasitor smartphone, alat bedah."},

    # GOLONGAN VIB
    "Cr": {"Informasi Dasar": {"Nama": "Kromium", "Nomor Atom": 24, "Kategori": "Logam Transisi", "Massa Atom Relatif": 51.996, "Golongan": "VIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁵ 4s¹", "Tahun Ditemukan": 1797}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat tahan korosi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik", "Massa Jenis": "7.19 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi (Cr VI)", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Cr(VI) karsinogenik", "Batas Paparan": "0.005 mg/m³"}, "Kegunaan": "Stainless steel, pelapisan krom."},
    "Mo": {"Informasi Dasar": {"Nama": "Molibdenum", "Nomor Atom": 42, "Kategori": "Logam Transisi", "Massa Atom Relatif": 95.95, "Golongan": "VIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁵ 5s¹", "Tahun Ditemukan": 1778}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tidak larut dalam HCl"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan", "Massa Jenis": "10.28 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Hindari paparan kronis debu", "Batas Paparan": "10 mg/m³"}, "Kegunaan": "Filamen listrik, mesin jet."},
    "W": {"Informasi Dasar": {"Nama": "Tungsten (Wolfram)", "Nomor Atom": 74, "Kategori": "Logam Transisi", "Massa Atom Relatif": 183.84, "Golongan": "VIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁴ 6s²", "Tahun Ditemukan": 1783}, "Sifat Kimia & Fisik": {"Reaktivitas": "Titik lebur tertinggi di antara logam"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keabu-abuan", "Massa Jenis": "19.25 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Aman dipegang", "Batas Paparan": "5 mg/m³"}, "Kegunaan": "Filamen bola lampu, mata bor berat."},

    # GOLONGAN VIIB
    "Mn": {"Informasi Dasar": {"Nama": "Mangan", "Nomor Atom": 25, "Kategori": "Logam Transisi", "Massa Atom Relatif": 54.938, "Golongan": "VIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁵ 4s²", "Tahun Ditemukan": 1774}, "Sifat Kimia & Fisik": {"Reaktivitas": "Perlahan teroksidasi di udara"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan", "Massa Jenis": "7.21 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Inhalasi debu memicu Manganisme", "Batas Paparan": "0.02 mg/m³"}, "Kegunaan": "Baja rel kereta api, baterai."},
    "Tc": {"Informasi Dasar": {"Nama": "Teknesium", "Nomor Atom": 43, "Kategori": "Logam Transisi", "Massa Atom Relatif": 98, "Golongan": "VIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁵ 5s²", "Tahun Ditemukan": 1937}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi, larut dalam asam nitrat"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu metalik", "Massa Jenis": "11.5 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Semua isotop radioaktif", "Batas Paparan": "Lab khusus"}, "Kegunaan": "Pelacak radiodiagnostik medis."},
    "Re": {"Informasi Dasar": {"Nama": "Renium", "Nomor Atom": 75, "Kategori": "Logam Transisi", "Massa Atom Relatif": 186.21, "Golongan": "VIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁵ 6s²", "Tahun Ditemukan": 1925}, "Sifat Kimia & Fisik": {"Reaktivitas": "Stabil secara mekanik pada suhu ekstrim"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "21.02 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Tidak berbahaya dalam wujud asli", "Batas Paparan": "Belum ditentukan"}, "Kegunaan": "Superalloy mesin jet pesawat."},

    # GOLONGAN VIIIB
    "Fe": {"Informasi Dasar": {"Nama": "Besi", "Nomor Atom": 26, "Kategori": "Logam Transisi", "Massa Atom Relatif": 55.845, "Golongan": "VIIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁶ 4s²", "Tahun Ditemukan": "Zaman Kuno"}, "Sifat Kimia & Fisik": {"Reaktivitas": "Mudah berkarat dengan air & oksigen"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak keabu-abuan", "Massa Jenis": "7.874 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Kelebihan memicu Hemokromatosis", "Batas Paparan": "5 mg/m³"}, "Kegunaan": "Infrastruktur jembatan, bangunan."},
    "Ru": {"Informasi Dasar": {"Nama": "Rutenium", "Nomor Atom": 44, "Kategori": "Logam Transisi", "Massa Atom Relatif": 101.07, "Golongan": "VIIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁷ 5s¹", "Tahun Ditemukan": 1844}, "Sifat Kimia & Fisik": {"Reaktivitas": "Inert pada banyak zat kimia"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih metalik", "Massa Jenis": "12.45 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (Senyawa)", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "RuO4 sangat beracun", "Batas Paparan": "Belum ada"}, "Kegunaan": "Kontak listrik, ujung pulpen elit."},
    "Os": {"Informasi Dasar": {"Nama": "Osmium", "Nomor Atom": 76, "Kategori": "Logam Transisi", "Massa Atom Relatif": 190.23, "Golongan": "VIIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁶ 6s²", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat keras dan rapuh"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih metalik kebiruan", "Massa Jenis": "22.59 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi (Oksidanya)", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Uap OsO4 memicu kebutaan", "Batas Paparan": "0.002 mg/m³"}, "Kegunaan": "Jarum piringan hitam, poros instrumen."},
    "Co": {"Informasi Dasar": {"Nama": "Kobal", "Nomor Atom": 27, "Kategori": "Logam Transisi", "Massa Atom Relatif": 58.933, "Golongan": "VIIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁷ 4s²", "Tahun Ditemukan": 1735}, "Sifat Kimia & Fisik": {"Reaktivitas": "Feromagnetik"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak abu-abu", "Massa Jenis": "8.90 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritan paru-paru", "Batas Paparan": "0.02 mg/m³"}, "Kegunaan": "Baterai Li-ion, turbin gas."},
    "Rh": {"Informasi Dasar": {"Nama": "Rodium", "Nomor Atom": 45, "Kategori": "Logam Transisi", "Massa Atom Relatif": 102.91, "Golongan": "VIIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁸ 5s¹", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Logam mulia tidak reaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "12.41 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Aman bentuk logam", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Konverter katalitik mobil, perhiasan."},
    "Ir": {"Informasi Dasar": {"Nama": "Iridium", "Nomor Atom": 77, "Kategori": "Logam Transisi", "Massa Atom Relatif": 192.22, "Golongan": "VIIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁷ 6s²", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Logam paling tahan korosi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih kekuningan", "Massa Jenis": "22.56 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Bentuk balok sangat aman", "Batas Paparan": "Belum ditentukan"}, "Kegunaan": "Busi performa tinggi, standar meter."},
    "Ni": {"Informasi Dasar": {"Nama": "Nikel", "Nomor Atom": 28, "Kategori": "Logam Transisi", "Massa Atom Relatif": 58.693, "Golongan": "VIIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁸ 4s²", "Tahun Ditemukan": 1751}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi tinggi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan kekuningan", "Massa Jenis": "8.908 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Pemicu alergi kontak kulit", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Baterai EV, koin, stainless steel."},
    "Pd": {"Informasi Dasar": {"Nama": "Paladium", "Nomor Atom": 46, "Kategori": "Logam Transisi", "Massa Atom Relatif": 106.42, "Golongan": "VIIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹⁰", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Menyerap gas hidrogen sangat baik"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan baja", "Massa Jenis": "12.02 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Logam asli aman", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Katalitik mobil, perhiasan emas putih."},
    "Pt": {"Informasi Dasar": {"Nama": "Platina", "Nomor Atom": 78, "Kategori": "Logam Transisi", "Massa Atom Relatif": 195.08, "Golongan": "VIIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁹ 6s¹", "Tahun Ditemukan": 1735}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat lembam, tidak berkarat"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih metalik", "Massa Jenis": "21.45 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Senyawa digunakan untuk kemoterapi", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Perhiasan elit, obat kemoterapi."},

    # GOLONGAN IVB s.d VIIIB (Periode 7 - Superberat)
    "Rf": {"Informasi Dasar": {"Nama": "Rutherfordium", "Nomor Atom": 104, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "267", "Golongan": "IVB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d² 7s²", "Tahun Ditemukan": 1964}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip Hafnium"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Prediksi)", "Warna": "Metalik (Prediksi)", "Massa Jenis": "23.2 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi mematikan", "Batas Paparan": "Lab nuklir"}, "Kegunaan": "Penelitian ilmiah."},
    "Db": {"Informasi Dasar": {"Nama": "Dubnium", "Nomor Atom": 105, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "268", "Golongan": "VB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d³ 7s²", "Tahun Ditemukan": 1967}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip Tantalum"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Prediksi)", "Warna": "Metalik (Prediksi)", "Massa Jenis": "29.3 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi mematikan", "Batas Paparan": "Lab nuklir"}, "Kegunaan": "Penelitian murni."},
    "Sg": {"Informasi Dasar": {"Nama": "Seaborgium", "Nomor Atom": 106, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "269", "Golongan": "VIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁴ 7s²", "Tahun Ditemukan": 1974}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip Tungsten"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Prediksi)", "Warna": "Metalik (Prediksi)", "Massa Jenis": "35.0 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi mematikan", "Batas Paparan": "Lab nuklir"}, "Kegunaan": "Penelitian ilmiah."},
    "Bh": {"Informasi Dasar": {"Nama": "Bohrium", "Nomor Atom": 107, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "270", "Golongan": "VIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁵ 7s²", "Tahun Ditemukan": 1981}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip Renium"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Prediksi)", "Warna": "Metalik (Prediksi)", "Massa Jenis": "37.1 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi mematikan", "Batas Paparan": "Lab nuklir"}, "Kegunaan": "Penelitian murni."},
    "Hs": {"Informasi Dasar": {"Nama": "Hassium", "Nomor Atom": 108, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "277", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁶ 7s²", "Tahun Ditemukan": 1984}, "Sifat Kimia & Fisik": {"Reaktivitas": "Membentuk HsO4 gas mirip Osmium"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Prediksi)", "Warna": "Metalik (Prediksi)", "Massa Jenis": "40.7 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi ionisasi ekstrim", "Batas Paparan": "Lab khusus"}, "Kegunaan": "Penelitian murni."},
    "Mt": {"Informasi Dasar": {"Nama": "Meitnerium", "Nomor Atom": 109, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "278", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁷ 7s²", "Tahun Ditemukan": 1982}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip Iridium"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Prediksi)", "Warna": "Metalik (Prediksi)", "Massa Jenis": "37.4 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Meluruh dalam milidetik", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Penelitian akselerator partikel."},
    "Ds": {"Informasi Dasar": {"Nama": "Darmstadtium", "Nomor Atom": 110, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "281", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁸ 7s²", "Tahun Ditemukan": 1994}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi inert mirip Platina"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Prediksi)", "Warna": "Putih keperakan (Prediksi)", "Massa Jenis": "34.8 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi murni", "Batas Paparan": "Akselerator partikel"}, "Kegunaan": "Penelitian nukleus."}
}

# --- SISTEM NAVIGASI SIDEBAR ---
st.sidebar.title("Navigasi Unsur")
st.sidebar.write("Silakan pilih unsur untuk melihat detailnya.")

# Menu dropdown utama
menu_halaman = st.sidebar.selectbox(
    "Cari dan Pilih Unsur Kimia:",
    ["Beranda (Selamat Datang)", "Tabel Periodik Interaktif"]
)

# Menampilkan Hak Cipta di Sidebar bawah
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 - Aplikasi Tabel Periodik")


# ==================== HALAMAN 1: BERANDA ====================
if menu_halaman == "Beranda (Selamat Datang)":
    # Membuat layout dua kolom untuk teks judul/isi dan ikon gambar/logo di sebelah kanan
    kolom_teks, kolom_gambar = st.columns([2, 1])
    
    with kolom_teks:
        st.markdown("<h4 style='color:gray;'>Tahun Ditemukan: 1766</h4>", unsafe_allow_html=True) # Sesuai SS kedua Anda
        st.title("👋 Selamat Datang di Ensiklopedia Unsur Kimia")
        st.write("")
        st.markdown("""
        Aplikasi ini adalah **Tabel Periodik Interaktif** yang dirancang untuk membantu Anda mempelajari berbagai unsur kimia dengan mudah dan detail.
        
        Melalui aplikasi ini, Anda dapat mengeksplorasi:
        * 📝 **Informasi Dasar** (Massa atom, konfigurasi elektron, dll)
        * 🧪 **Sifat Kimia & Fisik** (Reaktivitas, kelarutan)
        * 🧊 **Wujud Fisik** (Massa jenis, wujud pada suhu ruang)
        * ⚠️ **Kesehatan & Keselamatan** (Piktogram GHS dan tingkat toksisitas)
        * 🧰 **Kegunaan** (Aplikasi di dunia nyata)
        """)
        
        # Info Box Cara Penggunaan
        st.info("💡 **Cara Penggunaan:** Silakan buka menu dropdown di sebelah kiri (Sidebar) dan pilih unsur kimia atau menu **Tabel Periodik Interaktif** yang ingin Anda pelajari!")

    with kolom_gambar:
        # Tempat meletakkan ikon/emoji besar sebagai representasi visual gambar di SS kedua kamu
        st.write("")
        st.write("")
        st.markdown("<h1 style='font-size: 100px; text-align: center;'>🔬</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 100px; text-align: center;'>🧪</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 100px; text-align: center;'>⚛️</h1>", unsafe_allow_html=True)


# ==================== HALAMAN 2: TABEL PERIODIK ====================
elif menu_halaman == "Tabel Periodik Interaktif":
    st.title("Tabel Periodik Unsur Kimia Interaktif ⚛️")
    st.write("Klik pada unsur yang tersedia (warna dapat diklik) untuk melihat detailnya di bagian bawah.")
    
    # --- LOGIKA TOMBOL TABEL PERIODIK KAMU DI SINI ---
    # Sebagai contoh layout grid sederhana untuk tombol-tombolnya:
    st.subheader("Blok-s & Blok-d (Golongan IA - VIIIB)")
    
    # Kita buat baris tombol sederhana memakai st.columns
    baris1 = st.columns(18)
    with baris1[0]:
        if st.button("H", key="btn_H", use_container_width=True):
            st.session_state.pilihan_unsur = "H"
    with baris1[17]:
        if st.button("He", key="btn_He", use_container_width=True):
            st.warning("Data Helium belum dimasukkan ke dataset.")

    baris2 = st.columns(18)
    with baris2[0]:
        if st.button("Li", key="btn_Li", use_container_width=True):
            st.session_state.pilihan_unsur = "Li"
    with baris2[1]:
        if st.button("Be", key="btn_Be", use_container_width=True):
            st.session_state.pilihan_unsur = "Be"

    # [Tambahkan sisa tombol grid tabel periodik kamu yang lain di sini sesuai foto kesatu]
    
    st.markdown("---")
    
    # --- BAGIAN DETAIL UNSUR SAAT TOMBOL DIKLIK ---
    if "pilihan_unsur" in st.session_state and st.session_state.pilihan_unsur in unsur_data:
        simbol = st.session_state.pilihan_unsur
        detail = unsur_data[simbol]
        
        st.header(f"Detail Unsur: {detail['Informasi Dasar']['Nama']} ({simbol})")
        
        # Tampilkan Tabs agar informasi rapi sesuai fitur aplikasi Anda
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📝 Informasi Dasar", 
            "🧪 Sifat Kimia & Fisik", 
            "🧊 Wujud Fisik", 
            "⚠️ Kesehatan & Keselamatan", 
            "🧰 Kegunaan"
        ])
        
        with tab1:
            st.write(pd.DataFrame(detail["Informasi Dasar"].items(), columns=["Parameter", "Nilai"]))
        with tab2:
            st.write(detail["Sifat Kimia & Fisik"])
        with tab3:
            st.write(detail["Wujud Fisik"])
        with tab4:
            st.write(detail["Kesehatan & Keselamatan"])
        with tab5:
            st.write(f"**Kegunaan utama:** {detail['Kegunaan']}")
