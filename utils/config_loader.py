import json

def load_config(env="dev"):
    with open(f"config/{env}_config.json") as f:
        return json.load(f)