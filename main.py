import streamlit as st

st.title("Hitung Luas Persegi Panjang")

panjang = st.number_input ("nilai panjang", 0)
lebar = st.number_input ("nilai lebar", 0)
hitung = st.button ("Hitung")
