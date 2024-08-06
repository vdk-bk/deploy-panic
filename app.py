from flask import Flask, request,render_template
import pickle

app = Flask(__name__)

Model = pickle.load(open('model.pkl','rb'))

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/y_predict', methods=['POST'])
def predict():

    age = (request.form['Age'])
    gender = request.form['Gender']  
    symptoms = request.form['Symptoms']
    severity = (request.form['Severity'])
    medical_history = request.form['Medical History']
    lifestyle_factors = request.form['Lifestyle Factors']



    prediction = Model.predict([[age,gender,symptoms,severity,medical_history,lifestyle_factors]])

    # Determining the results
    if prediction >= 1:
        result = 'Positive for Panic Disorder'
    else:
        result = 'Negative for Panic Disorder'

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=False)
