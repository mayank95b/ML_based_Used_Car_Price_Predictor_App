
import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image



pickle_in = open("Linear_regression.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_car_price(Year,Present_Price,Owner,kms_Driven):
    print(Year,Present_Price,Owner,kms_Driven)
    your_array = [[Year,Present_Price,Owner,kms_Driven]]
    your_array = np.asarray(your_array)
    your_array = your_array.astype(np.float64)
    prediction=classifier.predict(your_array)


    print(prediction)
    return prediction

def main():
    st.title("Second Hand Car Price Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Second Hand Car Price Predictor App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Year = st.text_input("Year","Type Here")
    Present_Price = st.text_input("Present_Price","Type Here")
    Owner = st.text_input("Owner","Type Here")
    kms_Driven = st.text_input("kms_Driven","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_car_price(Year,Present_Price,Owner,kms_Driven)
    st.success('The New Selling Price is  {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
