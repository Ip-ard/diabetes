import streamlit as st

from web_functions import predict

def app(dataset, x, y):

    st.title('Halaman Prediksi Diabetes')

    # col1, col2, col3 = st.columns(3)

    Pregnancies = st.text_input ('Input Nilai Kehamilan')
    Glucose = st.text_input ('Input Nilai Glukosa')
    BloodPressure = st.text_input ('Input Nilai Tekanan Darah')
    BMI = st.text_input ('Input Nilai BMI')
    Age = st.text_input ('Input Nilai Usia')

    features = [Pregnancies,Glucose,BloodPressure,BMI,Age]

    # tombol prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x,y,features)
        score = score
        st.info("Prediksi Sukses...")

        if (prediction == 1):
            st.warning("Orang Tersebut Terkena Penyakit Diabetes")
        else:
            st.success("Orang Tersebut Aman Dari Penyakit Diabetes")

        st.write("Model Yang Digunakan Memiliki Tingkat Akurasi ", (score*100),"%")