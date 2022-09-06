import json


# Read data from yml file #
def json_data_reader(filepath):
    with open(filepath, 'r') as file:
        if len(file.readlines()) != 0:
            file.seek(0)
            payload = json.load(file)
            return payload
