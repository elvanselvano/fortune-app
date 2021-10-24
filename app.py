import streamlit as st
import pickle
import sklearn

#title & layout
st.set_page_config(page_title = "Fortune", layout = "wide")

#read pickle
fortune_model = pickle.load(open('finalized_model.pkl','rb'))

#sidebar
sidebar_description = st.sidebar.title("Fill your Information")
sidebar_age = st.sidebar.slider("Age", 17, 60)
sidebar_income = st.sidebar.number_input(label="Income", min_value=0, max_value=12000000, value=1000000, step=10000)
sidebar_job = st.sidebar.selectbox("Job", ("College Student","Employee","Businessman"))
sidebar_marital = st.sidebar.selectbox("Marital Status", ("Not Married","Married"))
sidebar_residence = st.sidebar.selectbox("Residence", ("House","Boarding House"))

#content
st.title("Welcome to Fortune")
st.markdown("""
    * Here you can find Information about how to split your money correctly based on your personal information
    * Please fill your information on the left side of the application
""")
st.header("Prediction Calculation")
st.markdown("""
    Press the predict button below to know your result!
""")

# marital status = notmarried(0),married(1) ; job = businessman(0),college(1),employee(2) ; residence = boarding(0), house(1)

#parameter marital
if sidebar_marital == "Not Married":
    marital_number = 0
else :
    marital_number = 1

#parameter job
if sidebar_job == "Businessman":
    job_number = 0
elif sidebar_job == "College Student":
    job_number = 1
else :
    job_number = 2

#parameter residence
if sidebar_residence == "Boarding House":
    residence_number = 0
else :
    residence_number = 1


#print prediction
result = fortune_model.predict([[sidebar_age, sidebar_income, marital_number, job_number, residence_number]])

if st.button('Predict'):
    if result == 1:
        consumption_calculation = sidebar_income * 0.75
        savings_calculation = sidebar_income * 0.15
        investment_calculation = sidebar_income * 0.1
        st.markdown(f"""
        From our prediction, we conclude you must split your income into this : 
        * 75% for Consumption = Rp{round(consumption_calculation):,}
        * 15% for Savings = Rp{round(savings_calculation):,}
        * 10% for Investment = Rp{round(investment_calculation):,}
        """)
    elif result == 2:
        consumption_calculation = sidebar_income * 0.65
        savings_calculation = sidebar_income * 0.2
        investment_calculation = sidebar_income * 0.15
        st.markdown(f"""
        From our prediction, we conclude you must split your income into this : 
        * 65% for Consumption = Rp{round(consumption_calculation):,}
        * 20% for Savings = Rp{round(savings_calculation):,}
        * 15% for Investment = Rp{round(investment_calculation):,}
        """)
    elif result == 3:
        consumption_calculation = sidebar_income * 0.6
        savings_calculation = sidebar_income * 0.25
        investment_calculation = sidebar_income * 0.15
        st.markdown(f"""
        From our prediction, we conclude you must split your income into this : 
        * 60% for Consumption = Rp{round(consumption_calculation):,}
        * 25% for Savings = Rp{round(savings_calculation):,}
        * 15% for Investment = Rp{round(investment_calculation):,}
        """)
    elif result == 4:
        consumption_calculation = sidebar_income * 0.55
        savings_calculation = sidebar_income * 0.3
        investment_calculation = sidebar_income * 0.15
        st.markdown(f"""
        From our prediction, we conclude you must split your income into this : 
        * 55% for Consumption = Rp{round(consumption_calculation):,}
        * 30% for Savings = Rp{round(savings_calculation):,}
        * 15% for Investment = Rp{round(investment_calculation):,}
        """)
    else :
        consumption_calculation = sidebar_income * 0.4
        savings_calculation = sidebar_income * 0.3
        investment_calculation = sidebar_income * 0.3
        st.markdown(f"""
        From our prediction, we conclude you must split your income into this : 
        * 40% for Consumption = Rp{round(consumption_calculation):,}
        * 30% for Savings = Rp{round(savings_calculation):,}
        * 30% for Investment = Rp{round(investment_calculation):,}
        """)
