import os, json

def load_manual(env_name="MsPacman", path_to_manuals=os.path.join("..", "manuals")) -> str:
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



if __name__ == "__main__":
    print(load_manual(env_name="Alien"))