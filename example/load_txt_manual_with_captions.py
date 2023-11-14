"""Example code for interfacing with the atari 2600 manuals."""
import json
from PIL import Image
import fitz
import pkgutil

def load_manual_text(env_name="MsPacman") -> str:
    """
    Load the text manual with the captioned images for a given environment.
    inputs:
        env_name (str): The string name of the atari 2600 environment
    outputs:
        manual (str): The text manual for the given environment
    """

    # 1. Load the text manual
    manual = pkgutil.get_data(__name__, f"manuals/{env_name}/{env_name}.txt").decode()

    # 2. Load the captioned images .json file 
    captions = json.loads(pkgutil.get_data(__name__, f"manuals/{env_name}/figure_captions.json").decode())

    # 3. Wrap the captions in the appropriate markdown
    for key, value in captions.items():
        captions[key] = f"[{key.replace('Figure','F')}-Caption: {value}]"

    # 4. Add the captions to the manual
    manual = manual.format(**captions)

    # 5. Return the manual
    return manual

def load_manual_images(env_name="MsPacman") -> list:
    """
    Load the text manual with the images for a given environment
    inputs:
        env_name (str): The string name of the atari 2600 environment
    outputs:
        images (list): A list of images for the given environment corresponding
            to the pages of the manual.
    """
    # 1. Convert the pdf to images
    pdf_data = pkgutil.get_data(__name__, f"manuals/{env_name}/{env_name}.pdf")
    doc = fitz.open(stream=pdf_data, filetype="pdf")
    images = []
    for page in doc:
        pix = page.get_pixmap()
        img = fitz.Pixmap(pix)
        images.append(img)
    # convert the images to PIL images
    images = [Image.frombytes("RGB", [img.width, img.height], img.samples) for img in images]

    # 2. Return the images
    return images


if __name__ == "__main__":
    print(load_manual_text(env_name="Alien"))
    ## test the pdf to images functionality by saving the images
    images = load_manual_images(env_name="Alien")
