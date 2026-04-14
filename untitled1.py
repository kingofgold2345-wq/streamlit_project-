import streamlit as st

st.title("test")

name = st.text_input("ادخل اسمك")
age = st.number_input("ادخل عمرك")
gender = st.selectbox("ولد او بنت", ("male", "female"))

st.write("اهلا بك", name)

st.balloons()

st.snow()
