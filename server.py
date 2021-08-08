# install poppler: http://blog.alivate.com.au/poppler-windows/
# install pdf2image: pip install pdf2images
# install pyzbar: pip install pyzbar

from flask import Flask, request, jsonify, send_file
import time

import barcode
from pdf import get_pdfinfo_fromfiles, get_page, get_page_filename

app = Flask(__name__)

users = []
messages = []


@app.route("/")
def hello():
    return """Use //recognize/<filenames> with | as a path separator"""


@app.route("/status")
def status():
    return {"status": True, "name": "Сервер Алексея"}


@app.route("/page/<string:strfilename>/<int:pagenum>", methods=["GET"])
def page(strfilename, pagenum):
    filename = strfilename.replace("|", "/")
    return send_file(get_page_filename(filename, pagenum))


@app.route("/decode_ean13/<string:strfilename>/<int:pagenum>", methods=["GET"])
def decode_ean13(strfilename, pagenum):
    filename = strfilename.replace("|", "/")
    imagefilename = get_page_filename(filename, pagenum)
    decoded = barcode.decode_ean13(imagefilename)
    return jsonify(decoded)


@app.route("/pdfinfo/<string:strfilenames>", methods=["GET"])
def pdfinfo(strfilenames):
    # recognize barcode from first page of pdf file or from image,
    # accepts file data or file path, accessible by local network
    app.logger.debug('pdfinfo')
    filenames = strfilenames.split(",")
    newfilenames = []
    for filename in filenames:
        newfilenames.append(filename.replace("|", "/"))
    if request.method == "GET":
        info = get_pdfinfo_fromfiles(newfilenames)
        return jsonify(info), 200
    else:
        return {"method": "Unsupported"}


@app.route("/recognize/<string:strfilenames>", methods=["GET"])
def recognize(strfilenames):
    # recognize barcode from first page of pdf file or from image,
    # accepts file data or file path, accessible by local network
    app.logger.debug('recognize')
    filenames = strfilenames.split(",")
    newfilenames = []
    for filename in filenames:
        newfilenames.append(filename.replace("|", "/"))
    if request.method == "GET":
        print(request.json)
        return {"method": "GET", "filename": newfilenames[0]}
    else:
        return {"method": "Unsupported"}


@app.route("/pdf2images", methods=["GET", "POST"])
def pdf2images():
    return {"method": "Not implemented"}


app.run()
