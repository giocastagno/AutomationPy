import logging

import allure
import pytest
from assertpy import soft_assertions

from backend.apis.exampleApi1 import ExampleAPI
from backend.general.api_validations import ApiValidations

pytestmark = [
    allure.parent_suite('Backend'),
    allure.suite('ExampleAPI1')
]


@pytest.mark.PBI("number PBI")
@pytest.mark.ExampleAPI1
@pytest.mark.API
class TestGetId:

    # region Setup
    def setup_class(self):
        self.example_api = ExampleAPI()

    # endregion

    # region Tests - Status 200
    def test_get_id_successfully(self):
        """
        TC-
        Verify response with successful execution
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Valid 'id'.")
        response = self.example_api.get_id(2)
        ApiValidations.response_status_200(response)
        self.example_api.validate_response_model_get_id(response)

    def test_get_id_no_matches(self):
        """
        TC-
        Verify response without matches
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: 'id' not found.")
        response = self.example_api.get_id(99999)
        ApiValidations.response_status_200(response)
        self.example_api.validate_response_model_not_found(response)

    # endregion

    # region Tests - Status 400
    def test_get_id_parameters_with_incorrect_data_type(self):
        """
        TC-
        Verify response when executing parameters with incorrect data type
        """
        with soft_assertions():
            # region Id string
            logging.info(f"\n{'-' * 10} SCENARIO:: 'id' type string.")
            response = self.example_api.get_id("a")
            ApiValidations.response_status_400(response, ["'id' is not the correct type."])
            # endregion

            # region Id long
            logging.info(f"\n{'-' * 10} SCENARIO:: 'id' type long.")
            response = self.example_api.get_id(2147483648)
            ApiValidations.response_status_400(response, ["'id' is not the correct type."])
            # endregion

            # region Id boolean
            logging.info(f"\n{'-' * 10} SCENARIO:: 'id' type bool.")
            response = self.example_api.get_id(True)
            ApiValidations.response_status_400(response, ["'id' is not the correct type."])
            # endregion

    def test_get_id_parameters_with_invalid_data(self):
        """
        TC-
        Verify response when executing parameters with invalid data
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: 'id' = 0.")
        response = self.example_api.get_id(0)
        ApiValidations.response_status_400(response, ["'id' must be greater than '0'."])

    def test_get_id_unspecific_extra_parameter(self):
        """
        TC-
        Verify response with unspecific extra parameter
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Extra param.")
        response = self.example_api.get_id(2, extra='test')
        ApiValidations.response_status_400(response, ["'extra' is unknown property."])

    def test_get_id_without_required_parameters(self):
        """
        TC-
        Verify response when executing without required parameters
        """
        with soft_assertions():
            # region Id = None
            logging.info(f"\n{'-' * 10} SCENARIO:: 'id' = None.")
            response = self.example_api.get_id(None, 'without required path parameters')
            ApiValidations.response_status_400(response, ["'id' must not be empty."])
            # endregion

            # region Id = 'null'
            logging.info(f"\n{'-' * 10} SCENARIO:: 'id' = 'null'.")
            response = self.example_api.get_id('null')
            ApiValidations.response_status_400(response, ["'id' must not be empty."])
            # endregion

            # region Id = ''
            logging.info(f"\n{'-' * 10} SCENARIO:: 'id' = ''.")
            response = self.example_api.get_id('')
            ApiValidations.response_status_400(response, ["'id' must not be empty."])
            # endregion

    def test_get_id_without_token(self):
        """
        TC-
        Verify response when executing without token
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Without token.")
        response = self.example_api.get_id(2, 'without token')
        ApiValidations.response_status_400(response, ["'Bearer Token' is required."])

    def test_get_id_without_bearer(self):
        """
        TC-
        Verify response when executing without bearer
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Without bearer.")
        response = self.example_api.get_id(2, 'without bearer')
        ApiValidations.response_status_400(response, ["'Bearer Schema' is required."])

    def test_get_id_without_authorization(self):
        """
        TC-
        Verify response when executing without authorization
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Without authorization.")
        response = self.example_api.get_id(2, 'without authorization')
        ApiValidations.response_status_400(response, ["Header Authorization is required."])

    # endregion

    # region Tests - Status 401
    def test_get_id_wrong_token(self):
        """
        TC-
        Verify response when executing with wrong token
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Wrong token.")
        response = self.example_api.get_id(2, 'wrong token')
        ApiValidations.response_status_401(response)
    # endregion
