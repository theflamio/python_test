# Streamlit Cheatsheet

## Installation
pip install streamlit

## Run app
streamlit run app.py

---

## Basic structure
import streamlit as st

st.title("My App")
st.write("Hello world")

---

## Text / UI
st.title("Titel")
st.header("Header")
st.subheader("Subheader")
st.text("Clear text")
st.write("Smart output")
st.markdown("**Bold tekst** og *Italic*")

---

## Inputs
name = st.text_input("your name")
age = st.number_input("age", 0, 120)
value = st.slider("chose value", 0, 100, 50)
option = st.selectbox("chose", ["A", "B", "C"])

if st.button("click me"):
    st.write("Clicked")

---

## Layout
col1, col2 = st.columns(2)
col1.write("Left")
col2.write("Rigth")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Content 1")
with tab2:
    st.write("Content 2")

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
st.error("Error")
st.warning("Warning")
st.info("Info")

---

## Metrics
st.metric("Score", 87, delta=5)

---

## Sidebar
st.sidebar.title("Menu")
choice = st.sidebar.selectbox("Chose", ["A", "B"])

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
value = st.slider("chose number", 0, 100)
st.write("you chosed:", value)
