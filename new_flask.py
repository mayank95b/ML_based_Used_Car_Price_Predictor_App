from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("Linear_regression.pkl","rb")
lm=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_car_price():

    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Year
        in: query
        type: number
        required: true
      - name: Present_Price
        in: query
        type: number
        required: true
      - name: Owner
        in: query
        type: number
        required: true
      - name: kms_Driven
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
    Year=request.args.get("Year")
    Present_Price=request.args.get("Present_Price")
    Owner=request.args.get("Owner")
    kms_Driven=request.args.get("kms_Driven")
    your_array = [[Year,Present_Price,Owner,kms_Driven]]
    your_array = np.asarray(your_array)
    your_array = your_array.astype(np.float64)
    prediction=lm.predict(your_array)
    print(prediction)
    return "The New Selling Price is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_car_price_file():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true

    responses:
        200:
            description: The output values

    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=lm.predict(df_test)

    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
