import streamlit as st
from firebase_admin import firestore

def app(global_state):
    st.title(':rainbow[SurplusFood] :rice:')
    st.divider()

    if global_state.email == '':
        st.warning('Pleas Login First!!')

    else:    

        # Radio button with validation
        is_surplus_food = st.radio("Is This Surplus Food?", ("Yes", "No"))

        if is_surplus_food == "No":
            st.write("This app is for surplus food donation. If you're looking for food assistance, please visit our resources page (link to resources).")
            st.stop()

        # Input fields with validation and error handling
        name = st.text_input("Name", key="name")
        if not name:
            st.error("Please enter your name.")

        phone = st.text_input("Phone Number", key="phone")
        if not phone.isdigit():
            st.error("Please enter a valid phone number using digits only.")

        email = st.text_input("E-mail", key="email")
        if not ("@" in email and "." in email):
            st.error("Please enter a valid email address.")

        state = st.selectbox("State", ["SELECT", "Andhra Pradesh", "Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"])  

        # Text area with placeholder text
        food_pickup_address = st.text_area(
            "Food Pick-up Address", key="food_pickup_address", placeholder="Enter the address where food can be picked up"
        )
        if not food_pickup_address:
            st.error("Please enter the food pick-up address.")

        meal_quantity = st.selectbox("Meal Quantity", ["SELECT", "10-49 Meals", "50-99 Meals", "100-199","200-299","300-399","400-500"])

        food_quality_confirmed = st.checkbox("By checking this box, I confirm the food quality is safe and fit for consumption.")

        # Submit button with conditional action (consider data persistence)
        data = {
                
            'Name':name,
            'Email':email,
            "Phone":phone,
            "Meal Quantity":meal_quantity,
            "State":state,
            "Food Pickup Address":food_pickup_address,
            "Food Quality Confirmed":True if food_quality_confirmed else False,

        }
        db = firestore.client()

        if st.button("Submit"):
            if all([name, phone, email, state, food_pickup_address, meal_quantity, food_quality_confirmed]):
                # Data is valid, proceed with processing (e.g., send data to home.py or an external service)
                db.collection("Users").document(global_state.email).update({"SurplusFood": data})  # Add data to Firestore collection

                st.success("Thank you for your donation! We will contact you shortly.")
                # Consider data persistence here (e.g., storing in a database or sending to another app)
            else:
                st.error("Please address all errors before submitting.")

if __name__ == "__main__":
    app()



    