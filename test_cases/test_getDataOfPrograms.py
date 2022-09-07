from pages.common_register_portal_api import CommonRegisterPortalApi
import pytest
api_obj = CommonRegisterPortalApi()


@pytest.mark.usefixtures
class TestCommonRegisterPortalApiTest:
    def test_city_api(self):
        result = api_obj.get_data_against_cities()
        api_obj.write_city_into_csv(result)


