import streamlit as st
import pickle
import pandas as pd
import numpy as np

# load trained pipeline
model = pickle.load(open('CarPricePredictionResale.pkl','rb'))

st.title("🚗 Used Car Price Predictor")

name = st.text_input("Car Name", "Hyundai Santro Xing")
company = st.text_input("Company", "Hyundai")
year = st.number_input("Year", 1990, 2025, 2015)
kms_driven = st.number_input("Kilometers Driven", 0, 300000, 50000)
fuel = st.selectbox("Fuel Type", ["Petrol","Diesel","CNG","LPG"])

if st.button("Predict Price"):
    
    # create dataframe
    input_df = pd.DataFrame([[name, company, year, kms_driven, fuel]],
                            columns=['name','company','year','kms_driven','fuel_type'])
    
    # 🔥 CLEAN INPUT (important for deployment)
    input_df = input_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
    try:
        prediction = np.exp(model.predict(input_df)[0])
        st.success(f"Estimated Price: ₹ {int(prediction):,}")
    
    except Exception as e:
        st.error("Prediction failed. Please check input values.")
        st.exception(e)