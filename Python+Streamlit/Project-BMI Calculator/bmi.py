import pandas as pd
import streamlit as st


st.title("BMI Calcualtor")

height = st.slider("Enter your height(in cm):", 100,250,175)
weight = st.slider("Enter your weight (in kg):",40,200,70)

bmi = weight / ((height/100)** 2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Category ###")
st.write ("- Underweight: BMI less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI 30 or greater")