# MENENTUKAN KUALITAS UDARA DALAM DATASET SETIAP TAHUNYA - 10122336 - M Taufik Iqbal
# Berapa rata-rata suhu pada daerah tersebut - 10122333 - Hisyam Rizqullah
# POLUSI UDARA PERTAHUN - 10122476 - Farrel Muhammad A
# Bagaimana tingkat polutan udara, seperti PM2.5 dan SO2, berfluktuasi selama periode waktu tertentu di suatu wilayah - 10122343 indra permana
# Bagaimana tingkat ozon disetiap bulan pada tahun 2013 di wilayah ini? - 10122327- Danarusmia
# Berapa rata rata debit hujan Pertahunnya - 10122325 - Alka Sabil Khubaib

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu


@st.cache_data
#load data Csv
def load_data(url):
    df = pd.read_csv(url)
    return df

def analisa_kualitas_udara(df_air_quality) :
    #mengambil data kualitas udara pertahun
    st.subheader('Rata-rata kualitas udara per Tahun')
    average_CO_per_year = df_air_quality.groupby('year')['CO'].mean()
    st.write(average_CO_per_year)

    #membuat chart kualittas udara pertahun
    plt.figure(figsize=(10, 6))
    plt.bar(average_CO_per_year.index, average_CO_per_year.values, color='skyblue')
    plt.title('Rata-rata Kualitas Udara per Tahun')
    plt.xlabel('Tahun')
    plt.ylabel('Rata-rata CO')
    plt.grid(axis='y')
    plt.xticks(average_CO_per_year.index)
    st.pyplot(plt)

    with st.expander("Penjelasan Mengenai Grafik Di atas") :
        st.write("Kita bisa melihat kualitas udara setiap tahunnya berdasarkan grafik diatas. kualitas udarapun sangat penting dalam meningkatkan kesejahteraan etnah itu masyarakat, pelanggan, dan karyawan. menilai kualias udara berdasarkan CO dapat membantu mengidentifikasi dan mengurangi sumber polusi dilingkungan kerja dan data ini pun dapat membantu bisnis untuk menyediakan ventilasi yang baik dan dapat berkontribusi dalam upaya pelestarian lingkungan dan pengurangan emisi gas rumah kaca")

    #memngambil data suhu pertahun
    st.header('Rata-rata Suhu per Tahun')
    avg_temp_per_year = df_air_quality.groupby('year')['TEMP'].mean()
    st.write(avg_temp_per_year)

    #membuat chart kualittas udara pertahun
    plt.figure(figsize=(10, 6))
    plt.plot(avg_temp_per_year.index, avg_temp_per_year.values, marker='o', color='skyblue', label='Rata-rata Suhu')
    plt.fill_between(avg_temp_per_year.index, avg_temp_per_year.values, color='skyblue', alpha=0.3)
    plt.title('Rata-rata Suhu per Tahun')
    plt.xlabel('Tahun')
    plt.ylabel('Rata-rata Suhu')
    plt.grid(True)
    plt.legend()
    plt.xticks(avg_temp_per_year.index)
    st.pyplot(plt)

    with st.expander("Penjelasan Mengenai Rata-rata Suhu Pertahun") :
        st.write("Sesuai dengan perhitungan rata” suhu pada daerah changping dari tahun ke tahun berada di sekitar 11° C")

