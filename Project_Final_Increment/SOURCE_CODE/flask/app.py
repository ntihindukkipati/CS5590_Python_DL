from werkzeug.utils import secure_filename
import joblib
from flask import Flask, request, render_template,jsonify
import cv2
import numpy as np
from keras.models import load_model


# Define a flask app
app = Flask(__name__, template_folder='Templates')

def process_eval(imk):
    output1 = cv2.resize(imk, (128,128))
    output1 = output1.astype('float')
    output1 /= 255.0
    output1 = np.array(output1).reshape(-1, 128, 128, 3)
    classifer = load_model('model-best.h5')
    x = classifer.predict_classes(output1[[0], :])
    if x[0] == 1:
        result = "PATIENT IS HAVING PNEMONIA "
    else:
        result = "PATIENT IS NORMAL  "
    j = classifer.predict(output1[[0], :])
    k = max(j[0]) * 100
    k = str(k)
    k = k[:5] + "% Sure"
    k = "(" + k + ")"
    result += k
    return result

@app.route('/', methods=['GET'])
def index():
   return render_template('fileUpload.html')

@app.route('/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename("save.jpeg"))
        im=cv2.imread("save.jpeg")
        result=process_eval(im)
        return render_template('fileUpload.html',result=result)
@app.route('/handle_request', methods=['POST'])
def handle_form_request():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename("save.jpeg"))
        im=cv2.imread("save.jpeg")
        result=process_eval(im)
        return jsonify({"data" : result })

if __name__ == "__main__":
    app.run()

