import os
import pickle

class Model:
    def __init__(self):
        model_path = os.path.join('myapp', 'model.pkl')
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
    def predict(self, x):
        return model.predict(x)
