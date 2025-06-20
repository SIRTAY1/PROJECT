
import streamlit as st
import joblib
import numpy as np
import pandas as pd


model = joblib.load("Finanical_account_model.pkl")
 
#st.header("Welcome to my model")
 
#def main():
    #st.title("Bank account")

    
    #st.header("Welcome to my model")
    #location_type=st. text_input("location_type")
    #cellphone_access= st.text_input("cellphone_acess")
    #household_size= st.text_input =("household_size")
    #age_of_respondent =st.tex_input("age_of_respondent")	 
    #gender_of_respondent = st.text_input("gender_of_respondent")
    #marital_status = st.text_input("martial_status")
    #education_leve =st.text_input("educational_level")	
    #job_type = st.text_input("job_type")
    #bank_account = st.text_input("bank_account") 


    #if st.button("button"):
       # makeprediction =model.predict( [[location_type, cellphone_access, household_size, age_of_respondent,	 
#gender_of_respondent, marital_status, education_level, job_type, bank_account]])

   # output=round(makeprediction[0],2)
    #st.success(f"You can now predict {output}")


    #if __name__ == '__main__':
        #main()




#.subheader("Prediction Result")
#st.write("Prediction:", prediction[0])
#st.write("Probability (Class 0 | Class 1):", prediction_proba[0])

import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("Finanical_account_model.pkl")

# Streamlit App
def main():
    st.title("Bank Account Prediction")

    # Input features
    location_type = st.text_input("Location Type")
    cellphone_access = st.text_input("Cellphone Access")
    household_size = st.number_input("Household Size", min_value=1)
    age_of_respondent = st.number_input("Age of Respondent", min_value=0)
    gender_of_respondent = st.text_input("Gender of Respondent")
    marital_status = st.text_input("Marital Status")
    education_level = st.text_input("Education Level")
    job_type = st.text_input("Job Type")
    
    # Prediction button
    if st.button("Make Prediction"):
        # Prepare input as 2D array for prediction
        features = [[
            location_type, cellphone_access, household_size, age_of_respondent,
            gender_of_respondent, marital_status, education_level, job_type
        ]]

        # Make prediction
        prediction = model.predict(features)

        st.success(f"Prediction: {prediction[0]}")

if __name__ == '__main__':
    main()







