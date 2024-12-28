# **Diabetes Prediction Web Application**
# Web application images and prediction results: 
###1. Data entry form .
![img1](https://github.com/user-attachments/assets/ffb3095b-1b14-45ac-8633-0a43ad9a9dd0)
________________________________________________________________________
2. Entering some data to test the model .
![img2](https://github.com/user-attachments/assets/aa382440-8ec0-4947-b374-b9e0fc28f84f)
__________________________________________________________________________
3. Display the prediction result with an alert message. 
![img3](https://github.com/user-attachments/assets/9dd4570c-9902-40ba-a55b-d470b851885d)


# Overview :
A web application to determine whether a person has diabetes or not, using the XG Boost model to predict the diabetes outcome when the following data is entered: glucose, blood pressure, skin thickness, insulin, body mass index (BMI), diabetes pedigree function, age.

# Project advantages :
* User interface: A simple interface for easy input of health data.
* XGBoost model: The XGBoost model, known for its high accuracy in predictions, is used.
* Instant prediction: Provides instant prediction results based on user inputs.

# Technologies Used :
* Frontend: HTML, CSS, JavaScript.
* Backend: Python, Flask.
* Machine learning: logistic regression, KNN, SVM, random forest, decision tree, XGBoost, and XGBoost was chosen as the best model in terms of precision, recall, and, ROC-AUC for predicting diabetes outcomes in a web application.
 
 # Project steps : 
 ### 1. Data Import:
+ Download the Diabetes dataset from Kaggle.

### 2. Data Analysis:
* Explore data and analyze different features.
* Creating visualizations to highlight the relationships between different features and the outcome. 

### 3. Data processing and cleaning: 
* Data cleaning by removing the unimportant feature that does not have a significant impact on the result.

### 4. Model Building:
* Try different algorithms like: Logistic regression, KNN, SVM, Random forest, Decision tree, XGBoost.
*  Each model is evaluated based on precision, recall, and roc-auc, and the best model in terms of precision, recall, and roc-auc is selected for use in predicting the outcome in the web application based on user input.
  
### 5. Model improvement:
* Improving the model using techniques such as cross-validation and feature engineering.
* Compare the different models and choose the one that provides the best result.

### 6. Model Deployment:
* Save the Best Model: Save the trained model to a file (using joblib or pickle).
* Create a Flask Web Application: Develop a web application using Flask to serve the model.
* Build User Interface: Create an interface using HTML and CSS for users to input their health data.
* Integrate Model with Web App: By uploading the saved model in the Flask application and using it to generate predictions based on user inputs.
* Running the model: By testing it with data input to make a prediction of the result.

# Project goal:
* Developing a web application using the XGBoost model to predict diabetes based on a set of input data with high prediction accuracy.    








 

