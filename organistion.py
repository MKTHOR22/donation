import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore, storage

# Replace with your Firebase project credentials (from Firebase console)
# cred = credentials.Certificate("food-donation-bda4d-946ce54b194a.json")
# firebase_admin.initialize_app(cred)
db = firestore.client()  # Initialize Firestore client

def get_docs(email):
    try:
        print('\n running ')
        folder_path = f'Organisations/{email}'
        bucket = storage.bucket()
        blobs = list(bucket.list_blobs(prefix=folder_path))
        print(blobs)


        # subfolders = set()
        # for blob in reversed(blobs):
        # subfolder = blob.name[len(folder_path):].split('/')[0]
        # if subfolder and subfolder not in subfolders:
        # subfolders.add(subfolder)
        # subfolder_path = f"{folder_path}{subfolder}/"
        # blobs = bucket.list_blobs(prefix=subfolder_path)


        # # Iterate through subfolders and get links for files
        # # for subfolder in subfolders:
        # subfolder_path = f"{folder_path}{subfolder}/"

        # List all files in the specified subfolder
        # blobs = bucket.list_blobs(prefix=subfolder_path)


        # Dictionary to store data for the current subfolder
        
            # Iterate through blobs and update data dictionary
        # for blob in blobs:
            # if blob.contain(f'Organisations/{email}/Detail'):
        blob=blobs[1]
        blob.make_public()
        public_url = blob.public_url
        print(public_url)
        return public_url
                # print(f"Folder: {subfolder}, Public URL: {public_url}")
    except Exception as e:
        print(e)
def app(global_state):

    st.title(':violet[ORGANISATION] :gray[REGISTRATION]')
    st.subheader('Be part of !:violet[ Share Joy] Register your local organization and make a positive impact with us')
    st.divider()

    with st.form(key="organization_form"):
        st.subheader('BASIC :violet[ INFORMATION]:writing_hand:')
        org_name = st.text_input('Name of the organization', key='org_name')
        reg_number = st.text_input('Registration number', key='reg_number')
        reg_doc = st.file_uploader('Registration Document', type=["pdf", "docx"])
        st.text('CONTACT INFORMATION')
        mobile_number = st.text_input('Mobile Number', key='mobile_number')
        email = st.text_input('E-Mail', key='email')
        address = st.text_area('Address', key='address')
        st.text('MISSION AND PURPOSE')
        mission = st.selectbox('SELECT', ['Orphanage', 'HOME-LESS FOOD', 'CHILD-EDUCATION', 'STRAY-DOG', 'PLANTED-TREE'])
        st.text('BANK DETAILS')
        account_holder = st.text_input('Holder Name', key='account_holder')
        bank_name = st.text_input('Bank Name', key='bank_name')
        account_number = st.text_input('A/C Number', key='account_number')
        ifsc_code = st.text_input('IFSC Number', key='ifsc_code')
        submit_button = st.form_submit_button('Register')

    # Check for empty fields and make them mandatory
    if all(field != '' for field in [org_name, reg_number, mobile_number, email, address,
                                       account_holder, bank_name, account_number, ifsc_code]):
        try:
            data = {
                "name": org_name,
                "registration_number": reg_number,
                "mobile_number": mobile_number,
                "email": email,
                "address": address,
                "mission": mission,
                "account_holder": account_holder,
                "bank_name": bank_name,
                "account_number": account_number,
                "ifsc_code": ifsc_code
            }

            # Handle potential file upload (if implemented)
            if reg_doc is not None:
                bucket = storage.bucket()
                file_name = f"{org_name}_{reg_number}_{reg_doc.name}"  # Unique filename
                reg_doc.write(f"tmp/{file_name}", overwrite=True)  # Store temporarily
                blob = bucket.blob(file_name)  # Access a Cloud Storage bucket (requires setup)
                blob.upload_from_filename(f"tmp/{file_name}")  # Upload to Cloud Storage
                data["registration_document_url"] = blob.public_url  # Store document URL in Firestore

            db.collection("organizations").add(data)  # Add data to Firestore collection
            st.success("Organization registration successful!")
        except Exception as e:
            st.error(f"Firebase error: {e}")
    else:
        st.error("Please fill in all required fields.")

if __name__ == "__main__":
    app()

