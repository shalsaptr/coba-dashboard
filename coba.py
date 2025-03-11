import streamlit as st
import pandas as pd

# Load data dari file Excel
@st.cache_data
def load_data():
    file_path = "D:\LATIHAN DASHBOARD SSH\coba dashboard SSH TUBAN.xlsx"  # Sesuaikan dengan lokasi file
    df = pd.read_excel(file_path, sheet_name=0)  # Pastikan sheet_name sesuai
    df.columns = df.columns.str.strip()  # Hapus spasi ekstra dari nama kolom
    return df

df = load_data()

# Buat Sidebar untuk Input Data
st.sidebar.header("Input Kode Barang")
kode_kelompok = st.sidebar.text_input("Masukkan Kode Kelompok Barang")
kode_barang = st.sidebar.text_input("Masukkan Kode Barang")

# Filter Data Berdasarkan Input
if kode_kelompok and kode_barang:
    hasil = df[
        (df["KODE KELOMPOK BARANG"] == kode_kelompok) & 
        (df["KODE BARANG"] == kode_barang)
    ]
    
    if not hasil.empty:
        # Menampilkan Data
        st.subheader("Detail Barang")
        st.write(f"**Uraian Kelompok Barang:** {hasil.iloc[0]['URAIAN KELOMPOK BARANG']}")
        st.write(f"**Uraian Barang:** {hasil.iloc[0]['URAIAN BARANG']}")
        
        # Menampilkan Spesifikasi dan Harga
        kolom_yang_dibutuhkan = ["SPESIFIKASI", "SATUAN", "HARGA SATUAN 2025", "SSH 2026"]
        st.subheader("Spesifikasi dan Harga")
        st.dataframe(hasil[kolom_yang_dibutuhkan])
    else:
        st.warning("Data tidak ditemukan. Cek kembali kode yang diinput.")
