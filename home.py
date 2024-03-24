import streamlit as st
from PIL import Image
from firebase_admin import credentials, initialize_app, storage, firestore
from datetime import datetime
import firebase_admin
import webbrowser
from organistion import get_docs
# from main import global_state
# cred = credentials.Certificate("food-donation-bda4d-946ce54b194a.json")
# try:
#     firebase_admin.get_app()
# except ValueError as e:
#     initialize_app(cred, {'storageBucket': 'food-donation-bda4d.appspot.com'})

def app(global_state):

    if 'email' not in st.session_state:
        global_state.email = ''

    st.title('Welcome to :violet[ShareJoy] :blush:')

    st.video('ShareJoy.mp4')


   

    if 'uploaded_image' not in st.session_state:
        st.session_state.uploaded_image = None

        # File uploader allows user to add their own image in the left column
    uploaded_file = st.file_uploader(label="Share your SharedJoy images", type=["png", "jpg", "jpeg", "heic"])

    if uploaded_file is not None:

        # Display the uploaded image under the upload area
        image = Image.open(uploaded_file).convert("RGB")
        
        # Save the image to session state
        st.session_state.uploaded_image = image

        # save the image to disk
        image.save("./uploaded_image.jpg")
    if 'uploaded_image' not in st.session_state:
        st.session_state.uploaded_image = None
    if st.session_state.uploaded_image is not None:
        st.image(st.session_state.uploaded_image, caption="Uploaded Image", use_column_width=True)


    #For storage
    if global_state.email!='' and st.session_state.uploaded_image:
        current_time = datetime.now()
        shared_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        fileName = "Users/"+global_state.email+f"/{shared_timestamp}"
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename('uploaded_image.jpg')

        # Opt : if you want to make public access from the URL
        blob.make_public()

    st.title(":rainbow[SurplusFood] :rice: Summary")

    # Assuming data is received from surplusfood.py through a mechanism like session state or a database
    name = st.session_state.get("name", "")
    phone = st.session_state.get("phone", "")
    email = st.session_state.get("email", "")
    state = st.session_state.get("state", "")
    food_pickup_address = st.session_state.get("food_pickup_address", "")
    meal_quantity = st.session_state.get("meal_quantity", "")

    # Display donation details if available
    if name:
        st.write(f"**Name:** {name}")
        st.write(f"**Phone Number:** {phone}")
        st.write(f"**E-mail:** {email}")
        st.write(f"**State:** {state}")
        st.write(f"**Food Pick-up Address:** {food_pickup_address}")
        st.write(f"**Meal Quantity:** {meal_quantity}")
    else:
        st.write("No recent donations to display.")

        st.divider
        

    

    def open_org_page(email):
        url=get_docs(email)
        # url = '''https://firebasestorage.googleapis.com/v0/b/food-donation-bda4d.appspot.com/o/Users%2Fmolakalamohankrishna%40gmail.com%2F2024-02-12%2010%3A11%3A12?alt=media&token=ab40a494-b267-4101-963c-29da4261f59a'''
        webbrowser.open(url)


    org_list = [{'Email':'abc','Name':'THAAGAM FOUNDATION','DEtails':'''We are orphanage children's helpers ..........\n Show your support !!!!- THAAGAM FOUNDATION '''},{'Email':'2a@g','Name':'DONATEinKIND','DEtails':'''2We are helpers For Hungry people ..........\n Show your support !!!!- DONATEinKIND'''},{'Email':'3a@g','Name':'NATIONAL ORGAN & TISSUE TRANSPLANT ORG','DEtails':'''3We are Orgon & Tissue Donars  ..........\n Show your support !!!!- NOTTO '''}]
    total_orgs = len(org_list)
    i=0
    while i < total_orgs:

        c1,c2 = st.columns(2)    
        with st.container(border=2):
            c1.title(org_list[i]['Name'])
            c1.write(f'''{org_list[i]['DEtails']}
                 ''')
            if c1.button('Org, Details', key=i):
                open_org_page(org_list[i]['Email'])
        if i+1 < total_orgs:
            with st.container(border=2):
                c2.title(org_list[i+1]['Name'])
                c2.write(f'''{org_list[i]['DEtails']}
                    ''')
                if c2.button('Org, Details', key=i+1):
                    open_org_page(org_list[i]['Email'])
        i+=2        
if __name__ == "__main__":
    app()    




