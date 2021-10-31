import streamlit as st
import pickle
import sklearn
from multiapp import MultiApp
from apps import home, expense #import your new app page here

#title & layout
st.set_page_config(page_title = "Fortune", layout = "wide")

#hiding streamlit button
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#multiapp
app = MultiApp()

#content
st.title("Welcome to Fortune")
st.markdown("""
    * Here you can find Information about how to split your money correctly based on your personal information
    * Please use the bar on the left to navigate the app
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Expense Calculator", expense.app)
# The main app
app.run()