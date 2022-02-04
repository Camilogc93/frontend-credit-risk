import streamlit as st
st.title("hello")
st.write("ejemplo")
print("hola")

age = st.slider('Primera variable', 0, 130, 25)
st.write("I'm ", age, 'years old')

age = st.slider('Segunda variable', 0, 130, 25)
st.write("I'm ", age, 'years old')


age = st.slider('Tercera variable', 0, 130, 25)
st.write("I'm ", age, 'years old')

age = st.slider('Cuarta variable', 0, 130, 25)
st.write("I'm ", age, 'years old')

age = st.slider('Quinta variable', 0, 130, 25)
st.write("I'm ", age, 'years old')