import streamlit as st

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
    st.text_input('Name')
    st.text_input('E-mail')
    st.text_input('phone')
    st.text_area('Case Decription')
    st.button('Submit')
