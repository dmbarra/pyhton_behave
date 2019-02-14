import os
import json

settings = None


def load_settings():
    global settings
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../project_config.json")
    with open(path) as f:
        settings = json.load(f)


load_settings()