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


class ImageClassifier(object):
    """Image classifer class

    Args:
        object (_type_): none

    Returns:
        str: With the use of hugging face Transformers, look at the image and try to identify
                what it is.
    """

    processor = None
    model = None

    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


    def evaluate(self, image_path):
        """Evaluate image and determine contents.

        Args:
            image_path (str): absolute path of the image to be loaded

        Returns:
            str: description of the object classified by the Transformer 
        """
        raw_image = Image.open(image_path).convert('RGB')

        inputs = self.processor(raw_image, return_tensors="pt")

        out = self.model.generate(**inputs)
        return self.processor.decode(out[0], skip_special_tokens=True)

if __name__ == "__main__":
    workfolder = Path.cwd()
    imagec = ImageClassifier()
    print(imagec.evaluate(os.path.join(workfolder, "images", "1.jpg")))
