import streamlit as st
from firebase_admin import firestore

def app(global_state):

    # App title and divider
    st.title(':violet[FIND ORGAN ] & :violet[TISSUE DONORS]')
    st.divider()

    # Radio button to select action (FIND DONORS or BECOME A DONOR)
    selection = st.radio('SELECT', ['FIND DONORS', 'BECOME A DONOR'])

    # List to store registered donor details (temporary solution)
    registered_donors = []

    # User details section (hidden initially)
    user_details = st.container()
    user_details.visible = False

    # BECOME A DONOR section
    if selection == 'BECOME A DONOR':
        user_details.visible = True

        with user_details:
            donation_type = st.selectbox('SELECT Donation Type', [
                'BLOOD-DONATION',
                'ORGAN-DONATION(KIDNEY,LIVER,HEART,LUNGS)',
                'BONE-MARROW DONATION',
                'EYE-DONATION',
                'HAIR-DONATION',
                'ORGAN AND BODY DONATION FOR MEDICAL EDUCATION'
            ])
            name = st.text_input('Enter Name')
            gender = st.radio('Gender', ['Male', 'Female'])
            dob = st.date_input('DOB')
            address = st.text_input('Address')
            # Assuming District of Columbia details are not required for Find Donors
            st.subheader('(Optional) District of Columbia')
            zip_code = st.text_input('zip')
            phone = st.text_input('phone')
            email = st.text_input('E-mail')
            place_of_birth = st.text_input('Place of Birth(city/state)')
            ethnicity = st.selectbox('Ethnicity', [
                'select census category',
                'White',
                'Black',
                'Hispanic',
                'Asian',
                'American Indian/Alaskan Native',
                'Pacific Islander',
                'Multiracial'
            ])

            # Legal agreement and checkbox
            st.write('By submitting this registration I affirm that I am the applicant described on this application and that the information entered herein is true and correct to the best of my knowledge. This registration will serve as a document of gift as outlined in the District of Columbia Uniform Anatomical Gift Act. A document of gift, not revoked by the donor before death, is irreversible and does not require the consent of any other person. It also authorizes any examination necessary to ensure the medical acceptability of the anatomical gift')
            agree = st.checkbox('I agree')
            submit_button = st.button('submit')

            # Handle form submission and data storage (temporary)
            if submit_button:
                if agree:
                    donor_data = {  # Create a dictionary for each donor
                        'name': name,
                        'donation_type': donation_type,
                        'gender': gender,
                        'dob': str(dob),
                        'address': address,
                        # ... (add other user details as needed)
                    }

                    db = firestore.client()

                    db.collection("Users").document(global_state.email).update({"MedicalDonations": donor_data})  # Add data to Firestore collection

                    registered_donors.append(donor_data)  # Add donor data to list
                    st.success('Thank you for registering as a donor!')
                else:
                    st.warning('Please check the agreement box to submit the form.')

    # FIND DONORS section (display registered donors)
    elif selection == 'FIND DONORS':
        if registered_donors:  # Check if any donors are registered
            st.header('Registered Donors')
            for donor in registered_donors:  # Make sure this loop is indented within the if block
                st.write(f"Name: {donor['name']}")
                st.write(f"Donation Type: {donor['donation_type']}")
                # Add more details as needed: st.write(f"...")
        else:
            st.info('No donors are registered yet.')  # Informative message if no donors


 


