
import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import requests,json
# from main import global_state


cred = credentials.Certificate("food-donation-bda4d-946ce54b194a.json")
# firebase_admin.initialize_app(cred)
def app(global_state):
# Usernm = []
    st.title('Sign into :violet[ShareJoy] and be the spark for good vibes!')
    st.image('images\Brown and Yellow Charity Vector Hand Logo.png',width=300,use_column_width=300,)

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''



    def on_login(): 
        try:
            # user = auth.get_user_by_email(email)
            user = sign_in_with_email_and_password(email,password)
            # print(user.uid)
            # st.session_state.username = user.uid
            global_state.email = user
            
            global Useremail
            Useremail=(user)
            
            st.session_state.signedout = True
            st.session_state.signout = True  

            db = firestore.client()
            if global_state.email:
                doc_ref = db.collection("Users").document(global_state.email)
                doc_snapshot = doc_ref.get()
                if doc_snapshot.exists:
                    data = doc_snapshot.to_dict()
                    field_value = data.get("SurplusFood")
                    print("Surplus:", field_value)
                    # global_state.key=field_value
                    # global_state.payments=field_value

                else:
                    data={"SurplusFood":{},'MedicalDonations':{}}
                    db.collection('Users').document(global_state.email).set(data)  
  
            
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''


    def sign_up_with_email_and_password(email, password, return_secure_token=True):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
            payload = json.dumps({
                "email": email,
                "password": password,
                
                "returnSecureToken": return_secure_token
            })
            r = requests.post(rest_api_url, params={"key": "AIzaSyA8r2YFU2wLmnCK6kn3aCySZw9Xf5Y4k_s"}, data=payload)
            try:
                print(r.json())
                return r.json()['email']
            except:
                st.warning(r.json())
        except Exception as e:
            st.warning(f'Signup failed: {e}')

    def sign_in_with_email_and_password(email, password, return_secure_token=True):
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

        try:
            payload = json.dumps({
                "email": email,
                "password": password,
                "returnSecureToken": return_secure_token
            })
            r = requests.post(rest_api_url, params={"key": "AIzaSyA8r2YFU2wLmnCK6kn3aCySZw9Xf5Y4k_s"}, data=payload)
            # print('done r')

            try:
                print(r.json())
                return r.json()['email']
            except:
                st.warning(r.json())

        except Exception as e:
            st.warning(f'Login failed: {e}')

        
    
        
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
        

        
    
    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        choice = st.selectbox('Login/Signup',['Login','Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password',type='password')
        

        
        if choice == 'Sign up':
            username = st.text_input("Enter  your unique username")
            
            if st.button('Create my account'):
                # user = auth.create_user(email = email, password = password,uid=username)
                user = sign_up_with_email_and_password(email,password)
                
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()
        else:
            # st.button('Login', on_click=f)          
            st.button('Login', on_click=on_login)
            
            
    if st.session_state.signout:
                # st.text('Name '+st.session_state.username)
                st.text(f"Email id: {global_state.email}")
                st.button('Sign out', on_click=t) 
            
                
    

                            
    def ap():
        st.write('Posts')


              

 
    