#import library yang dibutuhkan

import streamlit as st
from web_functions import load_data

from Tabs import home, predict, visualise

Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "Visualisation" : visualise
}

# Membuat Sidebar
st.sidebar.title("Navigasi")

# Membuat Radio Option
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Load Dataset
dataset, x, y = load_data()

# Konsidi Call App Fuction
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(dataset,x,y)
else:
    Tabs[page].app()