import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('Liver_Patient.sav', 'rb'))

st.title('Prediksi Pasien Penyakit Hati di India')
col1, col2 = st.columns(2)

with col1:
    Age = st.number_input('Umur Pasien')
    Total_Bilirubin = st.number_input(' jumlah Bilirubin dalam darah')
    Alkaline_Phosphotase = st.number_input('Fosfatase Alkalin')
    Aspartate_Aminotransferase = st.number_input('Asspartat Transaminase')
    Albumin = st.number_input('Albumin')

with col2:
    Gender = st.number_input('Jenis Kelamin Pasien')
    Direct_Bilirubin = st.number_input('Bilirubin Langsung (mg/dL)')
    Alamine_Aminotransferase = st.number_input('Transaminase Alanina')
    Total_Protiens = st.number_input('Jumlah Protein Pasien (g/dL)')
    Albumin_and_Globulin_Ratio = st.number_input('Jumlah Albumin dan Globulin Rasio')

predik = ''
if st.button('Hasil Prediksi'):
    predik = model.predict([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])

    if(predik[0] == 1):
        predik = 'Pasien memiliki Penyakit Liver'
    else:
        predik = 'Pasien tidak memiliki Penyakit Liver'
st.success(predik)