pip install openpyxl

import streamlit as st
import pandas as pd

# Load data dari file Excel
@st.cache_data
def load_data():
    file_path = "coba dashboard SSH TUBAN.xlsx"  # Sesuaikan dengan lokasi file
    try:
        df = pd.read_excel(file_path, sheet_name=0, engine="openpyxl")  # Pastikan sheet_name sesuai
        df.columns = df.columns.str.strip()  # Hapus spasi ekstra dari nama kolom
        return df
    except FileNotFoundError:
        st.error(f"File {file_path} tidak ditemukan. Pastikan file tersedia di lokasi yang benar.")
        return pd.DataFrame()  # Kembalikan DataFrame kosong jika file tidak ditemukan
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
        return pd.DataFrame()

df = load_data()

# Periksa apakah data berhasil dimuat
if df.empty:
    st.stop()  # Hentikan aplikasi jika tidak ada data yang dimuat

# Buat Sidebar untuk Input Data
st.sidebar.header("Input Kode Barang")
kode_kelompok = st.sidebar.text_input("Masukkan Kode Kelompok Barang")
kode_barang = st.sidebar.text_input("Masukkan Kode Barang")

# Filter Data Berdasarkan Input
if kode_kelompok and kode_barang:
    hasil = df[
        (df["KODE KELOMPOK BARANG"].astype(str) == kode_kelompok) & 
        (df["KODE BARANG"].astype(str) == kode_barang)
    ]
    
    if not hasil.empty:
        # Menampilkan Data
        st.subheader("Detail Barang")
        st.write(f"**Uraian Kelompok Barang:** {hasil.iloc[0]['URAIAN KELOMPOK BARANG']}")
        st.write(f"**Uraian Barang:** {hasil.iloc[0]['URAIAN BARANG']}")
        
        # Menampilkan Spesifikasi dan Harga
        kolom_yang_dibutuhkan = ["SPESIFIKASI", "SATUAN", "HARGA SATUAN 2025", "SSH 2026"]
        
        # Pastikan hanya menampilkan kolom yang tersedia
        kolom_valid = [col for col in kolom_yang_dibutuhkan if col in hasil.columns]
        
        if kolom_valid:
            st.subheader("Spesifikasi dan Harga")
            st.dataframe(hasil[kolom_valid])
        else:
            st.warning("Kolom spesifikasi dan harga tidak ditemukan dalam data.")
    else:
        st.warning("Data tidak ditemukan. Cek kembali kode yang diinput.")
