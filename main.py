import streamlit as st 
 
from streamlit_option_menu import option_menu 
from firebase_admin import credentials, firestore, initialize_app, storage  # Import Firestore
import firebase_admin
cred = credentials.Certificate("food-donation-bda4d-946ce54b194a.json")  

try:
    firebase_admin.get_app()
except ValueError as e:
    # firebase_admin.initialize_app(cred)     
    initialize_app(cred, {'storageBucket': 'food-donation-bda4d.appspot.com'})

 



class global_state:
    def __init__(self):
        self.email = ''
        self.messages=[]
        self.selectbox=''


if "global_state" not in st.session_state:
    st.session_state.global_state = global_state()

global_state = st.session_state.global_state


import home,authentication,organistion, donate, medidonars,surplusfood,about,contact

class MultiApp: 

    st.set_page_config( 
        page_title="ShareJoy", 
) 
 
    def init(self): 
        self.apps=[] 
 
    def add_app(self, title, func): 
 
        self.apps.append({ 
            "title": title, 
            "function": func 
        }) 
 
    def run(): 
        #app = st.sidebar( 
        with st.sidebar:         
            app=option_menu( 
                menu_title='ShareJoy', 
                options=['Home','Authentication','Organistion','Donate','Medidonars','Surplusfood','About','Contact'], 
                ) 
 
        if app=='Home': 
            home.app(global_state) 
        if app=="Authentication": 
            authentication.app(global_state)     
        if app=="Organistion": 
            organistion.app(global_state)    
        if app=='Donate': 
            donate.app(global_state) 
        if app=='Medidonars': 
            medidonars.app(global_state)
        if app=='Surplusfood': 
            surplusfood.app(global_state)            
        if app=='About': 
            about.app(global_state)
        if app=='Contact': 
            contact.app(global_state)       


    run()