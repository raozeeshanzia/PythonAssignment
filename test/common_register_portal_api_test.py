import unittest
from utilities import HtmlReader

from pages.common_register_portal_api import CommonRegisterPortalApi

api_obj = CommonRegisterPortalApi()


class CommonRegisterPortalApiTest(unittest.TestCase):
    def test_city_api(self):
        result = api_obj.get_data_against_cities()
        api_obj.write_city_into_csv(result)