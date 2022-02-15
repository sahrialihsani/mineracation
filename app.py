# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from app_helper import *

# Define a flask app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/detect/')
def detect():
    return render_template('index2.html')

@app.route('/uploader', methods = ['POST'])
def upload_file():
    predictions=""

    if request.method == 'POST':
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'static','uploads', secure_filename(f.filename))
        f.save(file_path)

        predictions = get_classes(file_path)
        if predictions>0.5:
            prob = (predictions[0][0])*100
            predictions="Terindikasi Cancer, \nProbability: "+str(prob)
        else:
            prob = (predictions[0][0])*100
            predictions="Normal, \nProbability: "+str(prob)

        print("preds:::",predictions)
    return render_template("upload.html", predictions=predictions, display_image=f.filename) 


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port="4100")
