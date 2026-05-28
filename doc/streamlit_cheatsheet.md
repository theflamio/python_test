# Streamlit Cheatsheet

## Installation
pip install streamlit

## Run app
streamlit run app.py

---

## Basic structure
import streamlit as st

st.title("Min App")
st.write("Hej verden")

---

## Text / UI
st.title("Titel")
st.header("Header")
st.subheader("Subheader")
st.text("Ren tekst")
st.write("Smart output")
st.markdown("**Fed tekst** og *kursiv*")

---

## Inputs
name = st.text_input("Dit navn")
age = st.number_input("Alder", 0, 120)
value = st.slider("Vælg værdi", 0, 100, 50)
option = st.selectbox("Vælg", ["A", "B", "C"])

if st.button("Klik mig"):
    st.write("Klikket")

---

## Layout
col1, col2 = st.columns(2)
col1.write("Venstre")
col2.write("Højre")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Indhold 1")
with tab2:
    st.write("Indhold 2")

---

## Data
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})

st.dataframe(df)

---

## Charts
st.line_chart(df)
st.bar_chart(df)

---

## Status
st.success("OK")
st.error("Fejl")
st.warning("Advarsel")
st.info("Info")

---

## Metrics
st.metric("Score", 87, delta=5)

---

## Sidebar
st.sidebar.title("Menu")
choice = st.sidebar.selectbox("Vælg", ["A", "B"])

---

## File upload
file = st.file_uploader("Upload fil")
if file:
    st.write(file.name)

---

## Caching
@st.cache_data
def load_data():
    return expensive_function()

---

## Example app
import streamlit as st

st.title("Demo App")
value = st.slider("Vælg tal", 0, 100)
st.write("Du valgte:", value)
