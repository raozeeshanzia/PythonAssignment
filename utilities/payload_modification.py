import json


def payload_update(payload_path, key, updated_value):
    with open(payload_path) as json_data:
        data = json.load(json_data)
    if key in data:
        data[key] = updated_value
    with open(payload_path, 'w') as fp:
        json.dump(data, fp)
    return data


def payload_writer(payload_path, result):
    with open(payload_path, 'w') as fp:
        json.dump(result, fp)
    return result