import streamlit as st
import firebase_admin  # Import Firebase Admin SDK
from firebase_admin import credentials, firestore, storage  

# Replace with your Firebase project credentials (from Firebase console)
# cred = credentials.Certificate('food-donation-bda4d-946ce54b194a.json')  # Replace with actual path
# firebase_admin.initialize_app(cred)
db = firestore.client()

def app(global_state):

    st.title(':orange[Our Contacts]:pushpin:')
    st.subheader(':violet[Phone] :iphone:')
    st.text('91+93xxxx89')
    st.text("")
    st.subheader(':violet[E-mail] :email:')
    st.text('office@ShareJoy.org')
    st.text("")
    st.divider()
    st.title(':orange[Quick Contact Form]:mailbox_with_mail:')

    name = st.text_input('Name', key='name', help='Please enter your name (required)')
    email = st.text_input('E-mail', key='email', help='Please enter your email (required)')
    phone = st.text_input('phone', key='phone', help='Please enter your phone number')
    case_description = st.text_area('Case Decription', key='case_description')

    # Check if all mandatory fields are filled
    if all(field != '' for field in [name, email]):
        submitted = st.button('Submit')
    else:
        submitted = False

    if submitted:
        # Create data dictionary with user input
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "case_description": case_description
        }

        # Add data to Firestore collection (replace 'contacts' with your desired collection name)
        try:
            doc_ref = db.collection('contacts').document()  # Generate unique document ID
            doc_ref.set(data)
            st.success('Your message has been submitted successfully!')
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    app()

