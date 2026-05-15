from flask import Flask, render_template, request,send_from_directory
import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():

    file = request.files["file"]

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # OCR
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image).lower()

    # Classification
    if "otp" in text:
        result = "OTP Screenshot"
    elif "import" in text or "print" in text:
        result = "Coding Screenshot"
    elif "order" in text:
        result = "Shopping Screenshot"
    else:
        result = "Others"

    # Save image for display
    image_url = "/" + file_path.replace("\\", "/")

    return render_template("result.html", result=result, image_url=image_url)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


app.run(debug=True)