def analisa_polusi_udara_dan_fluktuasi (df_air_quality):

    st.header('Polusi Udara dan Fluktuasi')
    
    #mengambil data polusi pertahun
    st.subheader('Fluktuasi pertahun')
    df_PM25_mean= df_air_quality.groupby('year')['PM2.5'].mean()
    average_Pm25_per_year_reversed = df_PM25_mean.sort_index(ascending=False)
    average_Pm25_per_year_reversed

    #membuat line char dari data polusi pertahun
    # Membuat line chart
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot line chart dari data rata-rata polusi per tahun
    ax.plot(average_Pm25_per_year_reversed.index, df_PM25_mean, marker='o',color='red')

    # Memberikan judul dan label sumbu
    ax.set_title('Rata-rata Polusi Per Tahun')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Rata-rata Polusi')

    # Menyusun formatter untuk sumbu x agar menampilkan tahun tanpa koma
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0f}'.format(x)))

    # Menambahkan grid
    plt.grid(True)

    # Tampilkan plot
    st.pyplot(fig)

    with st.expander("Penjelasan Mengenai Polusi Udara per tahunnya ") :
        st.write("berdasarkan grafik pertanyaan nomor 3 dapat disimpulkan bahwa, tingkat polusi udara(pm2.5) pertahun di daerah tersebut rata rata di atas ambang maksimal yang seharusnya di bawah 65, sebagaimana jika di atas 65 maka dikatakan berbahaya bagi tubuh mahluk hidup di daerah tersebut")

    # mengambil data untuk fluktuasi pm2.5 dan SO2
    st.subheader('Fluktuasi PM2.5 dan SO2')
    df_PM25_mean= df_air_quality.groupby('year')['PM2.5'].mean()
    df_SO2_mean = df_air_quality.groupby('year')['SO2'].mean()
    average_Pm25_per_year_reversed = df_PM25_mean.sort_index(ascending=False)
    average_SO2_per_year_reversed = df_SO2_mean.sort_index(ascending=False)
    average_Pm25_per_year_reversed
    average_SO2_per_year_reversed

    #membuat visualisasi untuk fluktuasi pm2.5 dan SO2
    fig, ax = plt.subplots()
    df_air_quality.groupby('year')['PM2.5'].mean().plot(ax=ax, label='PM2.5')
    df_air_quality.groupby('year')['SO2'].mean().plot(ax=ax, label='SO2')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Kadar Polutan')
    ax.legend()
    st.pyplot(fig)

    with st.expander("Fluktuasi PM2.5 dan SO2") :
        st.write("Tingkat fluktuasi polutan udara, dengan rata-rata PM2.5 mencapai 400 (tertinggi 800 pada jam 4) dan SO2 sekitar 100 (tertinggi 300 pada jam 5), menciptakan kondisi udara yang berpotensi berbahaya.Fluktuasi tingkat polutan tersebut menciptakan kualitas udara yang buruk, yang dapat menyebabkan penurunan kualitas hidup secara keseluruhan.")
    
    # Analisis tingkat ozon per bulan tahun 2013
    st.subheader('Tingkat Ozon per Bulan Tahun 2013')
    ozone_2013 = df_air_quality[df_air_quality['year'] == 2013].groupby('month')['O3'].mean()
    st.write(ozone_2013)

    # Membuat plot
    plt.figure(figsize=(10,6))
    plt.plot(ozone_2013.index, ozone_2013.values, marker='o')
    plt.title('Tingkat Ozon per Bulan Tahun 2013')
    plt.xlabel('Bulan')
    plt.ylabel('Tingkat Ozon')
    plt.grid(True)

    # Menampilkan plot di Streamlit
    st.pyplot(plt)

    with st.expander("Penjelasan Tingkat Ozon per Bulan Tahun 2013"):
        st.write("Berdasarkan grafik di atas, dapat disimpulkan bahwa tingkat ozon(O3) setiap bulan per tahun 2013 tertinggi di changping berada di bulan 10")

    
    # Rata-rata debit hujan per tahun
    st.subheader('Rata-rata Debit Hujan per Tahun')
    avg_rainfall_per_year = df_air_quality.groupby('year')['RAIN'].mean()
    st.write(avg_rainfall_per_year)

    # Membuat grafik rata rata debit hujan
    plt.figure(figsize=(10, 6))
    plt.plot(avg_rainfall_per_year.index, avg_rainfall_per_year.values, marker='o')
    plt.title('Rata-rata Debit Hujan Pertahun')
    plt.xlabel('Tahun')
    plt.ylabel('Rata-rata Debit Hujan')
    plt.grid(True)
    st.pyplot(plt)
    
    with st.expander ("Penjelasan Debit Hujan Per Tahun") :
        st.write("Berdasarkan grafik yang tertera pada pertanyaan nomor 6 debit hujan pertahun ada perubahan signifikan yang mana pada awal tahun mengalami debit hujan yang lumayan tinggi dan pada pertengahan tahun ada nya penurunan debit hujan yang sangat besar dan pada akhir tahun mengalami kenaikan debit hujan yang tinggi bisa kita simpul kan bahwa akan tidak akan banyak terjadinya banjir pada perusahaan")


df_PRSA_Data_Changping = load_data("https://raw.githubusercontent.com/MrShel00/UAS/main/Tugas%20Uas/PRSA_Data_Changping.csv")

with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)
    
if (selected == 'Dashboard') :
    st.header(f"Dashboard Analisis Air Quality")
    tab1,tab2 = st.tabs(["Analisis Kualitas Udara", "Analisi Polusi dan Fluktusi"])

    with tab1 :
        df_air_quality = df_PRSA_Data_Changping
        analisa_kualitas_udara(df_air_quality)
    with tab2 :
        analisa_polusi_udara_dan_fluktuasi(df_air_quality)

