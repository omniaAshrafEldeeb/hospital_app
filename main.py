import streamlit as st
from streamlit_option_menu import option_menu
import pyodbc
import pandas as pd
from sqlalchemy import create_engine
st.set_page_config(page_title = "Hospital App", page_icon= '🏥', layout="wide")




import Home, Hospital_info, about, My_info , Tests, Doctor_info

with st.spinner("Calculating......."):

    st.snow()



    class MultiApp :
        
        def __init__ (self):
            self.apps = []

        def add_app(self, title, func):

            self.apps.append (
                {"title": title,
                "function" : func,
                })
            
        def run():
            with st.sidebar:
                app = option_menu(
                    menu_title ='Hispotals app',
                    menu_icon = 'options',
                    options = ['Home', "Hospitals info","Doctors info","My info","Tests","About&contact"] ,
                    icons = [] ,
                    default_index = 0,
            
                )

            if app == "Home":
                Home.app()

            if app == "Hospitals info":
                Hospital_info.app()
            if app == "Doctors info":
                Doctor_info.app()
            if app == "My info":
                #
                # st.balloons()
                My_info.app()
            if app == "Tests":
                Tests.app()
            if app == "About&contact":
                about.app()

        run()    
        print("okay6")






    # Inject the CSS into the app using st.markdown








