import streamlit as st
import pickle
import numpy as np

st.title("🚗 Car Price Prediction")

# Load model
model = pickle.load(open("car_model.pkl","rb"))

present_price = st.number_input("Present Price (Lakhs)")
kms_driven = st.number_input("Kilometers Driven")

owner = st.selectbox("Owner",[0,1,2,3])

fuel_type = st.selectbox("Fuel Type",["Petrol","Diesel","CNG"])
seller_type = st.selectbox("Seller Type",["Dealer","Individual"])
transmission = st.selectbox("Transmission",["Manual","Automatic"])

car_age = st.number_input("Car Age")

fuel_map = {"Petrol":0,"Diesel":1,"CNG":2}
seller_map = {"Dealer":0,"Individual":1}
trans_map = {"Manual":0,"Automatic":1}

fuel = fuel_map[fuel_type]
seller = seller_map[seller_type]
trans = trans_map[transmission]

if st.button("Predict Price"):

    prediction = model.predict([[present_price,kms_driven,owner,fuel,seller,trans,car_age]])

    st.success(f"Estimated Selling Price: {prediction[0]:.2f} Lakhs")
