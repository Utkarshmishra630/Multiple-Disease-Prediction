import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#set page configuration
st.set_page_config(page_title="Health Guard",layout="wide")

#getting the working directory of the .py file
working_dir = os.path.dirname(os.path.abspath(__file__))

#loading of the saved models
diabetes_model=pickle.load(open('diabetes.pkl','rb'))

#sidebar for navigation
with st.sidebar:
	selected =option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
	

if selected == 'Diabetes Prediction':
	st.title("Welcome to the Diabetes Prediction Model")
	col1,col2,col3 = st.columns(3)
	
	glucose = col1.slider('Glucose Level',0,500,120)
	bp = col2.slider('Blood Pressure Level',0,200,120)
	skthick = col3.slider('Skin Thickness Value',0,100,20)
	insulin = col1.slider('Isulin Level',0,900,30)
	bmi = col2.slider('BMI Value',0.0,70.0,25.0)
	dpf=col3.slider('Diabetes Pedigree Function',0.00,2.50,.50)
	age=col1.slider('Age of person',0,100,5)

	if st.button('Diabetes Test Result'):
	 user_input=[glucose,bp,skthick,insulin,bmi,dpf,age]
	 pred = diabetes_model.predict([user_input])[0]
	 diab_diagnosis = 'The Person is Diabetic' if pred == 1 else 'The Person is not Diabetic'
	 st.success(diab_diagnosis)
		