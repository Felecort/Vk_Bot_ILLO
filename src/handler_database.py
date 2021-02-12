
from pprint import pprint
import json
data_filename = "../data/database.json"


def get_database():
    with open(data_filename, "r") as file:
        database = json.load(file)
    return database


def set_database(database):
    with open(data_filename, "w") as file:
        json.dump(database, file, indent=4, ensure_ascii=False)
