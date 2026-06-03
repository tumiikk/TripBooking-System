import json
import os

def load_json(filename):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        return json.load(file)

def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)