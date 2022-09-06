import re

from bs4 import BeautifulSoup


class HtmlParser:
    @staticmethod
    def getAllTagsValues(response):
        bs = BeautifulSoup(response.content, 'html.parser')
        res = bs.findAll('span', class_='marginLeft20')
        result = []
        for each in res:
            if each['class'][0] == 'marginLeft20' and len(each['class']) < 2:
                result.append(each.text)
        return result

    def get_option_name_and_value(response):
        bs = BeautifulSoup(response.content, 'html.parser')
        select_tag = bs.find('select', {"id":"form:registergericht_input"})
        options = select_tag.find_all('option')
        result = {}
        for index in range(2, 12):

            value = options[index]
            result[value.text] = value['value']
        return result




