# Use a pipeline as a high-level helper
# from transformers import pipeline
import os 
from pathlib import Path
import requests
from huggingface_hub import configure_http_backend

from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

import urllib3
urllib3.disable_warnings()

def backend_factory() -> requests.Session:
    session = requests.Session()
    session.verify = False
    return session

configure_http_backend(backend_factory=backend_factory)

def do_something():

    workfolder = Path.cwd()
    
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    raw_image = Image.open(os.path.join(workfolder, "images", "7.jpg")).convert('RGB')

    inputs = processor(raw_image, return_tensors="pt")

    out = model.generate(**inputs)
    print(processor.decode(out[0], skip_special_tokens=True))

if __name__ == '__main__':
    do_something()