import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.sav')

st.title('Sales Prediction App')
st.write('This app predicts sales based on TV, Radio, and Newspaper advertising budgets.')

# Input fields
tv = st.number_input('TV Budget ($)', min_value=0.0, value=150.0, step=1.0)
radio = st.number_input('Radio Budget ($)', min_value=0.0, value=25.0, step=1.0)
newspaper = st.number_input('Newspaper Budget ($)', min_value=0.0, value=25.0, step=1.0)

# Predict button
if st.button('Predict Sales'):
    features = np.array([[tv, radio, newspaper]])
    prediction = model.predict(features)[0]
    st.success(f'Predicted Sales: {prediction:.2f} units')
