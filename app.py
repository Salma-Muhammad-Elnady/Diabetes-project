from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('best_xgboost.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            Glucose = int(request.form['Glucose'])
            BloodPressure = int(request.form['BloodPressure'])
            SkinThickness = int(request.form['SkinThickness'])
            Insulin = int(request.form['Insulin'])
            BMI = float(request.form['BMI'])
            DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
            Age = int(request.form['Age'])

            data = np.array([[Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            prediction = model.predict(data)
            if prediction[0] == 1:
                
                result = 'The person has diabetes.'
            else:
                result = 'The person does not have diabetes.'
            

            return render_template('result.html', prediction=result)
        except ValueError as e:
            return render_template('result.html', prediction="Please enter valid numeric values.", error=str(e))

if __name__ == '__main__':
    app.run(debug=True)