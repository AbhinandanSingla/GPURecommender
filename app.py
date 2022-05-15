from flask import Flask
from flask import Flask, render_template, request, jsonify
import random
from keras.models import load_model
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

app = Flask(__name__)
df = pd.read_csv('datasets/CleanedData.csv')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('./index.html')


@app.route('/getRecommendation', methods=['POST'])
def getRecommendation():
    res = request.values.to_dict()
    print(res)
    gpuValue, tdp, testDate, desktop, workstation, mobile = 0, 0, 0, 0, 0, 0
    if res['gpuValue'] == '':
        gpuValue = random.randrange(0, 69)
    else:
        gpuValue = int(res['gpuValue'])
    if res['tdp'] == '':
        tdp = random.randrange(5, 500)
    else:
        tdp = int(res['tdp'])
    if res['date'] == '':
        testDate = 2022
    else:
        testDate = int(res['date'])
    if res['category'] == 'Desktop':
        desktop = 1
    if res['category'] == 'Workstation':
        workstation = 1
    if res['category'] == 'Mobile':
        mobile = 1
    mark3d = int(res['Mark3d'])
    mark2d = int(res['Mark2d'])
    price = int(res['price'])
    pp = int(res['pp'])

    loadModel = load_model('models/model.h5')
    arr = np.array([[mark3d, mark2d, price, gpuValue, tdp, pp, testDate, 0, 0, 0, 0, 1, 0]])
    print(arr)
    pred = loadModel(arr)
    # print(np.argmax(pred[0]))
    b = df.iloc[np.argmax(pred[0])]
    print(b.to_dict())
    return jsonify(b.to_dict())


if __name__ == '__main__':
    app.run()
