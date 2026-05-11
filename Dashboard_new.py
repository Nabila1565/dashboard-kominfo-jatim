import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import matplotlib.colors as mcolors
import streamlit.components.v1 as components
import json
import base64
from PIL import Image
from pathlib import Path
from textwrap import dedent
from babel.numbers import format_currency


st.set_page_config(
    page_title="Dashboard Pertumbuhan Ekonomi Jawa Timur",
    page_icon="🗺️",
    layout="wide"
)

# Custom Sidebar
st.markdown("""
<style>
/* Background utama */
.stApp {
    background: linear-gradient(135deg, #061A33, #0B2C55);
}    

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #031120, #08284d);
}

/* Judul logo */
.logo-box {
    text-align: center;
    padding: 20px 10px;
    color: white;
}

.logo-icon {
    width: 45px;
    height: 45px;
    background: #0f4c81;
    border-radius: 12px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin-bottom: 8px;
    box-shadow: 0 0 15px rgba(77, 166, 255, 0.45);
}

.logo-title {
    font-size: 22px;
    font-weight: 700;
}

.logo-subtitle {
    font-size: 12px;
    color: #b8d9ff;
}

/* Radio menu */
div[role="radiogroup"] label {
    background-color: #5DADE2 !important;  
    border: 1.5px solid #5DADE2 !important; 
    padding: 14px 16px;
    border-radius: 14px;
    margin-bottom: 12px;
    color: white !important;
    transition: 0.3s;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}
}

div[role="radiogroup"] label:hover {
    background-color: rgba(77,166,255,0.22);
    transform: translateX(4px);
}

/* Tulisan "Pilih Menu" */
[data-testid="stSidebar"] label {
    color: white !important;
    font-weight: 600;
}

/* Tulisan menu radio: Informasi Jawa Timur, Dashboard */
div[role="radiogroup"] label p {
    color: white !important;
    font-size: 16px;
    font-weight: 600;
}

/* Warna bulatan radio */
div[role="radiogroup"] input {
    accent-color: #4DA6FF;
}     

/* Card konten */
.content-card {
    background: rgba(255,255,255,0.10);
    padding: 30px;
    border-radius: 22px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.30);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(184,217,255,0.22);
}

.content-card h1 {
    color: #ffffff;
    margin-bottom: 10px;
}

.content-card p {
    font-size: 17px;
    line-height: 1.8;
    color: #eaf5ff;
}

/* Info box */
.info-box {
    background: rgba(255,255,255,0.12);
    padding: 18px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid rgba(184,217,255,0.22);
}

.info-number {
    font-size: 28px;
    font-weight: bold;
    color: #8ecaff;
}

.info-label {
    font-size: 14px;
    color: #dceeff;
}
</style>
""", unsafe_allow_html=True)

# Logo Sidebar
st.sidebar.image("kominfobg.png", width=350)

# Sidebar Menu
menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "Informasi Jawa Timur",
        "Dashboard"
    ]
)
#Backgroud
def get_base64_image(image_path):
    image_file = Path(image_path)
    if image_file.exists():
        return base64.b64encode(image_file.read_bytes()).decode()
    return""
bg_image = get_base64_image("Jatim.jpg")

st.markdown(f"""
<style>
.hero-banner {{
    background-image: linear-gradient(
        rgba(0, 0, 0, 0.70),
        rgba(0, 0, 0, 0.70)
    ), url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    border-radius: 18px;
    padding: 90px 35px;
    margin-bottom: 35px;
}}

.hero-title {{

    color: white !important;
    font-size: 70px;
    font-weight: 1000;
    line-height: 1.15;
    margin: 0;
     text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.10);
}}
</style>

<div class="hero-banner">
    <h1 class="hero-title">
        Dashboard Pertumbuhan Ekonomi<br>
        Provinsi Jawa Timur
    </h1>
</div>
""", unsafe_allow_html=True)
            

#Membaca data
df = pd.read_csv("PertumbuhanEkonomi.csv")

