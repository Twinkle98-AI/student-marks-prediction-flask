# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load(r"C:\Users\Admin\Desktop\student marks\Desktop.pkl")

# DataFrame to store inputs and outputs
df = pd.DataFrame(columns=['Study Hours', 'Predicted Output'])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    global df

    # Get input from form
    input_features = [int(x) for x in request.form.values()]
    study_hours = input_features[0]

    # Validate study hours (0 to 24 only)
    if study_hours < 0 or study_hours > 24:
        return render_template(
            'index.html',
            prediction_text='Please enter valid study hours between 0 and 24'
        )

    # Model prediction
    prediction = model.predict([np.array(input_features)])[0][0]

    # Cap marks at 100%
    prediction = round(min(prediction, 100), 2)

    # Save data to DataFrame and CSV
    df = pd.concat(
        [df, pd.DataFrame({'Study Hours': [study_hours], 'Predicted Output': [prediction]})],
        ignore_index=True
    )

    df.to_csv('smp_data_from_app.csv', index=False)

    return render_template(
        'index.html',
        prediction_text=f'You will get [{prediction}%] marks when you study [{study_hours}] hours per day'
    )


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
