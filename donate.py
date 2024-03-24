import streamlit as st
import stripe
import webbrowser

def app(global_state):
    st.title('Give with heart, change a life.:violet[Share The Joy] make a difference')
    org = st.selectbox('SELECT',['Orphanage','HOME-LESS FOOD','CHILD-EDUCATION','STRAY-DOG','PLANTED-TREE'])

    st.divider()

    stripe.api_key = "sk_test_51Oiv3cSEf9JLaVyQrO935O7irkmBVIINUU3dA9dDZpkDEXLfV23DnsvMMWbCvmKAw6APXKtZW4Dn4beCj5Di09iQ00uUXR9Izy"

    def is_active_subscriber(user_email: str) -> bool:
        if 'plan' not in st.session_state:
            st.session_state.plan = ''
        if 'payments' not in st.session_state:
            st.session_state.payments = ''     

        # stripe.api_key = get_api_key()


        payments = []

        customers = stripe.Customer.list(email=user_email)
        total_payment=0


        # Iterate over the list of customers and retrieve the customer ID
        for customer in customers.auto_paging_iter():
            customer_id = customer.id
            payment_intents = stripe.PaymentIntent.list(customer=customer_id)

            payment_type=''
            for payment_intent in payment_intents.auto_paging_iter():
                # Check if the PaymentIntent is associated with a Subscription
                if payment_intent.status == 'succeeded' or True:
                    print(payment_intent)
                    total_payment+=int(str(payment_intent.amount)[:-2])
                    print(str(payment_intent.amount)[:-2])

        print('Total: ',total_payment)        
                    # print('Customer ID:', customer_id)
                    # print('pt',payment_intents)

                    # try:
                    #     if payment_intent.description is not None:
                    #         subscriptions = stripe.Subscription.list(customer=customer_id)
                    #         for subscription in subscriptions.auto_paging_iter():
                    #             if subscription.status == 'active':
                    #                 # active_subscriptions += 1
                    #                 payment_type = 'month'
                    #     else:
                    #         payment_type = 'one-time'
                    # except:
                    #     payment_type = ''
                    # print('Payment Type: ',payment_type)    

        # if len(payments)>0:
        #     if global_state.email:
        #         try:
        #             db.collection('Users').document(global_state.email).update({"Stripe": 'True'})
        #         except:pass 
        #         try:
        #             db.collection('Users').document(global_state.email).update({"Plans": st.session_state.payments})
        #         except:pass 

            
        # else:
        #     if global_state.email:
        #         try:
        #             db.collection('Users').document(global_state.email).update({"Stripe": 'False'})
        #         except:pass 
        #         try:
        #             db.collection('Users').document(global_state.email).update({"Plans": ''})
        #         except:pass 
        #     return False
        



        return len(payments) > 0
    
    is_active_subscriber('as@g.com')


    #org = 'B'
    def get_link():
        customer = stripe.Customer.create(
        email='as@g.com'
        )
        # if type == 'one-time':    
        session = stripe.checkout.Session.create(
            customer=customer.id,
            payment_method_types=['card'],
            # price="price_1OkmaESEf9JLaVyQrbpcOMGH",
            line_items=[{
                    'price': 'price_1OkmaESEf9JLaVyQrbpcOMGH',
                    'quantity': 1,
                }],
            # payment_url='https://buy.stripe.com/test_7sIcQ35ou6pv2d2288',  # Replace 'your_payment_link_here' with your actual payment link
            mode='payment',
            success_url="https://sharejoy.onrender.com/",
            cancel_url="https://sharejoy.onrender.com/",
            payment_intent_data={
                'description': org, 
            },
            metadata={
                'payment type': 'one-time',
            }
            
            ,
        )
        print(session.url)
        webbrowser.open(session.url)
        return session.url

                #if type=='monthly':
                #     session = stripe.checkout.Session.create(
                #         customer=customer.id,
                #         payment_method_types=['card'],
                #         line_items=[{
                #             'price': 'price_1OKNUnI1gmlWVXDMGAtc0SPX',

                #             # 'price': 'price_1OKIxHI1gmlWVXDMIvdO1BOX', # For live stripe key
                #             'quantity': 1,
                #         }],
                #         mode='subscription',
                #         success_url="",
                #         # success_url=st.secrets['redirect_url'],
                #         cancel_url=st.secrets['redirect_url'],
                #     )
                #  st.session_state.opt_to_subscribe = True

                #     #url=f"{stripe_link}?prefilled_email={encoded_email}"
                #     return session.url
                # if type=='one-time':    
                #     session = stripe.checkout.Session.create(
                #         customer=customer.id,
                #         payment_method_types=['card'],
                #         line_items=[{
                #             'price': 'price_1OKNVuI1gmlWVXDMMpafIA6C',

                #             # 'price': 'price_1OKIxHI1gmlWVXDMIvdO1BOX', # For live stripe key
                #             'quantity': 1,
                #         }],
                #         mode='payment',
                #         success_url="h",
                #         # success_url=st.secrets['redirect_url'],
                #         cancel_url=st.secrets['redirect_url'],
                #     )
                #     st.session_state.opt_to_subscribe = True

                #     #url=f"{stripe_link}?prefilled_email={encoded_email}"
                #     return session.url
                # # return False     
        is_active_subscriber('as@g.com')
          

    if st.button('Donate'):
         webbrowser.open(get_link)
