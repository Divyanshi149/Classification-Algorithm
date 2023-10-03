
import streamlit as st
import joblib
import pandas as pd

model = joblib.load('Diabetes_Prediction_Model.pkl')

# Create a Streamlit app
st.markdown("<h1 style='color: #00008B; font-size: 48px; font-weight: bold;'>Diabetes Prediction Model</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: black; font-size: 20px; font-weight: bold;'>Fill the given form appropriately and predict your diabetes risk</h2>", unsafe_allow_html=True)

# Create a dictionary with questions, feature names, and answer mappings
question_data = {
    "Do you have High Blood Pressure? - 0 = No; 1 = Yes":
        {"feature_name": "HighBP", "answers": (0,1)},
    "Do you have High Cholestrol Levels? - 0 = No; 1 = Yes":
        {"feature_name": "HighChol", "answers": (0,1)},
    "Did you get your Cholestrol checked in the last 5 years? - 0= No; 1 = Yes":
        {"feature_name": "CholCheck", "answers": (0,1)},
    "What is your Body Mass Index (BMI)? - between 12 to 98":
        {"feature_name": "BMI", "answers": (12,98)},
    "Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes] - 0 = No; 1 = Yes":
        {"feature_name": "Smoker", "answers": (0,1)},
    "Ever had a stroke?- 0 = No; 1 = Yes":
        {"feature_name": "Stroke", "answers": (0,1)},
    "Do you have Coronary Heart Disease (CHD) or Myocardial Infarction (MI) - 0 = No; 1 = Yes":
        {"feature_name": "HeartDiseaseorAttack", "answers": (0,1)},
    "Did you do any Physical Activity in past 30 days (not including job) - 0 = No; 1 = Yes":
        {"feature_name": "PhysActivity", "answers": (0,1)},
    "Do you consume Fruits 1 or more times per day? - 0 = No; 1 = Yes":
        {"feature_name": "Fruits", "answers": (0,1)},
    "Do you consume Vegetables 1 or more times per day? - 0 = No; 1 = Yes":
        {"feature_name": "Veggies", "answers": (0,1)},
    "Are you a Heavy Drinker? (Adult men having >14 drinks/week & adult women having >7 drinks/week) - 0 = No; 1 = Yes":
        {"feature_name": "HvyAlcoholConsump", "answers": (0,1)},
    "Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc.- 0 = No; 1 = Yes":
        {"feature_name": "AnyHealthcare", "answers": (0,1)},
    "Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? - 0 = No; 1 = Yes":
        {"feature_name": "NoDocbcCost", "answers": (0,1)},
    "How would you say that in general your health is on a scale of 1-5? - 1 = Excellent; 2 = Very Good; 3 = Good; 4 = Fair; 5 = Poor":
        {"feature_name": "GenHlth", "answers": (1,5)},
    "Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? Scale 1-30 days?":
        {"feature_name": "MentHlth", "answers": (0,30)},
    "Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? Scale 1-30 days?":
        {"feature_name": "PhysHlth", "answers": (0,30)},
    "Do you have serious difficulty in walking or climbing stairs? - 0 = No; 1 = Yes?":
        {"feature_name": "DiffWalk", "answers": (0,1)},
    "Sex - 0 = Female; 1 = Male":
        {"feature_name": "Sex", "answers": (0,1)}, 
    "13-level age category (_AGEG5YR see codebook) 1 = 18-24; 2 = 25-30; 3 = 31-35; 4 = 36-40; 5 = 41-45; 6 = 46-50; 7 = 51-55; 8 = 56-60; 9 = 61-65; 10 = 66-70; 11 = 71-75; 12 = 76-80; 13 = 80 or older":
        {"feature_name": "Age", "answers": (1,13)}, 
    "Education level on scale of 1-6: 1 = Never attended school or only kindergarten; 2 = Grades 1 through 8 (Elementary); 3 = Grades 9 through 11 (Some high school); 4 = Grade 12 or GED (High school graduate); 5 = College 1 year to 3 years (Some college or technical school); 6 = College 4 years or more (College graduate)":
        {"feature_name": "Education", "answers": (1,6)}, 
    "Income scale (INCOME2 see codebook) on scale of 1-8 - 1 = Less than Rs.50,000; 2 = Between Rs. 50,000 & 1,00,000; 3 = Between Rs. 1,00,000 & 2,00,000; 4 = Between Rs. 2,00,000 & 5,00,000; 5 = Between Rs. 5,00,000 & 8,00,000; 6 = Between Rs. 8,00,000 & 10,00,000; 7 = Between Rs. 10,00,000 & 15,00,000; 8 = Rs. 15,00,000 or more":
        {"feature_name": "Income", "answers": (1,8)} 
}

# Create input fields for each question with custom answer mappings
answers = {}
for question, data in question_data.items():
    feature_name = data["feature_name"]
    min_range, max_range = data["answers"]
    
    # Use a number input with the extracted min and max ranges
    answer = st.number_input(question, min_value=min_range, max_value=max_range, value=min_range, key=feature_name, format="%d")

    answers[feature_name] = answer
# Create a button to trigger prediction
if st.button("Predict"):
    # Prepare the input data for prediction
    input_data = pd.DataFrame([answers], columns=[data["feature_name"] for data in question_data.values()])

    # Make the prediction
    prediction = model.predict(input_data)[0]

    # Display the result with custom styling
    if prediction == 0:
        st.markdown("<h1 style='color: green; font-size: 28px; font-weight: bold;'>You are likely to have NO DIABETES.</h1>", unsafe_allow_html=True)
    elif prediction == 1:
        st.markdown("<h1 style='color: yellow; font-size: 28px; font-weight: bold;'>You are likely to have PRE-DIABETES.</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='color: red; font-size: 28px; font-weight: bold;'>You are likely to have DIABETES.</h1>", unsafe_allow_html=True)
