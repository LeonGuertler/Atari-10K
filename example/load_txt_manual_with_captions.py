"""Example code for interfacing with the atari 2600 manuals."""
import json
import os
import fitz

def load_manual_text(env_name="MsPacman", path_to_manuals=os.path.join("..", "manuals")) -> str:
    """
    Load the text manual with the captioned images for a given environment.
    inputs:
        env_name (str): The string name of the atari 2600 environment
        path_to_manuals (str): The path to the manuals directory
    outputs:
        manual (str): The text manual for the given environment
    """

    # 1. Load the text manual
    with open(os.path.join(path_to_manuals, env_name, f"{env_name}.txt"), "r") as f:
        manual = f.read()

    # 2. Load the captioned images .json file 
    with open(os.path.join(path_to_manuals, env_name, f"figure_captions.json"), "r") as f:
        captions = json.load(f)

    # 3. Wrap the captions in the appropriate markdown
    for key, value in captions.items():
        captions[key] = f"[{key.replace('Figure','F')}-Caption: {value}]"

    # 4. Add the captions to the manual
    manual = manual.format(**captions)

    # 5. Return the manual
    return manual

def load_manual_images(env_name="MsPacman", path_to_manuals=os.path.join("..", "manuals")) -> list:
    """
    Load the text manual with the images for a given environment
    inputs:
        env_name (str): The string name of the atari 2600 environment
        path_to_manuals (str): The path to the manuals directory
    outputs:
        images (list): A list of images for the given environment corresponding
            to the pages of the manual.
    """
    path = os.path.join(path_to_manuals, env_name, f"{env_name}.pdf")
    # 1. Convert the pdf to images
    doc = fitz.open(path)
    images = []
    for page in doc:
        pix = page.get_pixmap()
        img = fitz.Pixmap(pix)
        images.append(img)

    # 2. Return the images
    return images


if __name__ == "__main__":
    print(load_manual_text(env_name="Alien", path_to_manuals="manuals"))
    ## test the pdf to images functionality by saving the images
    images = load_manual_images(env_name="Alien", path_to_manuals="manuals")
    for i, image in enumerate(images):
        image.save(f"Alien_{i}.png")
