import streamlit as st
import pickle
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler

# load the train model
with open('linear_regression_model.pkl', 'rb') as rf:
    model1 = pickle.load(rf)
# load the StandardScaler
#with open('scaler.pkl', 'rb') as stds:
    #scaler = pickle.load(stds)
standard_to = StandardScaler()
    
def predict(bathrooms, stories, parking, mainroad_yes, guestroom_yes,hotwaterheating_yes,airconditioning_yes,prefarea_yes, furnishingstatus_unfurnished):
    
    # processing user input
    
    '''lists = [bathrooms, stories, parking, mainroad_yes, guestroom_yes,hotwaterheating_yes,airconditioning_yes,prefarea_yes, furnishingstatus_unfurnished]
    df = pd.DataFrame(lists).transpose()
    # scaling the data
    standard_to.fit_transform(df)
    # making predictions using the train model
    prediction = model1.predict(df)
    result = int(prediction)
    return result'''

    input_data = pd.DataFrame({
        'bathrooms': [bathrooms],
        'stories': [stories],
        'parking': [parking],
        'mainroad_yes': [mainroad_yes],
        'guestroom_yes': [guestroom_yes],
        'hotwaterheating_yes': [hotwaterheating_yes],
        'airconditioning_yes': [airconditioning_yes],
        'prefarea_yes': [prefarea_yes],
        'furnishingstatus_unfurnished': [furnishingstatus_unfurnished]
    })

    # Scale the input data using the loaded scaler
    scaled_input_data = standard_to.transform(input_data)

    # Make predictions using the trained model
    prediction = model1.predict(scaled_input_data)
    result = int(prediction)
    return result







def main():
    style = """<div style='background-color:orange; padding:12px'>
              <h1 style='color:black'>House Price Prediction App</h1>
       </div>"""
    st.markdown(style, unsafe_allow_html=True)
    left, right = st.columns((2,2))

    
    bathrooms = left.number_input('Enter the number of bathrooms you want',
                                  step =1.0, format="%d")
    stories = right.number_input('Enter the number of stories you want',
                                  step=1.0, format='%d')
    parking = left.number_input("Enter the number of vehicles you'll be parking",
                                           step=1.0, format='%d')
    mainroad_yes = st.selectbox('Do you want your house to be on mainroad?',
                                      ("Yes","No"))
    guestroom_yes = st.selectbox('Do you want guestroom in your house?',
                                      ("Yes","No"))
    hotwaterheating_yes = st.selectbox('Do you want hot water in your house?',
                                      ("Yes","No"))
    airconditioning_yes = st.selectbox('Do you want airconditioning in your house?',
                                      ("Yes","No"))
    prefarea_yes = st.selectbox('Do you want prefarea?',
                                      ("Yes","No"))
    furnishingstatus_unfurnished = st.selectbox('Do you want your house to be on mainroad?',
                                      ("Furnished","Unfurnished"))
    
    furnishingstatus_furnished=0
    if(mainroad_yes=='Yes'):
                mainroad_yes=1
    else:
                mainroad_yes=0
    if(guestroom_yes=='Yes'):
                guestroom_yes=1
    else:
                guestroom_yes=0
    if(hotwaterheating_yes=='Yes'):
                hotwaterheating_yes=1
    else:
                hotwaterheating_yes=0
    if(airconditioning_yes=='Yes'):
                airconditioning_yes=1
    else:
                airconditioning_yes=0
    if(prefarea_yes=='Yes'):
                prefarea_yes=1
    else:
                prefarea_yes=0
    if(furnishingstatus_unfurnished=='unfurnished'):
                furnishingstatus_unfurnished=1
                furnishingstatus_furnished=0
    else:
                furnishingstatus_furnished=1
                furnishingstatus_unfurnished=0
    
    
    button = st.button('Predict')


    
    # if button is pressed
    if button:
        
        # make prediction
        result = predict(bathrooms, stories, parking, mainroad_yes, guestroom_yes,hotwaterheating_yes,airconditioning_yes,prefarea_yes, furnishingstatus_unfurnished)
        st.write(f'The value of the house is ${result}')