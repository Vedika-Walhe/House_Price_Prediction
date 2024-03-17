import streamlit as st
import pandas as pd
import pickle

data = pickle.load(open('House_data_model.pkl','rb'))

df = pd.read_csv('Cleaned_data.csv')
zipcode = df['zipcode'].unique()
print(zipcode)

st.title('House Price Prediction')

sel_zipcode = st.selectbox(
    'Enter the zipcode of your area',
    zipcode)

sel_bedrooms = st.number_input('Enter the number of bedrooms:' ,value = 0,step = 1)
sel_bathrooms = st.number_input('Enter the number of bathrooms:' ,value = 0,step = 1)

sel_sqft_living = st.text_input('Enter the area of living room in square feet:')
sel_sqft_living = int(sel_sqft_living) if sel_sqft_living.isdigit() else 0

sel_sqft_lot = st.text_input('Enter the area of the lot in square feet:')
sel_sqft_lot = int(sel_sqft_lot) if sel_sqft_lot.isdigit() else 0

sel_floor = st.number_input('Enter the floor number:',value=0,step=1)

sel_year = st.number_input('Enter the construction year of the building:',min_value = 1900,max_value=2023 , value = 2023, step=1)

sel_apb = sel_sqft_lot / sel_bedrooms if (sel_bedrooms!=0) else sel_sqft_lot

# st.button('Predict the price')

if st.button('Predict the price'):
    user_data = {
        'bedrooms' : sel_bedrooms,
        'bathrooms' : sel_bathrooms,
        'sqft_living' : sel_sqft_living,
        'sqft_lot' : sel_sqft_lot,
        'floors' : sel_floor,
        'yr_built' : sel_year,
        'zipcode' : sel_zipcode,
        'area_per_bhk' : sel_apb
    }

    user_input = pd.DataFrame([user_data])

    if data:
        predicted_price = data.predict(user_input)
        st.write('Predicted Price:', predicted_price[0])