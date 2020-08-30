import numpy as np

URL_BASE = "http://localhost:5000/predict_single?"
URL_BASE_JSON = "http://127.0.0.1:5001/predict-many"
URL_BASE_SINGLE = "http://127.0.0.1:5000/predict_single?"

FILENAME = '/Users/mikhailgoncharov/ITC_2/FRAMEWORKS AND TOOLS/serving_your_model.joblib'
SAMPLE = np.array([['4', '3', '0', '1', '0', '2']], dtype=object)
DATA = np.array([[2, 3, 1, 1, 1, 5],
                 [3, 2, 1, 1, 0, 1],
                 [3, 3, 0, 1, 1, 1],
                 [4, 1, 0, 0, 0, 1],
                 [4, 3, 0, 0, 0, 1],
                 [4, 2, 0, 0, 0, 1]], dtype=object)