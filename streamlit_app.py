import streamlit as st
import pandas as pd
# --- LAYOUT MATRIKS TABEL PERIODIK ---
st.markdown("""
<div style='text-align:center'>
<h1>🧪 Ensiklopedia Unsur Kimia Interaktif ✨</h1>
<h4>Kelompok 4</h4>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### 👩‍🔬 Tim Editor

- Hayu Raihanun (2560641)
- Niken Sri Uttari (2560727)
- Nisfy Sabrina Flowerridha Supriyadi (2560728)
- Raifan Syahdan Putra Raya (2560742)

---
""")
import time

loading = st.empty()

loading.markdown("""
<div style='text-align:center'>
<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaG9hdWhtYWdwYTVtY3JncWttN2hjemRzMzNtamhsaTM3aGtyZnI3NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L4rugeg6oC3yE/giphy.gif' width='250'>
<h3>Memuat Data Unsur...</h3>
</div>
""", unsafe_allow_html=True)

time.sleep(2)
loading.empty()
st.markdown("""
<style>

.stApp{
background:linear-gradient(
180deg,
#FFF0F8,
#F5EFFF,
#EAF8FF
);
}

[data-testid="stSidebar"]{
background:#FFE4F2;
}

.stButton button{
background:#FFB7D5 !important;
border-radius:15px !important;
border:none !important;
}

</style>
""", unsafe_allow_html=True)
