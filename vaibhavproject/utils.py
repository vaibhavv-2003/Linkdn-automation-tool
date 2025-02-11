import json
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    print(f"Loading config from {config_path}")
    with open(config_path) as config_file:
        return json.load(config_file)

def is_test_mode(config):
    return config.get("test_mode", True)
