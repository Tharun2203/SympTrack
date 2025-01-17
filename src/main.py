import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Disease Prediction System",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction'],
                           menu_icon='hospital',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction')

    # Collect Patient Information
    col1, col2 = st.columns(2)
    with col1:
        patient_name = st.text_input("Patient Name")
    with col2:
        patient_id = st.text_input("Patient ID")

    # Input Fields
    cols = st.columns(4)  # Divide the page into 4 equal columns
    with cols[0]:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with cols[1]:
        if gender == "Female":
            Pregnancies = st.text_input("Number of Pregnancies")
        else:
            Pregnancies = 0
            st.text_input("Number of Pregnancies", disabled=True)
    with cols[2]:
        Glucose = st.text_input('Glucose Level')
    with cols[3]:
        BloodPressure = st.text_input('Blood Pressure value')

    with cols[0]:
        SkinThickness = st.text_input('Skin Thickness value')
    with cols[1]:
        Insulin = st.text_input('Insulin Level')
    with cols[2]:
        BMI = st.text_input('BMI value')
    with cols[3]:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with cols[0]:
        Age = st.text_input('Age of the Person')

    # Prediction Button
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        try:
            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                st.warning(f"The patient **{patient_name}** (ID: {patient_id}) is diabetic")
            else:
                st.success(f"The patient **{patient_name}** (ID: {patient_id}) is not diabetic")
        except ValueError:
            st.error("Please enter valid numerical values for all input fields.")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction')

    # Collect Patient Information
    col1, col2 = st.columns(2)
    with col1:
        patient_name = st.text_input("Patient Name")
    with col2:
        patient_id = st.text_input("Patient ID")

    # Input Fields
    cols = st.columns(4)  # Divide the page into 4 equal columns
    with cols[0]:
        age = st.text_input('Age')
    with cols[1]:
        sex = st.text_input('Sex')
    with cols[2]:
        cp = st.text_input('Chest Pain types')
    with cols[3]:
        trestbps = st.text_input('Resting Blood Pressure')

    with cols[0]:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with cols[1]:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with cols[2]:
        restecg = st.text_input('Resting Electrocardiographic results')
    with cols[3]:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with cols[0]:
        exang = st.text_input('Exercise Induced Angina')
    with cols[1]:
        oldpeak = st.text_input('ST depression induced by exercise')
    with cols[2]:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with cols[3]:
        ca = st.text_input('Major vessels colored by fluoroscopy')

    with cols[0]:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    # Prediction Button
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        try:
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                st.warning(f"The patient **{patient_name}** (ID: {patient_id}) has heart disease")
            else:
                st.success(f"The patient **{patient_name}** (ID: {patient_id}) does not have heart disease")
        except ValueError:
            st.error("Please enter valid numerical values for all input fields.")


# To run this code, use : python3 -m streamlit run main.py (or) streamlit run main.py
