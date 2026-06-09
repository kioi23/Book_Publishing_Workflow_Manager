# This module provides utility functions for saving and loading data to and from JSON files. It includes functions to save data to a file, load data from a file, and ensure that the necessary directories exist for storing the data.
import json
import os


# Save - saves data to a JSON file. It takes the data to be saved and the filename as arguments, and writes the data to the specified file in JSON format.
def save_data(data):

    with open( # Opens the file "data/database.json" in write mode. If the file does not exist, it will be created. If it already exists, its contents will be overwritten.
        "data/database.json",
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

# Load - loads data from a JSON file. It takes the filename as an argument, reads the data from the specified file, and returns it as a Python object.
def load_data():

    if not os.path.exists(
        "data/database.json"
    ):
        return {}

    try:
        # Opens the file "data/database.json" in read mode. If the file does not exist, it will raise a FileNotFoundError, which is handled by the if statement above. If the file exists but contains invalid JSON, it will raise a JSONDecodeError, which is handled by the except block below.

        with open(
            "data/database.json",
            "r"
        ) as file:

            return json.load(file)

    except json.JSONDecodeError: # If a JSONDecodeError occurs while trying to load the data from the file, it means that the file contains invalid JSON. In this case, the function returns an empty dictionary to indicate that no valid data could be loaded.

        return {}