#Isi
if menu == "Informasi Jawa Timur":

    st.markdown("""
<style>
.info-jatim-title {
    color: #FFFFFF !important;
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 20px;
}

.info-jatim-text {
    color: #FFFFFF !important;
    text-align: justify;
    font-size: 17px;
    line-height: 1.8;
}

.info-jatim-text b {
    color: #FFFFFF !important;
}
</style>

<h2 class="info-jatim-title">Informasi Jawa Timur</h2>

<div class="info-jatim-text">
Jawa Timur merupakan salah satu provinsi di bagian timur Pulau Jawa, Indonesia. 
Provinsi ini secara resmi dibentuk berdasarkan Undang-Undang Nomor 2 Tahun 1950 
dan ditetapkan pada 4 Maret 1950. Jawa Timur merupakan provinsi terluas di Pulau Jawa dengan luas wilayah sekitar 
<b>48.033 km²</b>. Secara administratif, provinsi ini terdiri atas 
<b>29 kabupaten dan 9 kota</b>, dengan Kota Surabaya sebagai ibu kota sekaligus 
pusat kegiatan ekonomi dan pemerintahan.Mayoritas penduduk Jawa Timur berasal dari Suku Jawa. Selain itu, provinsi ini 
dikenal memiliki kekayaan budaya yang beragam dan khas, seperti kesenian 
<b>Reog Ponorogo</b>, <b>Ludruk</b>, serta berbagai tradisi daerah lainnya yang 
masih dilestarikan hingga saat ini.
</div>
""", unsafe_allow_html=True)

 

    #Peta Jawa Timur    
    st.markdown("""
    <style>
    .info-jatim-title {
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <h3 class="info-jatim-title">Peta Kabupaten/Kota Provinsi Jawa Timur</h3>
    """, unsafe_allow_html=True
    )
    peta = Image.open("peta(2).jpeg")
    st.image(peta, caption="Peta Kabupaten/Kota Provinsi Jawa Timur", use_container_width=True)

    #Grafik Kondisi Pertumbuhan Ekonomi
    df = pd.DataFrame({
        "Kabupaten/Kota":["DIY","Jawa Barat","Jawa Timur","Jawa Tengah","DKI Jakarta","Banten"],
        "Nilai":[5.94,5.85,5.85,5.84,5.71,5.64]
    })
    st.markdown("""
    <style>
    .info-jatim-title {
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <h2 class="info-jatim-title">6 Provinsi dengan Pertumbuhan Ekonomi Tertinggi di Pulau Jawa Tahun 2025</h2>
    """, unsafe_allow_html=True
    )


    df = df.sort_values("Nilai", ascending=False)
    df["Warna"] = df["Kabupaten/Kota"].apply(
    lambda x: "Sorotan" if x == "Jawa Timur" else "Lainnya"
)

    fig = px.bar(
        df,
        x="Kabupaten/Kota",
        y="Nilai",
        color="Warna",
        color_discrete_map={
            "Sorotan": "#DFEDC8",   # warna batang yang beda
            "Lainnya": "#3F8101"    # warna batang lainnya
        },
        category_orders={
        "Kabupaten/Kota": df["Kabupaten/Kota"].tolist()
        },
        labels={
            "Kabupaten/Kota":"Kabupaten/Kota",
            "Nilai":"Nilai (%)"
        },
        text = "Nilai"
    )
    fig.update_layout(
        height=500,
        xaxis = dict(
            title=dict(text="Kabupaten/Kota", font=dict(color="white")),
            tickfont=dict(color="white"),
        ),
        yaxis = dict(
            title=dict(text="Nilai(%)", font=dict(color="white")),
            tickfont=dict(color="white"),
        ),
        xaxis_tickangle=0,
        plot_bgcolor="#000000",
        paper_bgcolor="#000000",
        font=dict(color="white"),
    )
    fig.update_yaxes(range=[5.6,6.05], ticksuffix="%")

    fig. update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside",
        textfont=dict(color="white", size=12)
    )
    fig.add_annotation(
    text="Sumber: BPS Jatim Tahun 2025",
    xref="paper",
    yref="paper",
    x=0,
    y=-0.20,
    showarrow=False,
    font=dict(size=15, color="white"),
    align="left"
    )
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)  
    with col1:
        st.markdown("""
        <div style="
            background:#000000;
            color:white;
            padding:20px;
            border-radius:12px;
            font-size:25px;
        ">
            <span style="color:orange; font-weight:bold; font-size:30px;">Jawa Timur</span><br><br>
            Menempati posisi ketiga pertumbuhan ekonomi tertinggi di Pulau Jawa sebesar <b>5.85%</b>.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            background:#000000;
            color:white;
            padding:20px;
            border-radius:12px;
            font-size:25px;
        ">
            <span style="color:orange; font-weight:bold; font-size:30px;">Daerah Istimewa Yogyakarta</span><br><br>
            Menjadi provinsi dengan pertumbuhan ekonomi tertinggi di Pulau Jawa dengan nilai <b>5.94%</b>.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .inflasi-wrapper {
        height: 450px;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .inflasi-box {
        background-color: #ff8c00;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #ffb366;
        text-align: center;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .inflasi-title {
        font-size: 15px;
        font-weight: bold;
        color: #ffffff;
    }

    .inflasi-value {
        font-size: 26px;
        font-weight: bold;
        color: #ffffff;
    }

    .inflasi-subvalue {
        font-size: 16px;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
<style>
.box {
    background-color: #ff8c00;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ffb366;
    text-align: center;
}
.title {
    font-size: 16px;
    font-weight: bold;
    color: #ffffff;
}
.value {
    font-size: 28px;
    font-weight: bold;
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

    #Grafik Pertumbuhan Ekonomi Provinsi Jawa
    data_str = ["5.47", "5.53","-2.33","3.56","6.51","5.7","5.76","5.33"]
    year = list(range(2018,2026))
    #membuat data frame
    df = pd.DataFrame({
        "Tahun":year,
        "Nilai": data_str
    })
    print(df)

    #Line Chart Pertumbuhan Jawa Timur Berdasarkan Tahun
    st.markdown("""
    <style>
    .info-jatim-title {
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <h2 class="info-jatim-title">Grafik Pertumbuhan Ekonomi Provinsi Jawa Timur Tahun 2018–2025</h2>
    """, unsafe_allow_html=True
    )

    fig = px.line(df, x="Tahun", y="Nilai", markers=True, labels={"Tahun":"Tahun","Nilai": "Nilai(%)"}, text="Nilai")
    fig.update_layout(
    plot_bgcolor="#000000",
    paper_bgcolor="#000000",
    font=dict(color="white"), 
    xaxis = dict(
        title=dict(text="Tahun", font=dict(color="white")),
        tickfont=dict(color="white")
    ),
    yaxis = dict(
            title=dict(text="Nilai(%)", font=dict(color="white")),
            tickfont=dict(color="white"))
    )
    fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="top center",
    textfont=dict(color="white", size=12)
    )
    fig.add_annotation(
    text="Sumber: BPS Jatim Tahun 2018-2025",
    xref="paper",
    yref="paper",
    x=0,
    y=-0.20,
    showarrow=False,
    font=dict(size=16, color="white"),
    align="left")

   
    st.plotly_chart(fig)
    
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="box">
            <div style="font-size:20px; font-weight:bold; color:white;">
                Rata-Rata Pertumbuhan Ekonomi 2024
            </div>
            <div style="font-size:40px; font-weight:bold; color:white;">
                5.76%
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="box">
            <div style="font-size:20px; font-weight:bold; color:white;">
                Rata-Rata Pertumbuhan Ekonomi 2025
            </div>
            <div style="font-size:40px; font-weight:bold; color:white;">
                5.33%
            </div>
        </div>
        """, unsafe_allow_html=True)

    #Subba  Laju Pertumbuhan Ekonomi berdasarkan lapangan usaha tahun 2025
    st.markdown("""
    <style>
    .info-jatim-title {
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <h2 class="info-jatim-title">Laju Pertumbuhan Ekonomi Berdasarkan Lapangan Usaha Tahun 2025</h2>
    """, unsafe_allow_html=True
    )
    #Pertumbuhan Ekonomi Berdasarkan Lapangan Usaha Tahun 2025
    df_lapangan = pd.read_csv("PE Lapangan Usaha - Sheet1.csv", header=0)

    #Mengambil kolom yang tergabung
    df_lapangan= df_lapangan.iloc[:,0]
    # Memisahkan 2 kolom
    df_lapangan = df_lapangan.str.rsplit(',"',n=1, expand=True)
    df_lapangan.columns=["Lapangan Usaha","Laju pertumbuhan ekonomi"]
    # bersihin tanda kutip & ubah ke float
    df_lapangan["Laju pertumbuhan ekonomi"] = (
        df_lapangan["Laju pertumbuhan ekonomi"]
        .str.replace('"', "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    df_lapangan = df_lapangan.sort_values("Laju pertumbuhan ekonomi")
    fig = px.bar(
        df_lapangan,
        x="Laju pertumbuhan ekonomi",
        y="Lapangan Usaha",
        orientation='h',
        color="Laju pertumbuhan ekonomi",
        color_continuous_scale="RdYlGn",
        text="Laju pertumbuhan ekonomi"
    )

    fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside",
    cliponaxis=False
    )
    fig.update_layout(
    plot_bgcolor="#000000",
    paper_bgcolor="#000000",
    font=dict(color="white"),
    height=700,
    margin=dict(l=250, r=120, t=50, b=120),
    yaxis=dict(
        automargin=True,
        title = dict(text="Lapangan Usaha", font=dict(color="white")),
        tickfont=dict(size=11, color="white"),
    ),
    xaxis=dict(
        title=dict(text="Laju pertumbuhan ekonom (%)", font=dict(color="white")),
        range=[0, df_lapangan["Laju pertumbuhan ekonomi"].max() + 3],
        ticksuffix="%",
        tickfont=dict(size=11, color="white"),
    ),
    coloraxis_colorbar=dict(
        title="Laju<br>pertumbuhan<br>ekonomi<br>(%)"
    )
)
    fig.add_annotation(
    text="Sumber: BPS Jatim Tahun 2025",
    xref="paper",
    yref="paper",
    x=0,
    y=-0.20,
    showarrow=False,
    font=dict(size=16, color="white"),
    align="left")

    st.plotly_chart(fig, use_container_width=True)

    # SUBBAB INFLASI
    st.markdown("""
    <style>
    .info-jatim-title {
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <h2 class="info-jatim-title">Inflasi Provinsi Jawa Timur Tahun 2018-2025</h2>
    """, unsafe_allow_html=True
    )
    
    # 1. LOAD DATA
    df_inflasi = pd.read_csv("Inflasi (1).csv")
    df_inflasi.columns = ["tahun", "periode", "jumlah"]
   
    # 2. CLEANING
    df_inflasi["tahun"] = df_inflasi["tahun"].astype(int)
    
    df_inflasi["jumlah"] = (
        df_inflasi["jumlah"]
        .astype(str)
        .str.replace('"', '', regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    # STATISTIK INFLASI
    #Rata-rata Inflasi
    mean_inflasi_tahunan = (
        df_inflasi.groupby("tahun", as_index=False)["jumlah"].mean()
    )
    mean_total_inflasi = df_inflasi["jumlah"].mean()
    # Mengambil nilai rata-rata minimal
    min_row_inflasi = mean_inflasi_tahunan.loc[mean_inflasi_tahunan["jumlah"].idxmin()]
    min_tahun_inflasi = int(min_row_inflasi["tahun"])
    min_nilai_inflasi = min_row_inflasi["jumlah"]

    #Mengambil Nilai rata-rata terbesar
    max_row_inflasi = mean_inflasi_tahunan.loc[mean_inflasi_tahunan["jumlah"].idxmax()]
    max_tahun_inflasi = int(max_row_inflasi["tahun"])
    max_value_inflasi = max_row_inflasi["jumlah"]

    # GRAFIK TAHUNAN
    fig_line = px.line(
        mean_inflasi_tahunan,
        x="tahun",
        y="jumlah",
        text = "jumlah", 
        markers=True)

    fig_line.update_traces(
        text=mean_inflasi_tahunan["jumlah"],
        texttemplate="%{text:.2f}%",
        textposition="top center",
        marker=dict(size=9),
        line=dict(width=3),
        hovertemplate="<b>Tahun</b>: %{x}<br><b>Inflasi</b>: %{y:.2f}%<extra></extra>"
    )

    fig_line.update_xaxes(
        tickmode="linear",
        dtick=1
    )


    fig_line.add_annotation(
    text="Sumber: BPS Jatim Tahun 2025",
    xref="paper",
    yref="paper",
    x=0,
    y=-0.25,
    showarrow=False,
    font=dict(size=15, color="white"),
    align="left"
    )

    fig_line.update_layout(
        height=450,
        xaxis = dict(
            title = dict(text="Tahun",font=dict(color="white")), 
            tickfont = dict(color="white")               
        ),
        yaxis = dict(
            title = dict(text="Inflasi (%)",font=dict(color="white")), 
            tickfont = dict(color="white")               
        ),
        plot_bgcolor="#000000",
        paper_bgcolor="#000000",
        font=dict(color="white"),
        hoverlabel=dict(
        bgcolor="#0A2342",
        font_size=14,
        font_color="white",
        bordercolor="#8ecaff"
    ))
   
    st.plotly_chart(fig_line, use_container_width=True)

    # INSIGHT
    col1, col2, col3 = st.columns(3)
    st.markdown("""
    <style>
    .box {
        background-color: #ff8c00;
        border-radius: 12px;
        padding: 20px;
        height: 190px;
        text-align: center;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)
        
    with col1:
        st.markdown(f"""
        <div class="box"style= "text-align:center;">     
            <div style="font-size:18px; font-weight:bold; color:white;">
                Rata-rata Inflasi Tahun 2018-2025
            </div>
            <div style="font-size:50px;font-weight:bold; color: white;">
              {mean_total_inflasi:.2f}%
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="box">
            <div style="font-size:18px; font-weight:bold; color:white;">
                Nilai Inflasi Terkecil Periode Tahun 2018-2025
            </div>
            <div style="font-size:50px; font-weight:bold; color:white;">  
                {min_nilai_inflasi:.2f}%
            </div>
            <div style="font-size:20px; font-weight:bold; color:white;">
                Tahun {min_tahun_inflasi:}
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="box">
             <div style="font-size:18px; font-weight:bold; color:white;">
                Nilai Inflasi Terbesar Periode Tahun 2018-2025
            </div>
            <div style="font-size:50px; font-weight:bold; color:white;">
                {max_value_inflasi:.2f}%
            </div>
            <div style="font-size:18px; font-weight:bold; color:white;">
                 Tahun {max_tahun_inflasi}
            </div>
        </div>
        """, unsafe_allow_html=True)

elif menu == "Dashboard":
    #Visualisasi Berdasarkan Kabupaten/Kota
    st.markdown("""
    <style>
    .info-jatim-title {
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <h1 class="info-jatim-title">Pertumbuhan Ekonomi Berdasarkan Kabupaten/Kota</h1>
    """, unsafe_allow_html=True
    )

    
    
   
    df = pd.read_csv("PertumbuhanEkonomi.csv")
    #Change wide to long
    df_long = df.melt(
    id_vars=["Kabupaten/Kota"],   # kolom tetap
    var_name="Tahun",             # jadi kolom baru
    value_name="Nilai"            # isi nilai 
    )

    st.markdown("""
    <style>
    .info-jatim-title {
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <h2 class="info-jatim-title">5 Kabupaten/Kota dengan Nilai Pertumbuhan Ekonomi Tertinggi</h2>
    """, unsafe_allow_html=True
    )

    # Menghapus Kolom Nomor
    df_long = df_long[df_long["Tahun"] != "No"]
    #Cleaning data
    df_long["Tahun"] = df_long["Tahun"].astype(int)
    df_long["Nilai"] = df_long["Nilai"].astype(str).str.replace(",",".").astype(float)

    #Revisi Dashboard Tahun
  # Ambil daftar tahun
    tahun_list = sorted(df_long["Tahun"].unique())

    
    # FILTER TAHUN 
    st.markdown("""
    <style>
    .tahun-putih {
        color: #FFFFFF !important;
        font-size: 26px !important;
        font-weight: 800 !important;
        margin-top: 25px !important;
        margin-bottom: 15px !important;
        opacity: 1 !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
    /* Hanya tulisan label "Pilih Tahun" */
    [data-testid="stSelectbox"] label,
    [data-testid="stSelectbox"] label p {
        color: white !important;
        font-weight: 600;
    }

    /* Isi/dropdown tahun tetap gelap */
    [data-testid="stSelectbox"] [data-baseweb="select"] * {
        color: #111111 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    col_filter1, col_filter2 = st.columns(2)

    with col_filter1:
        year_left = st.selectbox("Pilih Tahun", tahun_list, index=len(tahun_list)-1)

    with col_filter2:
        year_right = st.selectbox("Pilih Tahun", tahun_list, index=len(tahun_list)-2)

    # Filter data
    df_left = df_long[df_long["Tahun"] == year_left]
    df_right = df_long[df_long["Tahun"] == year_right]

    # Ambil Nilai Tertinggi
    top_left = df_left.sort_values("Nilai", ascending=False).head(5)
    top_right = df_right.sort_values("Nilai", ascending=False).head(5)

    col1, col2 = st.columns(2)

    max_left = top_left["Nilai"].max()
    max_right = top_right["Nilai"].max()
    max_value = max(max_left, max_right)

    # Batas sumbu X dibuat dari 5 sampai nilai tertinggi + ruang label
    x_min = 5
    x_max = max_value + 0.45

    with col1:
        st.markdown(f"""
        <h3 style="color: white !important;">
            Tahun {year_left}
        </h3>
        """, unsafe_allow_html=True)


        fig_top_left = px.bar(
            top_left,
            x="Nilai",
            y="Kabupaten/Kota",
            orientation="h",
            text="Nilai",
            color="Nilai",
            color_continuous_scale="RdYlGn"
        )

        fig_top_left.update_traces(
            texttemplate="%{text:.2f}%",
            textposition="outside",
            cliponaxis=False
        )

        fig_top_left.update_layout(
            height=400,
            plot_bgcolor="#000000",
            paper_bgcolor="#000000",
            font=dict(color="white"),
            margin=dict(l=50, r=70, t=20, b=50),
            xaxis=dict(
                range=[x_min, x_max],
                tickmode="linear",
                dtick=0.5,
                tickfont=dict(color="white"),
                title = dict(text="Nilai(%)", font=dict(color ="white"))
            ),
            yaxis=dict(
                title=dict(text="Kabupaten/Kota", font= dict(color="white")),
                tickfont= dict(color="white"),
                automargin=True,
                categoryorder="total ascending"
            )
        )
        fig_top_left.add_annotation(
        text="Sumber: Open Data Jatim",
        xref="paper",
        yref="paper",
        x=0,
        y=-0.22,
        showarrow=False,
        font=dict(size=16, color="white"),
        align="left")
        st.plotly_chart(fig_top_left, use_container_width=True)


    with col2:
        st.markdown(f"""
        <h3 class="tahun-title">Tahun {year_right}</h3>
        """, unsafe_allow_html=True)

        fig_top_right = px.bar(
            top_right,
            x="Nilai",
            y="Kabupaten/Kota",
            orientation="h",
            text="Nilai",
            color="Nilai",
            color_continuous_scale="RdYlGn"
        )

        fig_top_right.update_traces(
            texttemplate="%{text:.2f}%",
            textposition="outside",
            cliponaxis=False
        )

        fig_top_right.update_layout(
            height=400,
            plot_bgcolor="#000000",
            paper_bgcolor="#000000",
            font=dict(color="white"),
            margin=dict(l=130, r=100, t=40, b=40),

            xaxis=dict(
                range=[5, 6],
                title=dict(
                    text="Nilai (%)",
                    font=dict(color="white")
                ),
                tickfont=dict(color="white"),
                linecolor="white"
            ),

            yaxis=dict(
                automargin=True,
                categoryorder="total ascending",
                tickfont=dict(color="white"),
                title=dict(
                    text="Kabupaten/Kota",
                    font=dict(color="white")
                ),
                linecolor="white"
            )
        )
                

        fig_top_right.add_annotation(
        text="Sumber: Open Data Jatim",
        xref="paper",
        yref="paper",
        x=0,
        y=-0.24,
        showarrow=False,
        font=dict(size=16, color="white"),
        align="left")

        st.plotly_chart(fig_top_right, use_container_width=True)
   



    #Submateri tentang pertumbuhan ekonomi berdasarkan Kab/Kota
    st.markdown("""
    <style>
    .info-jatim-title {
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <h2 class="info-jatim-title">Pertumbuhan Ekonomi Berdasarkan Kabupaten/Kota</h2>
    """, unsafe_allow_html=True
    )

# Filter
    kabupaten = st.selectbox(
        "Pilih Kabupaten/Kota",
        df_long["Kabupaten/Kota"].unique()
    )

    tahun_list = sorted(df_long["Tahun"].unique())

    def handle_tahun_change():
        selected = st.session_state.selected_tahun

        # Jika "Semua" dipilih bareng tahun lain, jadikan hanya "Semua"
        if "Semua" in selected and len(selected) > 1:
            st.session_state.selected_tahun = ["Semua"]
            return

        # Jika semua tahun dipilih manual, otomatis ganti jadi "Semua"
        tahun_dipilih = [t for t in selected if t != "Semua"]

        if set(tahun_dipilih) == set(tahun_list):
            st.session_state.selected_tahun = ["Semua"]
            return

        # Urutkan tahun yang dipilih
        st.session_state.selected_tahun = sorted(tahun_dipilih)

    selected_tahun = st.multiselect(
        "Pilih Tahun",
        ["Semua"] + tahun_list,
        default=["Semua"],
        key="selected_tahun",
        on_change=handle_tahun_change
    )
    # Validasi minimal 2 tahun
    if "Semua" not in selected_tahun and len(selected_tahun) < 2:
        st.warning("Pilih minimal 2 tahun")
        st.stop()

    # Info tampilan
    if "Semua" in selected_tahun:
        st.caption("Tahun: Semua")
        filtered = df_long[df_long["Kabupaten/Kota"] == kabupaten]
    else:
        st.caption(f"Tahun: {', '.join(map(str, selected_tahun))}")
        filtered = df_long[
            (df_long["Kabupaten/Kota"] == kabupaten) &
            (df_long["Tahun"].isin(selected_tahun))
        ]  
    st.markdown("""
    <style>
    .info-wrapper {
        height: 450px;
        display: flex;
        flex-direction: column;
        gap: 14px;
    }

    .box {
        background-color: #ff8c00;
        border-radius: 18px;
        border: 1px solid #ffb366;
        padding: 16px 18px;
        min-height: 125px;
        text-align: center;
        color: white;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 6px;
    }

    .title {
        font-size: 18px;
        font-weight: 700;
        line-height: 1.25;
        margin: 0;
    }

    .subvalue {
        font-size: 16px;
        font-weight: 600;
        line-height: 1;
        margin: 0;
    }

    .value {
        font-size: 34px;
        font-weight: 800;
        line-height: 1.1;
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)

    

    #Menghitung Statistik
    rata_rata = filtered["Nilai"].mean()
    data_tertinggi = filtered.loc[filtered["Nilai"].idxmax()]
    tahun_tertinggi = int(data_tertinggi["Tahun"])
    nilai_tertinggi = data_tertinggi["Nilai"]
    
    data_terendah = filtered.loc[filtered["Nilai"].idxmin()]
    tahun_terendah = int(data_terendah["Tahun"])
    nilai_terendah = data_terendah["Nilai"]

    if "Semua"in selected_tahun:
        tahun_text = f"{df_long['Tahun'].min()}-{df_long['Tahun'].max()}"
    else:
        tahun_text = f"{min(selected_tahun)}-{max(selected_tahun)}"


    col_grafik, col_info = st.columns([3, 1], gap="medium")

    with col_grafik:
        st.markdown(
        f"""
        <h3 style="
            margin-bottom: 10px;
            color: white;
            font-weight: 400;
        ">
            Pertumbuhan Ekonomi {kabupaten} Tahun {tahun_text}
        </h3>
        """,
        unsafe_allow_html=True
    )
        fig = px.line(
            filtered,
            x="Tahun",
            y="Nilai",
            text = "Nilai",
            markers=True,
        )
        fig.update_traces(
            texttemplate="%{text:.2f}%",
            textposition="top center",
            textfont=dict(color="white", size=12),
            marker=dict(size=9),
            line=dict(width=3)
        )
          
        fig.update_layout(
            plot_bgcolor="#000000",
            paper_bgcolor="#000000",
            font=dict(color="white"),
            height=450,
            xaxis=dict(
                tickmode="linear",
                title = dict(
                    text="Tahun", 
                    font=dict(color="white")),
                dtick=1,
                tickfont = dict(color="white")
            ),
           
            yaxis=dict(
                tickmode="linear",
                title =dict(text="Nilai (%)", font=dict(color="white")),
                dtick=1, 
                tickfont=dict(color="white")
            ),
            )
        fig.add_annotation(
        text="Sumber: Open Data Jatim",
        xref="paper",
        yref="paper",
        x=0,
        y=-0.20,
        showarrow=False,
        font=dict(size=14, color="white"),
        align="left"
        )

        st.plotly_chart(fig, use_container_width=True)
    with col_info:
        st.markdown(dedent(f"""
        <div class="info-wrapper">

        <div class="box">
            <div class="title">Rata-Rata<br>{kabupaten}<br>({tahun_text})</div>
            <div class="value">{rata_rata:.2f}%</div>
        </div>

        <div class="box">
            <div class="title">Nilai Tertinggi {kabupaten}</div>
            <div class="value">{nilai_tertinggi:.2f}%</div>
            <div class="subvalue"><br>Tahun {tahun_tertinggi}<br></div>
        </div>
        <div class="box">
            <div class="title">Nilai Terendah {kabupaten}</div>
            <div class="value">{nilai_terendah:.2f}%</div>
            <div class="subvalue">Tahun {tahun_terendah}</div>
        </div>
        """), unsafe_allow_html=True)

#Subbab Data Inflsi
    st.markdown("""
    <style>
    .info-jatim-title {
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <style>
    .info-jatim-subtitle {
        color: #FFFFFF !important;
        font-size: 25px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <style>
    .info-jatim-subtitle1 {
        color: #FFFFFF !important;
        font-size: 10px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <h1 class="info-jatim-title">Kondisi Inflasi Provinsi Jawa Timur</h1>
    <h2 class="info-jatim-subtitle">Inflasi Provinsi Jawa Timur Tahun 2018-2025</h2>
    <h5 class="info-jatim-subtitle1">Pilih Tahun</h5>      
    """, unsafe_allow_html=True
    )

    
    df_inflasi = pd.read_csv("Inflasi (1).csv")
    df_inflasi.columns = ["tahun", "periode", "jumlah"]

    # Cleaning data
    df_inflasi["tahun"] = df_inflasi["tahun"].astype(int)

    df_inflasi["jumlah"] = (
        df_inflasi["jumlah"]
        .astype(str)
        .str.replace('"', '', regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )
    df_inflasi["periode"] = (
        df_inflasi["periode"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    # Definisi bulan
    bulan = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]

    # Set kategori
    # Set kategori
    df_inflasi["periode"] = pd.Categorical(
    df_inflasi["periode"],
    categories=bulan,
    ordered=True
)

    df_inflasi = df_inflasi.sort_values(["tahun", "periode"])

    tahun_inflasi = sorted(df_inflasi["tahun"].unique())

    def reset_tahun_inflasi():
        selected = st.session_state.filter_tahun_inflasi

        # Kalau semua pilihan dihapus/disilang, balik ke "Semua"
        if len(selected) == 0:
            st.session_state.filter_tahun_inflasi = ["Semua"]
            return

        # Ambil pilihan tahun saja, tanpa "Semua"
        tahun_dipilih = [t for t in selected if t != "Semua"]

        # Kalau "Semua" masih ada tapi user memilih tahun lain,
        # maka "Semua" otomatis dibatalkan
        if "Semua" in selected and len(tahun_dipilih) > 0:
            st.session_state.filter_tahun_inflasi = sorted(tahun_dipilih)
            return

        # Kalau semua tahun dipilih manual, otomatis jadikan "Semua"
        if set(tahun_dipilih) == set(tahun_inflasi):
            st.session_state.filter_tahun_inflasi = ["Semua"]
            return

        # Urutkan tahun manual
        st.session_state.filter_tahun_inflasi = sorted(tahun_dipilih)

    def reset_tahun_inflasi():
        selected = st.session_state.filter_tahun_inflasi

        tahun_dipilih = [t for t in selected if t != "Semua"]

        # Kalau semua pilihan disilang/kosong, balik ke "Semua"
        if len(selected) == 0:
            st.session_state.filter_tahun_inflasi = ["Semua"]
            return
        tahun_dipilih = [t for t in selected if t != "Semua"]
        # Kalau "Semua" dipilih bersama tahun lain, balik jadi hanya "Semua"
        if "Semua" in selected and len(selected) > 1:
            st.session_state.filter_tahun_inflasi = ["Semua"]
            return

        # Kalau semua tahun dipilih manual, otomatis ganti jadi "Semua"
        if set(tahun_dipilih) == set(tahun_inflasi):
            st.session_state.filter_tahun_inflasi = ["Semua"]
            return

        # Kalau pilih tahun manual, urutkan tahun
        st.session_state.filter_tahun_inflasi = sorted(tahun_dipilih)


    selected_tahun_inflasi = st.multiselect(
        "Pilih Tahun Inflasi",
        ["Semua"] + tahun_inflasi,
        default=["Semua"],
        key="filter_tahun_inflasi",
        on_change=reset_tahun_inflasi,
        label_visibility="collapsed"
)
    

    # Ambil hasil terbaru dari session_state
    selected_tahun_inflasi = st.session_state.filter_tahun_inflasi

    # Filter data dan label tahun
    if "Semua" in selected_tahun_inflasi:
        filtered_inflasi = df_inflasi
        label_tahun_inflasi = "Semua Tahun"
    else:
        selected_tahun_inflasi = sorted(selected_tahun_inflasi)

        filtered_inflasi = df_inflasi[
            df_inflasi["tahun"].isin(selected_tahun_inflasi)
        ]

        label_tahun_inflasi = ", ".join(map(str, selected_tahun_inflasi))


    if filtered_inflasi.empty:
        st.warning("Tidak ada data untuk tahun yang dipilih.")
    else:
        # Statistik
        rata_inflasi = filtered_inflasi["jumlah"].mean()

        max_inflasi = filtered_inflasi.loc[
            filtered_inflasi["jumlah"].idxmax()
        ]

        min_inflasi = filtered_inflasi.loc[
            filtered_inflasi["jumlah"].idxmin()
        ]

        # Layout grafik + box
        col_chart, col_info = st.columns([3, 1], gap="medium")

        with col_chart:
            fig = px.line(
                filtered_inflasi,
                x="periode",
                y="jumlah",
                color="tahun",
                markers=True,
                title="Grafik Inflasi Provinsi Jawa Timur"
            )


            fig.add_annotation(
            text="Sumber: BPS Jatim Tahun 2018-2025",
            xref="paper",
            yref="paper",
            x=0,
            y=-0.25,
            showarrow=False,
            font=dict(size=15, color="white"),
            align="left"
            )
            fig.update_layout(
                title_font=dict(size=15, color="white"),
                height=450,
                xaxis =dict(
                    title = dict(text="Bulan", font= dict(color="white")),
                    tickfont = dict(color="white")
                ),
                yaxis =dict(
                    title = dict(text="Inflasi(%)", font= dict(color="white")),
                    tickfont = dict(color="white")
                ),
                plot_bgcolor="#000000",
                paper_bgcolor="#000000",
                font=dict(color="white"),
            )
            
            
            st.plotly_chart(fig, use_container_width=True)

        with col_info:
            components.html(f"""
            <style>
            .inflasi-wrapper {{
                height: 450px;
                display: flex;
                flex-direction: column;
                gap: 12px;
                font-family: Arial, sans-serif;
            }}

            .inflasi-box {{
                background-color: #ff8c00;
                padding: 18px;
                border-radius: 12px;
                border: 1px solid #ffb366;
                text-align: center;
                flex: 1;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }}

            .inflasi-title {{
                font-size: 16px;
                font-weight: bold;
                color: white;
            }}

            .inflasi-value {{
                font-size: 30px;
                font-weight: bold;
                color: white;
            }}

            .inflasi-subvalue {{
                font-size: 16px;
                color: white;
            }}
            </style>

            <div class="inflasi-wrapper">

                <div class="inflasi-box">
                    <div class="inflasi-title">Rata-Rata Inflasi Berdasarkan {label_tahun_inflasi}</div>
                    <div class="inflasi-value">{rata_inflasi:.2f}%</div>
                </div>

                <div class="inflasi-box">
                    <div class="inflasi-title">Inflasi Tertinggi Berdasarkan {label_tahun_inflasi}</div>
                    <div class="inflasi-value">{max_inflasi["jumlah"]:.2f}%</div>
                    <div class="inflasi-subvalue">{max_inflasi["periode"]} {max_inflasi["tahun"]}</div>
                </div>

                <div class="inflasi-box">
                    <div class="inflasi-title">Inflasi Terendah Berdasarkan {label_tahun_inflasi}</div>
                    <div class="inflasi-value">{min_inflasi["jumlah"]:.2f}%</div>
                    <div class="inflasi-subvalue">{min_inflasi["periode"]} {min_inflasi["tahun"]}</div>
                </div>
            </div>
            """, height=470)

    #Inflasi Berdasarkan Kabupaten/Kota
    df_inflasi_kab = pd.read_csv("Inflasi Kab_Kota - Sheet1.csv")
    # Membersihkan kolom inflasi
    df_inflasi_kab["Inflasi (Persen)"] = (df_inflasi_kab["Inflasi (Persen)"]
                                         .astype(str)
                                         .str.replace(",",".", regex=False)
                                         .astype(float)
                                         )
    df_inflasi_kab["Tahun"] = df_inflasi_kab["Tahun"].astype(int)


    st.markdown("""
    <style>
    .info-jatim-title {
        color: #FFFFFF !important;
        font-size: 36px;
        font-weight: 800;
        margin-top: 500px;
        margin-bottom: 20px;
    }
    </style>
    <h1 class="info-jatim-title">Grafik Inflasi Tahunan</h1>
    """, unsafe_allow_html=True
    )


    # Filter tahun
    tahun_pilihan = st.selectbox(
        "Pilih Tahun",
        sorted(df_inflasi_kab["Tahun"].unique())
    )

    # Data berdasarkan tahun yang dipilih
    df_filter = df_inflasi_kab[df_inflasi_kab["Tahun"] == tahun_pilihan]
    nilai = df_filter["Inflasi (Persen)"]
    # Normalisasi warna
    norm = mcolors.Normalize(
        vmin=nilai.min(),
        vmax=nilai.max()
    )
    colors = plt.cm.RdYlGn(norm(nilai))
    
    # Grafik batang
    fig, ax = plt.subplots(figsize=(10, 5))
    # Background
    fig.patch.set_facecolor("#0E1117")   # background luar grafik
    ax.set_facecolor("#1B1F2A")          # background area plot
    
    # Bar chart
    bars = ax.bar(
        df_filter["Kabupaten/kota"],
        nilai,
        color=colors,
        edgecolor="none",
        linewidth=0
    )


    # Label nilai di atas batang
    for bar in bars:
        tinggi = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  # posisi x: tengah batang
            tinggi + 0.02,                      # posisi y: sedikit di atas batang
            f"{tinggi:.2f}%",                   # format label
            ha="center",
            va="bottom",
            color="white",
            fontsize=11,
            fontweight="bold"
        )
    # Judul dan label
    ax.set_title(
        f"Inflasi Kabupaten/Kota Tahun {tahun_pilihan}",
        color="white",
        fontsize=16,
        fontweight="bold",
        pad=15
    )

    ax.set_xlabel(
        "Kabupaten/Kota",
        color="white",
        fontsize=12,
        fontweight="bold"
    )

    ax.set_ylabel(
        "Inflasi (%)",
        color="white",
        fontsize=12,
        fontweight="bold"
    )

    # Warna teks sumbu
    ax.tick_params(axis="x", colors="white", rotation=35, labelsize=15)
    ax.tick_params(axis="y", colors="white", labelsize=15)

    # Grid horizontal
    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.25,
        color="white"
    )
    # Hilangkan garis pinggir yang tidak perlu
    for spine in ax.spines.values():
        spine.set_visible(False)
    # Supaya label tidak kepotong
    plt.tight_layout()

    fig.text(
    0.01, 0.01,
    "Sumber: BPS Jatim Tahun 2020-2025",
    ha="left",
    va="bottom",
    fontsize=10,
    color="white"
)
    st.pyplot(fig)
