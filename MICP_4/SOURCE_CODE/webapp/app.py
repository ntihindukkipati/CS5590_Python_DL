from werkzeug.utils import secure_filename
import joblib
import os
from flask import Flask, request,jsonify, render_template
#import requests
import cv2
#from PIL import Image
#import tensorflow as tf
#import keras
import numpy as np
app = Flask(__name__)
#@app.route('/', methods=['GET'])
#def index():
    # Main page
 #   return render_template('index.html')


def process_evaluation(imk):
    output1 = cv2.resize(imk, (32,32))
    output1 = output1.astype('float')
    output1 /= 255.0
    print(type(output1))
    output1 = np.array(output1).reshape(-1, 32, 32, 3)
    classifer = joblib.load("Nithin.pk2")
    x = classifer.predict_classes(output1[[0], :])
    if x[0] == 0:
        result = "PREDICTED AS PAPER"
    elif x[0] ==1:
        result = "PREDICTED AS ROCK"
    else:
        result="PREDICTED AS SCISSORS"
    return result


@app.route('/', methods=['GET','POST'])
def handle_form():
    if request.method=='POST':
         file = request.files['file']
         file.save(secure_filename("save.jpeg"))
         im=cv2.imread("save.jpeg")
         result=process_evaluation(im)
         return render_template('finalpg.html',result=result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
