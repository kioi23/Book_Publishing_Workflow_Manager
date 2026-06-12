import json
import os

DATA_FILE = "data/database.json"


def load_data():
    """
    Load data from database.json.
    Returns a dictionary.
    """

    if not os.path.exists(DATA_FILE):
        return {
            "authors": [],
            "editors": [],
            "books": []
        }

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return {
            "authors": [],
            "editors": [],
            "books": []
        }


def save_data(data):
    """
    Save dictionary data to database.json.
    """

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)