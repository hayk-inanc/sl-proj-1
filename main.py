import streamlit as st


st.title("Калькулятор!")

val_1 = st.number_input("Insert a number", key="val_1")
val_2 = st.number_input("Insert a number", key="val_2")

st.write(f"Результат: {val_1 + val_2}")