import streamlit as st

# =========================================================
# KONFIGURASI
# =========================================================
st.set_page_config(
    page_title="Tabel Periodik Pop-Pastel",
    page_icon="🎨",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Fredoka', sans-serif;
    background-color: #fff7fb;
}

.title {
    text-align: center;
    font-size: 52px;
    font-weight: bold;
    color: #ff66a3;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 40px;
}

.element {
    background: white;
    border-radius: 18px;
    padding: 10px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    transition: 0.3s;
    margin-bottom: 10px;
}

.element:hover {
    transform: scale(1.05);
    background: #ffe6f2;
}

.symbol {
    font-size: 24px;
    font-weight: bold;
}

.number {
    font-size: 12px;
    color: gray;
}

.name {
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# JUDUL
# =========================================================
st.markdown('<div class="title">🎨 Tabel Periodik Pop-Pastel</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Versi lengkap semua unsur ✨</div>', unsafe_allow_html=True)

# =========================================================
# DATA SEMUA UNSUR
# =========================================================

elements = [
("H","Hydrogen"),("He","Helium"),
("Li","Lithium"),("Be","Beryllium"),("B","Boron"),("C","Carbon"),
("N","Nitrogen"),("O","Oxygen"),("F","Fluorine"),("Ne","Neon"),

("Na","Sodium"),("Mg","Magnesium"),("Al","Aluminium"),("Si","Silicon"),
("P","Phosphorus"),("S","Sulfur"),("Cl","Chlorine"),("Ar","Argon"),

("K","Potassium"),("Ca","Calcium"),("Sc","Scandium"),("Ti","Titanium"),
("V","Vanadium"),("Cr","Chromium"),("Mn","Manganese"),("Fe","Iron"),
("Co","Cobalt"),("Ni","Nickel"),("Cu","Copper"),("Zn","Zinc"),
("Ga","Gallium"),("Ge","Germanium"),("As","Arsenic"),("Se","Selenium"),
("Br","Bromine"),("Kr","Krypton"),

("Rb","Rubidium"),("Sr","Strontium"),("Y","Yttrium"),("Zr","Zirconium"),
("Nb","Niobium"),("Mo","Molybdenum"),("Tc","Technetium"),("Ru","Ruthenium"),
("Rh","Rhodium"),("Pd","Palladium"),("Ag","Silver"),("Cd","Cadmium"),
("In","Indium"),("Sn","Tin"),("Sb","Antimony"),("Te","Tellurium"),
("I","Iodine"),("Xe","Xenon"),

("Cs","Cesium"),("Ba","Barium"),("La","Lanthanum"),("Ce","Cerium"),
("Pr","Praseodymium"),("Nd","Neodymium"),("Pm","Promethium"),
("Sm","Samarium"),("Eu","Europium"),("Gd","Gadolinium"),
("Tb","Terbium"),("Dy","Dysprosium"),("Ho","Holmium"),
("Er","Erbium"),("Tm","Thulium"),("Yb","Ytterbium"),
("Lu","Lutetium"),

("Hf","Hafnium"),("Ta","Tantalum"),("W","Tungsten"),
("Re","Rhenium"),("Os","Osmium"),("Ir","Iridium"),
("Pt","Platinum"),("Au","Gold"),("Hg","Mercury"),
("Tl","Thallium"),("Pb","Lead"),("Bi","Bismuth"),
("Po","Polonium"),("At","Astatine"),("Rn","Radon"),

("Fr","Francium"),("Ra","Radium"),("Ac","Actinium"),
("Th","Thorium"),("Pa","Protactinium"),("U","Uranium"),
("Np","Neptunium"),("Pu","Plutonium"),("Am","Americium"),
("Cm","Curium"),("Bk","Berkelium"),("Cf","Californium"),
("Es","Einsteinium"),("Fm","Fermium"),("Md","Mendelevium"),
("No","Nobelium"),("Lr","Lawrencium"),

("Rf","Rutherfordium"),("Db","Dubnium"),("Sg","Seaborgium"),
("Bh","Bohrium"),("Hs","Hassium"),("Mt","Meitnerium"),
("Ds","Darmstadtium"),("Rg","Roentgenium"),("Cn","Copernicium"),
("Nh","Nihonium"),("Fl","Flerovium"),("Mc","Moscovium"),
("Lv","Livermorium"),("Ts","Tennessine"),("Og","Oganesson")
]

# =========================================================
# TAMPILAN GRID
# =========================================================

cols = st.columns(9)

for i, (symbol, name) in enumerate(elements):

    with cols[i % 9]:

        st.markdown(f"""
        <div class="element">
            <div class="number">{i+1}</div>
            <div class="symbol">{symbol}</div>
            <div class="name">{name}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"{symbol}", key=symbol):
            st.success(f"{symbol} = {name}")

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<br><br>
<center>✨ Semua unsur tabel periodik lengkap ✨</center>
""", unsafe_allow_html=True)
