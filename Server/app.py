from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from datetime import datetime, date
import base64
import os
from PIL import Image


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = API_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = API_PASSWORD
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)
today = date.today()

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


class Data(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.LargeBinary, nullable=False)
    time = db.Column(db.String, default=datetime.now().hour)

db.create_all()

@app.route("/", methods=["POST"])
@basic_auth.required
def main():
    rows = Data.query.all()
    try:
        if str(rows[-1][2]) != str(datetime.now().hour):
            print("Deleted pervious hour data")
            db.drop_all()
            db.create_all()
    except:
        print("Something Went Wrong!")

    file = Image.open(request.files['image'].stream)
    file.save("image.jpg", optimize=True,
              compress_level=9, quality=5)
    img = convertToBinaryData("image.jpg")

    data_tuple = Data(img=img, time=datetime.now().hour)
    db.session.add(data_tuple)
    db.session.commit()

    print("Image and date inserted successfully into database")
    os.remove('image.jpg')

    return jsonify({'msg': 'success'})



@app.route("/data", methods=["GET"])
@basic_auth.required
def get_data():

    rows = Data.query.all()

    data_tuple = []

    for i in range(0, len(rows)):
        with open('get_image.jpg', 'wb') as file:
            file.write(rows[i].img)
        rows[i].img = base64.b64encode(
            open('get_image.jpg', 'rb').read()).decode('utf-8')

        data_tuple.append([rows[i].img,rows[i].time])

        os.remove('get_image.jpg')

    return jsonify({"data": data_tuple})


if __name__ == "__main__":
    app.run(debug=True)
