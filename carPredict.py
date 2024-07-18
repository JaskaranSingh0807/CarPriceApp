import streamlit as st
import pickle
# Load the model
model_path = "CarPrice.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def predict_price(features):
    # Ensure features are in the right shape for the model
    prediction = model[1].predict([features])
    return prediction[0]
    
st.title("Car Price Prediction")
year = st.slider('Year', 2006, 2023, 2010)
km_driven = st.number_input('Kilometers Driven', 0, 500000, 50000)
fuel = st.selectbox('Fuel Type', ['Diesel', 'Petrol','CNG'])
seller_type = st.selectbox('Seller Type', ['Individual', 'Trustmark Dealer', 'Dealer'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
owner = st.selectbox('Owner', ['First Owner','Test Drive Car', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'])
fuel_Diesel = 1 if fuel == "Diesel" else 0
fuel_Electric = 1 if fuel == "Electric" else 0
fuel_LPG= 1 if fuel == "LPG" else 0
fuel_Petrol= 1 if fuel == "Petrol" else 0
seller_I=1 if seller_type == "Individual" else 0
seller_T=1 if seller_type == "Trustmark Dealer" else 0
transmission_man=1 if transmission == "Manual" else 0
owner_s=1 if owner == "Second Owner" else 0
owner_t=1 if owner == "Third Owner" else 0
owner_f=1 if owner == "Fourth & Above Owner" else 0
owner_test=1 if owner == "Test Drive Car" else 0
features = [year,km_driven,fuel_Diesel,fuel_Electric,fuel_LPG,fuel_Petrol,seller_I,seller_T,transmission_man,owner_f,owner_s,owner_test,owner_t]
if st.button("Predict Selling Price"):
    prediction = predict_price(features)
    st.write(f"Predicted Selling Price: {prediction[0]} INR")
