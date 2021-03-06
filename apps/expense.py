import streamlit as st
import matplotlib.pyplot as plt

def app():
    
    #sidebar
    st.sidebar.title("Your Income")
    sidebar_monthIncome = st.sidebar.number_input(label="Monthly Pay", min_value=0, value=0, step=500000)
    sidebar_monthOtherIncome = st.sidebar.number_input(label="Other Monthly Income (alimony, pensions, child support, etc)", min_value=0, value=0, step=500000)
    
    st.sidebar.title("Your Expense")
    sidebar_houseExpense = st.sidebar.number_input(label="Housing (electricity, internet, maintenance, etc)", min_value=0, value=0, step=500000)
    sidebar_transportExpense = st.sidebar.number_input(label="Transportation (gasoline, parking, service maintenance, etc)", min_value=0, value=0, step=500000)
    sidebar_foodExpense = st.sidebar.number_input(label="Food", min_value=0, value=0, step=500000)
    sidebar_healthExpense = st.sidebar.number_input(label="Health (insurance, prescription, etc)", min_value=0, value=0, step=500000)
    sidebar_childExpense = st.sidebar.number_input(label="Children (school, allowance, etc)", min_value=0, value=0, step=500000)
    sidebar_wifeExpense = st.sidebar.number_input(label="Wife (clothing, allowance, gift, etc)", min_value=0, value=0, step=500000)
    sidebar_selfExpense = st.sidebar.number_input(label="Self (hobby, pet, donation, etc)", min_value=0, value=0, step=500000)
    sidebar_installmentExpense = st.sidebar.number_input(label="Installment (house, car, etc)", min_value=0, value=0, step=500000) 

    st.sidebar.title("Your Saving")
    sidebar_emergencySaving = st.sidebar.number_input(label="Emergency", min_value=0, value=0, step=500000)
    sidebar_retirementSaving =st.sidebar.number_input(label="Retirement", min_value=0, value=0, step=500000)
    sidebar_otherSaving =  st.sidebar.number_input(label="Others", min_value=0, value=0, step=500000)

    #content
    st.header("Expense Calculator")
    st.markdown("""
        Easy way to count your monthly expense with Fortune, fill your income and expense on the left bar to see the result.
    """)



    #print calculator and pie chart (kalo bisa bikin reset button)
    total_income = sidebar_monthIncome + sidebar_monthOtherIncome
    total_expense = sidebar_houseExpense + sidebar_transportExpense + sidebar_foodExpense + sidebar_healthExpense + sidebar_childExpense + sidebar_wifeExpense + sidebar_selfExpense + sidebar_installmentExpense
    total_saving = sidebar_emergencySaving + sidebar_retirementSaving + sidebar_otherSaving
    calculator_result = total_income - total_expense - total_saving

    if st.button("Calculate"):
        #creating piechart
        labels = ["Monthly Pay", "Other Monthly Income", "Housing", "Transportation", "Food", "Health", "Children", "Wife", "Self", "Installment", "Emergency", "Retirement", "Others"]
        values = [sidebar_monthIncome, sidebar_monthOtherIncome, sidebar_houseExpense, sidebar_transportExpense, sidebar_foodExpense, sidebar_healthExpense, sidebar_childExpense, sidebar_wifeExpense, sidebar_selfExpense, sidebar_installmentExpense, sidebar_emergencySaving, sidebar_retirementSaving, sidebar_otherSaving]
        pie_colors = ["#008000", "#F0E68C", "#F08080", "#D3D3D3", "#FFA500", "#800080", "#A0522D", "#FF6347", "#DC143C", "#6495ED", "#7FFFD4", "#E9967A", "#483D8B"]
        fig1, ax1 = plt.subplots(figsize =(10, 5))
        ax1.pie(values, autopct='%1.1f%%', colors=pie_colors)
        ax1.axis('equal')
        ax1.legend(labels, title="Legend", loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))

        if(calculator_result > 0):
            st.write(f"Wow, you still have Rp{round(calculator_result):,} left. It is a great step, keep it going!!")
            st.pyplot(fig1)
        elif(calculator_result < 0):
            st.write(f"Your money is over budget for Rp{abs(round(calculator_result)):,}. Be careful and try to minimize your expense as you can.")
            st.pyplot(fig1)
        else :
            st.write(f"You have equal income and expense, maybe try to reduce some of your non-priority expense")