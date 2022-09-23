import numpy as np
import pickle
import joblib
import time
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    SeniorCitizen = 0
    if 'SeniorCitizen' in request.form:
        SeniorCitizen = 1
    Partner = 0
    if 'Partner' in request.form:
        Partner = 1
    Dependents = 0
    if 'Dependents' in request.form:
        Dependents = 1
    PaperlessBilling = 0
    if 'PaperlessBilling' in request.form:
        PaperlessBilling = 1

    MonthlyCharges = int(request.form["MonthlyCharges"])

    def tenure(t):
        if t<=12:
            return 1
        elif t>12 and t<=24:
            return 2
        elif t>24 and t<=36:
            return 3
        elif t>36 and t<=48:
            return 4
        elif t>48 and t<=60:
            return 5
        else:
            return 6

    tenure_group = tenure(int(request.form["Tenure"]))

    InternetService_Fiberoptic = 0
    InternetService_No = 0
    if request.form["InternetService"] == 0:
        InternetService_No = 1
    elif request.form["InternetService"] == 2:
        InternetService_Fiberoptic = 1


    OnlineSecurity_Yes = 0
    if request.form["OnlineSecurity"] == 1:
        OnlineSecurity_Yes = 1

    OnlineBackup_Yes = 0
    if request.form["OnlineBackup"] == 1:
        OnlineBackup_Yes = 1

    DeviceProtection_Yes = 0
    if request.form["DeviceProtection"] == 1:
        DeviceProtection_Yes = 1

    TechSupport_Yes = 0
    if request.form["TechSupport"] == 1:
        TechSupport_Yes = 1

    StreamingTV_Yes = 0
    if request.form["StreamingTV"] == 1:
        StreamingTV_Yes = 1

    StreamingMovies_Yes = 0
    if request.form["StreamingMovies"] == 1:
        StreamingMovies_Yes = 1

    Contract_Oneyear = 0
    Contract_Twoyear = 0
    if request.form["Contract"] == 1:
        Contract_Oneyear = 1
    elif request.form["Contract"] == 2:
        Contract_Twoyear = 1

    PaymentMethod_CreditCard = 0
    PaymentMethod_ElectronicCheck = 0
    PaymentMethod_MailedCheck = 0
    if request.form["PaymentMethod"] == 1:
        PaymentMethod_CreditCard = 1
    elif request.form["PaymentMethod"] == 2:
        PaymentMethod_ElectronicCheck = 1
    elif request.form["PaymentMethod"] == 3:
        PaymentMethod_MailedCheck = 1

    features = [SeniorCitizen, Partner, Dependents, PaperlessBilling, 
                   MonthlyCharges, tenure_group,
                   InternetService_Fiberoptic, InternetService_No, 
                   OnlineSecurity_Yes,  OnlineBackup_Yes, DeviceProtection_Yes,
                   TechSupport_Yes, StreamingTV_Yes, StreamingMovies_Yes,
                   Contract_Oneyear,Contract_Twoyear,PaymentMethod_CreditCard, 
                   PaymentMethod_ElectronicCheck, PaymentMethod_MailedCheck]

    columns = ['SeniorCitizen', 'Partner', 'Dependents', 'PaperlessBilling', 
                    'MonthlyCharges', 'tenure_group', 
                    'InternetService_Fiber optic', 'InternetService_No',  
                    'OnlineSecurity_Yes',  'OnlineBackup_Yes', 'DeviceProtection_Yes',  
                    'TechSupport_Yes',  'StreamingTV_Yes', 'StreamingMovies_Yes', 
                    'Contract_One year', 'Contract_Two year', 
                    'PaymentMethod_Credit card (automatic)', 
                    'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']

    final_features = [np.array(features)]
    prediction = model.predict_proba(final_features)


    output = prediction[0,1]
   
    t = time.time()
    return render_template('index.html', prediction_text='The Probability of customer churn: {}'.format(round(output, 2)))

if __name__ == "__main__":
    app.run()
