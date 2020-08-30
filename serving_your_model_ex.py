from flask import Flask
from flask import request
import numpy as np
import pandas as pd
from joblib import load

# from flask_exercise_json_request.py import json_request
# from flask_exercise_request.py import single_request
from conf import *

def main():
    # json_request(DATA)
    # single_request(SAMPLE)
    pass

app = Flask(__name__)
with open(FILENAME, 'rb') as f:
    clf = load(f)

@app.route('/')
def main_page():
    return 'Server is up!'


@app.route('/predict_single')
def predict_sample():
    features = [
        'Age', 'Beekeep_for', 'Qualif', 'Training', 'Coop_treat',
        'Bee_population_size'
    ]
    x = pd.DataFrame(np.array([float(request.args.get(key))
                               for key in features]).reshape(1, -1), columns=features)
    return str(round(clf.predict(x)[0], 2))

@app.route('/predict-many', methods=["POST"])
def predict_many():

    if request.is_json:
        req = request.get_json()
        req = pd.read_json(req, orient='table')
        preds = clf.predict(req).tolist()
        return str(preds)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    app.aboutToQuit.connect(app.deleteLater)

