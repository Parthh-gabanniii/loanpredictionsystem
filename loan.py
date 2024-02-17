import pickle
import sklearn
import pandas as pd
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

with open('df.pkl','rb') as file:
    df = pd.read_pickle(file)

with open('lr.pkl','rb') as file:
    lr = pd.read_pickle(file)



st.title('Loan')
Gender = st.selectbox('Gender (Mail = 1,Female = 0)',df['Gender'].unique())
Married = st.selectbox('married (Married = 1,Single = 0)',df['Married'].unique())
Dependents = st.selectbox('Dependents(Yes = 1,No=0)',df['Dependents'].unique())
Education = st.selectbox('Education(Graduate=1,Not Graduate=0)',df['Education'].unique())
Self_Employed = st.selectbox('Self_Employed(Yes=1,No=0)',df['Self_Employed'].unique())
ApplicantIncome = np.log(st.number_input('ApplicantIncome'))
CoapplicantIncome = np.log1p(st.number_input('income'))
LoanAmount = st.number_input('LoanAmount')
Loan_Amount_Term = st.selectbox('LoanAmount(Month)',df['Loan_Amount_Term'].unique())
Credit_History = st.selectbox('Credit_History',df['Credit_History'].unique())
Property_Area = st.selectbox('Property_Area(Urban = 1,Rural = 0)',df['Property_Area'].unique())

lr1 = lr.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
button = st.button("Predict")
if button:
    if lr1[0] == 1:
        st.subheader('Loan Approved')
    else:
        st.subheader('Loan Not Approved')

