# import pickle
# import sklearn
# import pandas as pd
# import streamlit as st
# import numpy as np
# from sklearn.linear_model import LinearRegression
#
# with open('df.pkl','rb') as file:
#     df = pd.read_pickle(file)
#
# with open('lr.pkl','rb') as file:
#     lr = pd.read_pickle(file)
#
#
#
# st.title('Loan Predection System')
# Gender = st.selectbox('Gender (Mail = 1,Female = 0)',df['Gender'].unique())
# Married = st.selectbox('married (Married = 1,Single = 0)',df['Married'].unique())
# Dependents = st.selectbox('Dependents(Yes = 1,No=0)',df['Dependents'].unique())
# Education = st.selectbox('Education(Graduate=1,Not Graduate=0)',df['Education'].unique())
# Self_Employed = st.selectbox('Self_Employed(Yes=1,No=0)',df['Self_Employed'].unique())
# ApplicantIncome = np.log(st.number_input('ApplicantIncome', min_value=0.01))
# CoapplicantIncome = np.log1p(st.number_input('income', min_value=0.01))
# LoanAmount = st.number_input('LoanAmount')
# Loan_Amount_Term = st.selectbox('LoanAmount(Month)',df['Loan_Amount_Term'].unique())
# Credit_History = st.selectbox('Credit_History',df['Credit_History'].unique())
# Property_Area = st.selectbox('Property_Area(Urban = 1,Rural = 0)',df['Property_Area'].unique())
# if (ApplicantIncome == 0.00) & (CoapplicantIncome == 0.00):
#     print('Income cannot be 0')
# else:
#     lr1 = lr.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
#     button = st.button("Predict")
#     if button:
#         if lr1[0] == 1:
#             st.subheader('Loan Approved')
#         else:
#             st.subheader('Loan Not Approved')
#
import pickle
import sklearn
import pandas as pd
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Set the page width to a fixed value
st.set_page_config(layout="wide")

with open('df.pkl','rb') as file:
    df = pd.read_pickle(file)

with open('lr.pkl','rb') as file:
    lr = pd.read_pickle(file)

st.title('Loan Predection System')

# Define the columns for input selectors
col1, col2, col3 = st.columns(3)

# Place each input selector in the respective column
with col1:
    Gender = st.selectbox('Gender (Mail = 1,Female = 0)',df['Gender'].unique())

with col2:
    Married = st.selectbox('married (Married = 1,Single = 0)',df['Married'].unique())

with col3:
    Dependents = st.selectbox('Dependents(Yes = 1,No=0)',df['Dependents'].unique())

# Define the columns for input selectors
col4, col5, col6 = st.columns(3)

# Place each input selector in the respective column
with col4:
    Education = st.selectbox('Education(Graduate=1,Not Graduate=0)',df['Education'].unique())

with col5:
    Self_Employed = st.selectbox('Self_Employed(Yes=1,No=0)',df['Self_Employed'].unique())

with col6:
    ApplicantIncome = np.log(st.number_input('ApplicantIncome', min_value=0.01))

# Define the columns for input selectors
col7, col8, col9 = st.columns(3)

# Place each input selector in the respective column
with col7:
    CoapplicantIncome = np.log1p(st.number_input('CoapplicantIncome', min_value=0.01))

with col8:
    LoanAmount = st.number_input('LoanAmount')

with col9:
    Loan_Amount_Term = st.selectbox('LoanAmount(Month)',df['Loan_Amount_Term'].unique())

# Define the columns for input selectors
col10, col11, col12 = st.columns(3)

# Place each input selector in the respective column
with col10:
    Credit_History = st.selectbox('Credit_History',df['Credit_History'].unique())

with col11:
    Property_Area = st.selectbox('Property_Area(Urban = 1,Rural = 0)',df['Property_Area'].unique())

# Center the "Predict" button and increase its size


if col12.button("Predict"):
    lr1 = lr.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
    if lr1[0] == 1:
        st.subheader('Loan Approved')
    else:
        st.subheader('Loan Not Approved')


