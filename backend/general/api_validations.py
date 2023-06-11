import logging

from assertpy import assert_that, soft_assertions
from pydantic import ValidationError


class ApiValidations:

    # region Success responses
    @staticmethod
    def response_status_200(response):
        try:
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response.reason).is_equal_to('OK')
        except AssertionError:
            logging.error(f"Status error.\n Status: {response.status_code}\n Body: {response.json()}")
            raise
        else:
            if response.status_code != 200:
                logging.error(f"Status code error.\n Response status: {response.status_code}.\t|\t Expected: 200.")
                logging.error(f"Body:\n {response.json()}")
            else:
                logging.info(f"Status OK: {response.status_code}")
    # endregion

    # region Error responses
    @staticmethod
    def response_status_400(response, errors):
        try:
            assert_that(response.status_code).is_equal_to(400)
            assert_that(response.reason).is_equal_to('Bad Request')
        except AssertionError:
            logging.error(f"Status error.\n Status: {response.status_code}\n Body: {response.json()}")
            raise
        else:
            if response.status_code != 400:
                logging.error(f"Status code error.\n Response status: {response.status_code}.\t|\t Expected: 400.")
            else:
                logging.info(f"Status OK: {response.status_code}")
        ApiValidations.validate_error_response_model(response, 'One or more errors have occurred.', errors)

    @staticmethod
    def response_status_401(response):
        logging.info("Validating status: 401")
        try:
            assert_that(response.status_code).is_equal_to(401)
            assert_that(response.reason).is_equal_to('Unauthorized')
            ApiValidations.validate_error_response_model(response, 'One or more errors have occurred.',
                                                         ['Bearer Token is invalid.'])
        except AssertionError:
            logging.error(response.json())
            raise

    @staticmethod
    def response_status_403(response, errors):
        logging.info("Validating status: 403")
        try:
            assert_that(response.status_code).is_equal_to(403)
            assert_that(response.reason).is_equal_to('Forbidden')
            ApiValidations.validate_error_response_model(response, '', errors)
        except AssertionError:
            logging.error(response.json())
            raise

    @staticmethod
    def response_status_500(response, errors):
        logging.info("Validating status: 500")
        try:
            assert_that(response.status_code).is_equal_to(500)
            assert_that(response.reason).is_equal_to('Server Error')
            ApiValidations.validate_error_response_model(response, '', errors)
        except AssertionError:
            logging.error(response.json())
            raise

    # endregion

    # region Validations
    @staticmethod
    def validate_error_response_model(response, message, errors):
        if response.text != "":
            with soft_assertions():
                try:
                    from backend.resources.models.error import ErrorModel
                    model = ErrorModel(**response.json())
                    assert_that(model.isSuccessfull).is_equal_to(False)
                    assert_that(model.message).is_equal_to(message)
                    if model.errors != errors:
                        assert_that(model.errors).is_equal_to(errors)
                        logging.error(f"Expected:\n {errors}\n Got:\n {model.errors}")
                except ValidationError:
                    logging.error(f"Model error.\n Response body: {response.json()}")
                else:
                    logging.info("Response model: OK")
    # endregion
