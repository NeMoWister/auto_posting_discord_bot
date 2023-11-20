import json
import os


def json_write(name, json_data):
    with open(f"{name}.json", "w") as json_file:
        json.dump(json_data, json_file)


def json_delete(name):
    os.remove(f"{name}.json")


def json_parse(name):
    with open(f"{name}.json", "r") as json_file:
        return json.load(json_file)
