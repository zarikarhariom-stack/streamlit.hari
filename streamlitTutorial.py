import streamlit as st
import pandas as pd
import numpy as np
 
st.title("Hello gpt")
name = st.text_input("Ask your question")

st.write("this is your 1st streamlit app")
st.text("lets get started")

name = st.text_input("Enter your name")
if st.button("Great"):
    st.success(f"Hello, {name}")
    
#allow to upload a csv file 
    
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        
        
st.header("this is header")
st.subheader("this is subheader")
st.markdown("Link(https://streamlit.io/)")
st.text_area("pick a number")
st.number_input('pick a number', min_value=0, max_value=10)
st.slider("choose a range",0,100)
st.selectbox("select a fruit",["apple","banana","mango"])
st.multiselect("select language",["python","java","c++"])
st.radio("pick one",["option1","option2"])
st.checkbox("I agree terms and conditions")       

if st.checkbox("show details"):
    st.text("here are more details")
    
#reform tag
with st.form("login form"):
    username = st.text_input("Enter username")
    password = st.text_input("passsword", type="password")
    submited = st.form_submit_button("login")
    
    if submited:
        st.success(f"Welcome ,{username}")
        
df = pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

st.video("https://www.youtube.com/watch?v=dlPHrD0p_uE")
st.image(
    "https://upload.wikimedia.org/wikipedia/en/9/91/Iron_Man_action_figure.jpg",
    caption="Iron Man")

