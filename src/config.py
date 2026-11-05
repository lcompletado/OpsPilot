import json

def load_config():
    with open("config.json", "r") as file:
        config = json.load(file)

    targets = config["targets"]

    return config