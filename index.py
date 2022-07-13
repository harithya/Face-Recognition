from deepface import DeepFace;
from flask import Flask
from flask import request

app = Flask(__name__)
app.env = "development"

@app.route('/verify',methods=['GET', 'POST'])
def index():
    models = ["VGG-Face"]
    result = DeepFace.verify(request.form['img_url_1'], request.form['img_url_2'], model_name = models[0]);
    return result;


