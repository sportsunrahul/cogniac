import os
import glob
import jsonpickle
import numpy as np
import io

from PIL import Image, ImageOps
from flask import Flask, request, jsonify, Response, send_file

app = Flask(__name__)


@app.route("/rotate", methods=["POST"])
def rotate_image():
    file = request.files['image']
    angle = request.values['angle']
    img = Image.open(file.stream)
    img = img.rotate(float(angle))

    return response(img)


@app.route("/gray", methods=["POST"])
def gray_image():
    file = request.files['image']
    img = Image.open(file.stream)
    img = ImageOps.grayscale(img)


@app.route("/resize", methods=["POST"])
def resize_image():
    file = request.files['image']
    sz = int(request.values['size'])
    img = Image.open(file.stream)
    img_size = (img.width * sz, img.height * sz)
    img = img.resize(img_size)

    return response(img)


def response(img):
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='PNG')
    imgByteArr.seek(0)

    return send_file(imgByteArr, mimetype="image/" + 'png')



if __name__ == "__main__":
    app.run(port=3000, debug=True)