import os
import glob
import numpy as np
import io

from PIL import Image, ImageOps
from flask import Flask, request, jsonify, Response, send_file

app = Flask(__name__)


@app.route("/tranform/rotate", methods=["GET"])
def rotate_image():
    '''
    request:
        files['image']: Binary image file
        params['angle']: Rotation angle

    return: Rotated image
    '''
    file = request.files['image']
    angle = request.values['angle']
    img = Image.open(file.stream)
    img = img.rotate(float(angle))

    return response(img)


@app.route("/tranform/gray", methods=["GET"])
def gray_image():
    '''
    request:
        files['image']: Binary image file

    return: Gray image
    '''

    file = request.files['image']
    img = Image.open(file.stream)
    img = ImageOps.grayscale(img)


@app.route("/tranform/resize", methods=["GET"])
def resize_image():
    '''
    request:
        files['image']: Binary image file
        params['size']: Scaling factor

    return: Resized image
    '''


    file = request.files['image']
    sz = float(request.values['size'])
    img = Image.open(file.stream)
    img_size = (int(img.width * sz), int(img.height * sz))
    img = img.resize(img_size)

    return response(img)


@app.route("/tranform/equalize", methods=["GET"])
def equalize_image():
    '''
    request:
        files['image']: Binary image file

    return: Equalized image
    '''

    file = request.files['image']
    img = Image.open(file.stream)
    img = ImageOps.equalize(img)

    return response(img)



@app.route("/tranform/crop", methods=["GET"])
def crop_image():
    '''
    request:
        files['image']: Binary image file
        params['left']: left coordinate
        params['top']: top coordinate
        params['right']: right coordinate
        params['low']: low coordinate

    return: Cropped image
    '''

    file = request.files['image']
    left = int(request.values['left'])
    up = int(request.values['up'])
    right = int(request.values['right'])
    low = int(request.values['low'])
    img = Image.open(file.stream)
    img = img.crop((left, up, right, low))

    return response(img)




def response(img):
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='PNG')
    imgByteArr.seek(0)

    return send_file(imgByteArr, mimetype="image/" + 'png')



if __name__ == "__main__":
    app.run(port=3000, debug=True)