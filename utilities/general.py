import csv
import json

from bs4 import BeautifulSoup


def csv_writer(all_product):
    keys = []
    if len(keys) == 0:
        keys = all_product[0].keys()
    with open('expected_result/csv/city_list.csv', 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, keys)
        writer.writeheader()
        writer.writerows(all_product)


def get_all_tags_values(response):
    bs = get_response_content(response)
    res = bs.findAll('span', class_='marginLeft20')
    result = []
    for each in res:
        if each['class'][0] == 'marginLeft20' and len(each['class']) < 2:
            result.append(each.text)
    return result


def get_option_name_and_value(response):
    bs = get_response_content(response)
    select_tag = bs.find('select', {"id":"form:registergericht_input"})
    options = select_tag.find_all('option')
    result = {}
    for index in range(2, 12):

        value = options[index]
        result[value.text] = value['value']
    return result


def json_data_reader(filepath):
    with open(filepath, 'r') as file:
        if len(file.readlines()) != 0:
            file.seek(0)
            payload = json.load(file)
            return payload


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


def get_response_content(response):
    return BeautifulSoup(response.content, 'html.parser')
