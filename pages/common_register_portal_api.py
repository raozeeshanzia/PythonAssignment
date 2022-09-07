import requests
from utilities import general
from config import constant


class CommonRegisterPortalApi:
    cities_code_payload_file_path = constant.CITY_CODE
    post_payload_file_path = constant.POST_REQUEST_PAYLOAD
    get_request_header_path = constant.GET_REQUEST_HEADER_PATH

    def get_cookie_session_id(self):
        payload = general.json_data_reader(self.post_payload_file_path)
        response = requests.post(constant.POST_URL, params=payload)
        return response.headers.get('Set-Cookie').split(';')[0]

    def get_data_of_get_api(self):
        res = requests.session()
        header = general.payload_update(self.get_request_header_path,"Cookie", self.get_cookie_session_id())
        response = res.get(constant.GET_URL, headers=header, stream=True,timeout=200)
        return response

    def get_data_against_cities(self):
        self.get_cities_values()
        result = {}
        cities_json = general.json_data_reader(self.cities_code_payload_file_path)
        for city in cities_json:
            general.payload_update(self.post_payload_file_path, "form:registergericht_input" ,cities_json[city])
            result[city] = general.get_all_tags_values(self.get_data_of_get_api())
        return result

    def write_city_into_csv(self, results):
        all_program = []
        for key in results.keys():
            all_program.append({
                "city_name": key,
                "program_name": str(results[key])
            })
            general.csv_writer(all_program)

    def get_cities_values(self):
        response = requests.post(constant.POST_URL)
        result = general.get_option_name_and_value(response)
        general.payload_writer(self.cities_code_payload_file_path, result)