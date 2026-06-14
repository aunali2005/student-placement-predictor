from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    cgpa = float(request.form['cgpa'])
    internships = int(request.form['internships'])
    projects = int(request.form['projects'])

    result = model.predict([[cgpa, internships, projects]])

    if result[0] == 1:
        prediction = "Likely to be Placed"
    else:
        prediction = "Placement Chances are Low"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)