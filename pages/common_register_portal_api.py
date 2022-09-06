import requests
from utilities import HtmlReader
from utilities import json_reader
from utilities import payload_modification
from utilities import csv_writer
from config.api_endpoints import Endpoints


from config.file_path import FilePath

api_end_point = Endpoints()
file_path = FilePath()


class CommonRegisterPortalApi:
    payLoad = {}
    header = {}
    all_program = []
    postUrl = api_end_point.POST_URL
    getUrl = api_end_point.GET_URL
    cities_code_payload_file_path = file_path.city_code
    post_payload_file_path = file_path.post_request_payload
    get_request_header_path = file_path.get_request_header_path

    def get_cookie_session_id(self):
        parameter = self.payLoad
        response = requests.post(self.postUrl, params=parameter);
        return response.headers.get('Set-Cookie').split(';')[0];

    def get_data_of_get_api(self):
        res = requests.session()
        self.header = payload_modification.payload_update(self.get_request_header_path,"Cookie", self.get_cookie_session_id())
        try:

            response = res.get(self.getUrl, headers=self.header, stream=True,timeout=200)
        except requests.exceptions.Timeout as e:
            print(e)
        return response

    def get_data_against_cities(self):
        self.get_cities_values()
        result = {}
        cities_json = json_reader.json_data_reader(self.cities_code_payload_file_path)
        for city in cities_json:
            self.payLoad = payload_modification.payload_update(self.post_payload_file_path, "form:registergericht_input" ,cities_json[city])
            result[city] = HtmlReader.HtmlParser.getAllTagsValues(self.get_data_of_get_api())
        return result

    def write_city_into_csv(self, results):
        for key in results.keys():
            self.all_program.append({
                "city_name": key,
                "program_name": str(results[key])
            })
            csv_writer.csv_writer(self.all_program)

    def get_cities_values(self):
        response = requests.post(self.postUrl)
        result = HtmlReader.HtmlParser.get_option_name_and_value(response)
        payload_modification.payload_writer(self.cities_code_payload_file_path, result)