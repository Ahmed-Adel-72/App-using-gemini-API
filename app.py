import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
google_api=os.getenv("google_api_key")

if google_api:
    genai.configure(api_key=google_api)
else:
    st.error("Api key is wrong")    


st.title("Fitness Bot ")


def calories_detect(age,height,weight,training_days,aim,gender):
    model=genai.GenerativeModel("gemini-pro")


    text=f"Now i will give you some info about me like age {age},weight{weight},height{height},training days (weekly){training_days} and my aim{aim} according to this info you should calculate the calories i should have ,training days i should train a week and diet (meals with grams and calories for each meal ) before this all you should look to my aim if it doesn't fit me you should tell me and don't calculate the calories or diet just tell me that it doesn't fit me and iam {gender}"
    response=model.generate_content(text)
    return response.text 


age=st.slider("Enter your age ", 8,80)
height=st.slider("Enter your height in cm", 140,210)
weight=st.slider("Enter your weight in kg", 20,150)
training_days=st.slider("Enter your training days in week", 0,7)
aim=st.selectbox("What's your aim ( Bulking , Maintaining , Cutting) ?",["Bulking","Maintaining","Cutting"])
gender=st.selectbox("Enter your gender",['Male','female'])

if st.button("Expected calories"):
    if age and height and weight  and aim:
        
        response = calories_detect(age, height, weight, training_days,aim,gender)
        st.session_state['response'] = response
        st.write(response)



