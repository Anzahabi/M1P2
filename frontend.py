import streamlit as st
import requests

# Give the Name of the Application
st.title('Prediction Churn of Customer')

# Create Submit Form
with st.form(key='form_parameters'):
  
      
    
    
    tc = st.number_input('TotalCharges', min_value=18.8, step=0.02,max_value=8684.8)
    mc = st.number_input('MonthlyCharges', min_value=18.25, step=0.05,max_value=118.75)
    con = st.sidebar.selectbox(label='Contract', options=['Month-to-month','One year','Two year'])
    pm = st.sidebar.selectbox(label='PaymentMethod', options=['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
    ins = st.sidebar.selectbox(label='InternetService', options=['No','DSL','Fiber optic'])

    submitted = st.form_submit_button('Predict')

# inference
if submitted:
    URL = 'https://churn-fadhilsadeli.koyeb.app/predict'
    param = {'gender': g,
    'SeniorCitizen': s,
    'Partner': p,
    'Dependents': d,
    'tenure': t,
    'PhoneService': ps,
    'MultipleLines': ml,
    'InternetService': ins,
    'OnlineSecurity': ons,
    'OnlineBackup': onb,
    'DeviceProtection': dp,
    'TechSupport': ts,
    'StreamingTV': stv,
    'StreamingMovies':sm,
    'Contract': con,
    'PaperlessBilling': pb,
    'PaymentMethod': pm,
    'MonthlyCharges': mc,
    'TotalCharges': tc}

    r = requests.post(URL, json=param)
    if r.status_code == 200:
        res = r.json()
        st.title('Telco Customer Churn is {}'.format(res['label_names']))
    else:
        st.title("Unexpected Error")
        st.write(r.status_code)
