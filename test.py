import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.header('Multi Disease Prediction Model using ML')

#loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav',"rb"))
breast_cancer_model = pickle.load(open('breast_cancer_model.sav',"rb"))
heart_disease_model = pickle.load(open('heart_disease_model.sav',"rb"))
parkinson_disease_model = pickle.load(open('parkinson_disease_model.sav',"rb"))

#sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction',
                             'Parkinson Disease Prediction'],
                             default_index = 0)
    
#Diabetes prediction page

if(selected == 'Diabetes Prediction'):

    #page title
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
      Pregnancies = st.text_input('Number of pregnancies')

    with col2:
      Glucose = st.text_input('Glucose level')

    with col3: 
      BloodPressure = st.text_input('Blood Pressure Value')	

    with col1:
      SkinThickness =	st.text_input('SkinThickness value')

    with col2: 
      Insulin	= st.text_input('Insulin level')

    with col3:
      BMI = st.text_input('weight/height^2 value')

    with col1:
      DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col3:
      Age = st.text_input('Age of person')

#code for diab_dignosis
    diab_diagnosis = ''

#creating a botton for prediction
    if st.button('Diabetes Test result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age	]])

        if(diab_prediction[0] == 1):
          diab_diagnosis = 'The person is Diabetic'
        else:
          diab_diagnosis = 'The person is not Diabetic'
    st.success(diab_diagnosis)            
        

#Heart Disease Prediction page

if(selected == 'Heart Disease Prediction'):

    #page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
      age = st.text_input('Age of the Person')

    with col2:
      sex = st.text_input('Sex of Person')

    with col3: 
      cp = st.text_input('Cheast pain Type')	

    with col1:
      trestbps =	st.text_input('Resting Blood Pressure value')

    with col2: 
      chol	= st.text_input('Serum Cholesterol in mg/dl')

    with col3:
      fbs = st.text_input('Fasting Blood sugar value in mg/dl')

    with col1:
      restecg = st.text_input('Resting ECG value')

    with col2:
      thalach = st.text_input('Maximum heart rate achieved value')

    with col3:
      exang = st.text_input('Exercise induced angina')

    with col1:
       oldpeak = st.text_input('ST depression induced by exercise relative to rest')

    with col2:
      slope = st.text_input('The slope of the peak exercise ST segment')  

    with col3:
      ca = st.text_input('number of major vessels (0-3) colored by flourosopy')

    with col1:
      thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')     

 #code for heart_disease_dignosis
    heart_disease_diagnosis = ''

 #creating a botton for prediction
    if st.button('Heart Disease Test result'):
      user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
      user_input=[float(x) for x in user_input]
      heart_disease_prediction=heart_disease_model.predict([user_input])

      if(heart_disease_prediction[0] == 1):
        heart_disease_diagnosis = 'The person have Heart Disease'
      else:
        heart_disease_diagnosis = 'The person dont have Heart Disease'
    st.success(heart_disease_diagnosis)

#Breast Cancer Prediction page

if(selected == 'Breast Cancer Prediction'):

    #page title
    st.title('Breast Cancer Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.text_input('Average Tumor Radius')

    with col2:
        texture_mean = st.text_input('Average Surface Texture (Roughness)')

    with col3:
        perimeter_mean = st.text_input('Average Tumor Boundary Length')

    with col1:
        area_mean = st.text_input('Average Tumor Area')

    with col2:
        smoothness_mean = st.text_input('Average Smoothness of Tumor Edge')

    with col3:
        compactness_mean = st.text_input('How Dense / Compact the Tumor Is')

    with col1:
        concavity_mean = st.text_input('How Deep the Tumor Indents Inwards')

    with col2:
        concave_points_mean = st.text_input('Number of Sharp Indent Points')

    with col3:
        symmetry_mean = st.text_input('How Symmetrical the Tumor Shape Is')

    with col1:
        fractal_dimension_mean = st.text_input('Complexity of Tumor Border')

    with col2:
        radius_se = st.text_input('Variation in Radius')

    with col3:
        texture_se = st.text_input('Variation in Texture')

    with col1:
        perimeter_se = st.text_input('Variation in Boundary Length')

    with col2:
        area_se = st.text_input('Variation in Area')

    with col3:
        smoothness_se = st.text_input('Variation in Smoothness')

    with col1:
        compactness_se = st.text_input('Variation in Compactness')

    with col2:
        concavity_se = st.text_input('Variation in Concavity')

    with col3:
        concave_points_se = st.text_input('Variation in Sharp Indents')

    with col1:
        symmetry_se = st.text_input('Variation in Symmetry')

    with col2:
        fractal_dimension_se = st.text_input('Variation in Border Complexity')

    with col3:
        radius_worst = st.text_input('Maximum Tumor Radius')

    with col1:
        texture_worst = st.text_input('Roughest Texture')

    with col2:
        perimeter_worst = st.text_input('Largest Boundary Length')

    with col3:
        area_worst = st.text_input('Largest Tumor Area')

    with col1:
        smoothness_worst = st.text_input('Roughest Edge')

    with col2:
        compactness_worst = st.text_input('Highest Density')

    with col3:
        concavity_worst = st.text_input('Deepest Inward Curves')

    with col1:
        concave_points_worst = st.text_input('Maximum Sharp Indents')

    with col2:
        symmetry_worst = st.text_input('Least Symmetrical Shape')

    with col3:
        fractal_dimension_worst = st.text_input('Highest Border Complexity')     

    #code for breast_cancer_dignosis
    breast_cancer_diagnosis = ''

    #creating a botton for prediction
    if st.button('Breast cancer Test result'):
      breast_cancer_prediction = breast_cancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean,
                                                                smoothness_mean, compactness_mean, 
                                                               concavity_mean, concave_points_mean, symmetry_mean, 
                                                               fractal_dimension_mean, radius_se, texture_se, perimeter_se, 
                                                               area_se, smoothness_se, compactness_se, concavity_se,
                                                                 concave_points_se, symmetry_se, fractal_dimension_se, 
                                                                 radius_worst, texture_worst, perimeter_worst, 
                                                                 area_worst, smoothness_worst, compactness_worst, 
                                                                 concavity_worst, concave_points_worst, 
                                                                 symmetry_worst, fractal_dimension_worst]])

      if(breast_cancer_prediction[0] == 1):
       breast_cancer_diagnosis = 'The cancer type is Benign'
      else:
        breast_cancer_diagnosis = 'The cancer type is Malignant'
    st.success(breast_cancer_diagnosis)

    

