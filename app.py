from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('iris_classifier.pkl', 'rb'))
iris_species = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

@app.route('/')
def home():
    return render_template('iris.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    features = [np.array(data)]
    prediction = model.predict(features)
    return jsonify({'prediction': iris_species[prediction[0]]})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
