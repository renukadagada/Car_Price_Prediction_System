import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("car_model.pkl","rb"))

st.title("Advanced Car Price Prediction System")

present_price = st.number_input("Showroom Price (in Lakhs)")
kms_driven = st.number_input("Kilometers Driven")

owner = st.selectbox("Number of Owners",[0,1,2,3])

fuel = st.selectbox(
"Fuel Type",
["Petrol","Diesel","CNG"]
)

seller = st.selectbox(
"Seller Type",
["Dealer","Individual"]
)

transmission = st.selectbox(
"Transmission",
["Manual","Automatic"]
)

car_age = st.number_input("Car Age (Years)")

fuel_val = ["Petrol","Diesel","CNG"].index(fuel)
seller_val = ["Dealer","Individual"].index(seller)
trans_val = ["Manual","Automatic"].index(transmission)

if st.button("Predict Price"):

    data = np.array([[
        present_price,
        kms_driven,
        owner,
        fuel_val,
        seller_val,
        trans_val,
        car_age
    ]])

    prediction = model.predict(data)

    st.success(
        f"Estimated Car Price: ₹ {prediction[0]:.2f} Lakhs"
    )