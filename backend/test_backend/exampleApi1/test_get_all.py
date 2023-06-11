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


@pytest.mark.PBI("numberPBI")
@pytest.mark.ExampleAPI1
@pytest.mark.API
class TestGetAll:

    # region Setup
    def setup_class(self):
        self.example_api = ExampleAPI()

    # endregion

    # region Tests - Status 200
    def test_get_all_successfully(self):
        """
        TC-
        Verify response with successful execution
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Required params.")
        response = self.example_api.get_all(paramEx1=1, paramEx2=10)
        ApiValidations.response_status_200(response)
        self.example_api.validate_response_model_get_all(response)

    def test_get_all_successfully_with_optional_parameter(self):
        """
        TC-
        Verify response with successful execution using optional parameter
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Optional params.")
        response = self.example_api.get_all(paramEx1=1, paramEx2=10, paramEx3='1', paramEx4='10')
        ApiValidations.response_status_200(response)
        self.example_api.validate_response_model_get_all(response)

    def test_get_all_no_matches(self):
        """
        TC-
        Verify response without matches
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: register not found.")
        response = self.example_api.get_all(paramEx1='write an example no matches')
        ApiValidations.response_status_200(response)
        self.example_api.validate_response_model_not_found(response)

    # endregion

    # region Tests - Status 400
    def test_get_all_parameters_with_incorrect_data_type(self):
        """
        TC-
        Verify response when executing parameters with incorrect data type
        """
        with soft_assertions():
            # region paramEx1 type bool
            logging.info(f"\n{'-' * 10} SCENARIO:: 'paramEx1' = True.")
            response = self.example_api.get_all(paramEx1=True, paramEx2=1)
            ApiValidations.response_status_400(response, ["'paramEx1' is not the correct type."])
            # endregion

            # region paramEx2 type bool
            logging.info(f"\n{'-' * 10} SCENARIO:: 'paramEx2' = True.")
            response = self.example_api.get_all(paramEx1=1, paramEx2=True)
            ApiValidations.response_status_400(response, ["'paramEx2' is not the correct type."])
            # endregion

    def test_get_all_parameters_with_invalid_data(self):
        """
        TC-
        Verify response when executing parameters with invalid data
        """
        with soft_assertions():
            # region paramEx1 = 0
            logging.info(f"\n{'-' * 10} SCENARIO:: 'paramEx1' = 0.")
            response = self.example_api.get_all(paramEx1=0, paramEx2=1)
            ApiValidations.response_status_400(response, ["'paramEx1' must be greater than '0'."])
            # endregion

    def test_get_all_unspecific_extra_parameter(self):
        """
        TC-
        Verify response with unspecific extra parameter
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Extra param..")
        response = self.example_api.get_all(paramEx1=1, paramEx2=1, extra='test')
        ApiValidations.response_status_400(response, ["'extra' is unknown property."])

    def test_get_all_without_required_parameters(self):
        """
        TC-
        Verify response when executing without required parameters
        """
        with soft_assertions():
            # region without paramEx1
            logging.info(f"\n{'-' * 10} SCENARIO:: Without 'paramEx1'.")
            response = self.example_api.get_all(paramEx2=1)
            ApiValidations.response_status_400(response, ["'paramEx1' must not be empty."])
            # endregion

            # region paramEx1 empty
            logging.info(f"\n{'-' * 10} SCENARIO:: 'paramEx1' = null.")
            response = self.example_api.get_all(paramEx1='null', paramEx2=1)
            ApiValidations.response_status_400(response, ["'paramEx1' must not be empty."])
            # endregion

    def test_get_all_without_token(self):
        """
        TC-
        Verify response when executing without token
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Without token.")
        response = self.example_api.get_all('without token')
        ApiValidations.response_status_400(response, ["'Bearer Token' is required."])

    def test_get_all_without_bearer(self):
        """
        TC-
        Verify response when executing without bearer
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Without bearer.")
        response = self.example_api.get_all('without bearer')
        ApiValidations.response_status_400(response, ["'Bearer Schema' is required."])

    def test_get_all_without_authorization(self):
        """
        TC-
        Verify response when executing without authorization
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Without authorization.")
        response = self.example_api.get_all('without authorization')
        ApiValidations.response_status_400(response, ["Header Authorization is required."])

    # endregion

    # region Tests - Status 401
    def test_get_all_wrong_token(self):
        """
        TC-
        Verify response when executing with wrong token
        """
        logging.info(f"\n{'-' * 10} SCENARIO:: Wrong token.")
        response = self.example_api.get_all('wrong token')
        ApiValidations.response_status_401(response)
    # endregion