#Perkinson Disease Prediction page

if(selected == 'Parkinson Disease Prediction'):

    #page title
    st.title('Parkinson Disease Prediction using ML') 
    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo = st.text_input('Average Pitch (Hz)')

    with col2:
        MDVP_Fhi = st.text_input('Maximum Pitch (Hz)')

    with col3:
        MDVP_Flo = st.text_input('Minimum Pitch (Hz)')

    with col1:
        MDVP_Jitter_percent = st.text_input('Jitter (Percent Pitch Variation)')

    with col2:
        MDVP_Jitter_Abs = st.text_input('Jitter (Absolute Pitch Variation)')

    with col3:
        MDVP_RAP = st.text_input('Jitter Relative Average Perturbation')

    with col1:
        MDVP_PPQ = st.text_input('Jitter – Pitch Period Perturbation Quotient')

    with col2:
        Jitter_DDP = st.text_input('Jitter – Average Absolute Difference')

    with col3:
        MDVP_Shimmer = st.text_input('Shimmer (Amplitude Variation)')

    with col1:
        MDVP_Shimmer_dB = st.text_input('Shimmer (dB)')

    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer – Amplitude Perturbation (APQ3)')

    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer – Amplitude Perturbation (APQ5)')

    with col1:
        MDVP_APQ = st.text_input('Shimmer – Amplitude Perturbation (APQ11)')

    with col2:
        Shimmer_DDA = st.text_input('Shimmer – Average Absolute Difference')

    with col3:
        NHR = st.text_input('Noise-to-Harmonics Ratio')

    with col1:
        HNR = st.text_input('Harmonics-to-Noise Ratio')

    with col3:
        RPDE = st.text_input('Nonlinear Voice Variability (RPDE)')

    with col1:
        DFA = st.text_input('Signal Complexity (DFA)')

    with col2:
        spread1 = st.text_input('Frequency Spread Measure 1')

    with col3:
        spread2 = st.text_input('Frequency Spread Measure 2')

    with col1:
        D2 = st.text_input('Correlation Dimension (Nonlinear Measure)')

    with col2:
        PPE = st.text_input('Pitch Period Entropy')

    
 #code for heart_disease_dignosis
    parkinson_disease_diagnosis = ''

 #creating a botton for prediction
    if st.button('Parkinson Disease Test result'):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter_percent,
                                                                        MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
                                                                            MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3,
                                                                            Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR,
                                                                            RPDE, DFA, spread1, spread2, D2, PPE]
        user_input=[float(x) for  x in user_input ]
        parkinson_disease_prediction=parkinson_disease_model.predict([user_input])


        if(parkinson_disease_prediction[0] == 1):
             parkinson_disease_diagnosis = 'The person have parkinson Disease'
        else:
             parkinson_disease_diagnosis = 'The person dont have parkinson Disease'
    st.success(parkinson_disease_diagnosis)