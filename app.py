from flask import Flask,request,jsonify
from test import main
import pybase64
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/generate",methods=["GET","POST"])
def Generate():
    data=request.get_json()
    main(data.get("file"))
    # main("data/json/2635.json ")

    with open('dump/fp_final_0.png', 'rb') as f:
        image_bytes = f.read()

    # Encode the image bytes as a base64 string
    image_base64 = pybase64.b64encode(image_bytes).decode()

    # Construct the data URL
    data_url = 'data:image/jpg;base64,' + image_base64
    return jsonify({"url":data_url,"success":True})
    # return "Success"

if __name__=="__main__":
    app.debug=True
    app.run()