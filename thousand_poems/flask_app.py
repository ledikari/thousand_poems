
import os
from flask import Flask, render_template, request, jsonify
from ImageClassifier import ImageClassifier
from multiprocessing import set_start_method


app = Flask(__name__)
ALLOWED_EXTENSIONS = 'jpg'

def test():
    return "Hello"

@app.route('/', methods=['GET', 'POST'])
def main():
    message = ""
    return render_template("index.html", message=message)

@app.route('/check_image', methods=['POST'])
def check_image():
    try:
        if 'file' not in request.files:
            return render_template("index.html", message="file not found")
        
        image_source = request.files['file']
        image_file_name = image_source.filename 

        if image_file_name.lower().endswith(ALLOWED_EXTENSIONS.lower()):
            output = check_image.evaluate(image_source)
            return render_template("index.html", message=output)
        else:
            return render_template("index.html", message="Invalid format/no file detected")

    except Exception as e:
        return jsonify({"error" : str(e)}), 500

if __name__  == '__main__':
    check_image = ImageClassifier()
    app.run(debug=True)
