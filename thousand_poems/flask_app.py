
import os
from flask import Flask, render_template, request, jsonify
from ImageClassifier import ImageClassifier
from multiprocessing import set_start_method
from ai_chat import Ai_chat
import re

app = Flask(__name__)
ALLOWED_EXTENSIONS = 'jpg'

def test():
    return "Hello"

@app.route('/', methods=['GET', 'POST'])
def main():
    message = ""
    return render_template("index.html", message=message)

@app.route('/generate', methods=['GET'])
def generate_mistake():
    message = ""
    return render_template("index.html", message=message)

@app.route('/generate', methods=['POST'])
def check_image():
    try:
        if 'file' not in request.files:
            return render_template("index.html", error_message="file not found/ file not valid")
        
        image_source = request.files['file']
        image_file_name = image_source.filename 

        if image_file_name.lower().endswith(ALLOWED_EXTENSIONS.lower()):
            output = transfomer_classifier.evaluate(image_source)
            output = ai_chat.generate_poem(output)
            print(output)
            output = re.split(r'[\n]', output)
            return render_template("index.html", message=output)
        else:
            return render_template("index.html", error_message="Invalid format (JPG Only)/no file detected")

    except Exception as e:
        return jsonify({"error" : str(e)}), 500

if __name__  == '__main__':
    transfomer_classifier = ImageClassifier()
    ai_chat = Ai_chat()
    app.run(debug=True)
