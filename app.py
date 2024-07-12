{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "081fee5e-abc1-4948-bda0-cb50b692ba2a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [12/Jul/2024 16:09:45] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [12/Jul/2024 16:09:45] \"GET /favicon.ico HTTP/1.1\" 404 -\n",
      "E:\\program\\Lib\\site-packages\\sklearn\\base.py:439: UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [12/Jul/2024 16:09:58] \"POST /predict HTTP/1.1\" 200 -\n",
      "E:\\program\\Lib\\site-packages\\sklearn\\base.py:439: UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [12/Jul/2024 16:11:03] \"POST /predict HTTP/1.1\" 200 -\n",
      "E:\\program\\Lib\\site-packages\\sklearn\\base.py:439: UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names\n",
      "  warnings.warn(\n",
      "127.0.0.1 - - [12/Jul/2024 16:11:11] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify, render_template\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "app = Flask(__name__)\n",
    "model = pickle.load(open('iris_classifier.pkl', 'rb'))\n",
    "iris_species = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('iris.html')\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    data = [float(x) for x in request.form.values()]\n",
    "    features = [np.array(data)]\n",
    "    prediction = model.predict(features)\n",
    "    return jsonify({'prediction': iris_species[prediction[0]]})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, use_reloader=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "832cce2b-2fb8-454c-8a98-1cfe720847c1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
