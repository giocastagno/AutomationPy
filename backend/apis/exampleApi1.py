import json
import logging

from assertpy import assert_that
from pydantic import ValidationError

from backend.general.api_tasks import ApiTasks
from backend.general.api_validations import ApiValidations
from backend.resources.models.exampleApi1 import ExampleModelGetId, ExampleModelGetAll, ExampleModelGetEnabled, \
    ExampleModelPostCreate, ExampleModelPutUpdate, ExampleModelPatchEnabled, ExampleModelNotFound


class ExampleAPI:

    @staticmethod
    def path():
        path = '/api/example'
        return path

    # region Methods
    def get_id(self, _id, *scenario, **query_params):
        endpoint = f'{self.path()}/get/{_id}'
        response = ApiTasks.scenario_constructor(method='GET', endpoint=endpoint, query_params=query_params,
                                                 scenario=scenario)
        return response

    def get_all(self, *scenario, **query_params):
        endpoint = f'{self.path()}/getall'
        response = ApiTasks.scenario_constructor(method='GET', endpoint=endpoint, query_params=query_params,
                                                 scenario=scenario)
        return response

    def get_enabled(self, *scenario, **query_params):
        endpoint = f'{self.path()}/get/enabled'
        response = ApiTasks.scenario_constructor(method='GET', endpoint=endpoint, query_params=query_params,
                                                 scenario=scenario)
        return response

    def post_create(self, payload, *scenario, **query_params):
        endpoint = f'{self.path()}/create'
        response = ApiTasks.scenario_constructor(method='POST', endpoint=endpoint, query_params=query_params,
                                                 scenario=scenario, payload=payload)
        return response

    def put_update(self, _id, payload, *scenario, **query_params):
        endpoint = f'{self.path()}/update/{_id}'
        response = ApiTasks.scenario_constructor(method='PUT', endpoint=endpoint, query_params=query_params,
                                                 scenario=scenario, payload=payload)
        return response

    def patch_enabled(self, _id, *scenario, **query_params):
        endpoint = f'{self.path()}/enabled/{_id}'
        response = ApiTasks.scenario_constructor(method='PATCH', endpoint=endpoint, query_params=query_params,
                                                 scenario=scenario)
        return response

    # endregion

    # region Actions
    def reset_updated_data(self, updated_id, reset_json):
        payload = ApiTasks.body_constructor(json.dumps(reset_json))
        ApiValidations.response_status_200(self.put_update(updated_id, payload))
        logging.info("Test data updated.")

    # endregion

    # region Validate update
    def validate_updated_json_of_id(self, updated_id, expected_json):
        response = self.get_id(updated_id)
        model = self.validate_response_model_get_id(response)
        if model.json() == json.dumps(expected_json):
            logging.info("Service updated correctly.")
        else:
            assert_that(model.json()).is_equal_to(json.dumps(expected_json))
            logging.error(f"Expected:\n {json.dumps(expected_json)}\n Got:\n {model.json()}")

    # endregion

    # region Validate model
    @staticmethod
    def validate_response_model_get_id(response):
        try:
            model = ExampleModelGetId(**response.json())
            assert_that(model.isSuccessfull).is_equal_to(True)
        except ValidationError:
            logging.error(f"Model error.\n Response body: {response.json()}")
            raise
        else:
            logging.info("Response model: OK")
            return model

    @staticmethod
    def validate_response_model_get_all(response):
        try:
            model = ExampleModelGetAll(**response.json())
            assert_that(model.isSuccessfull).is_equal_to(True)
        except ValidationError:
            logging.error(f"Model error.\n Response body: {response.json()}")
            raise
        else:
            logging.info("Response model: OK")
            return model

    @staticmethod
    def validate_response_model_get_enabled(response):
        try:
            model = ExampleModelGetEnabled(**response.json())
            assert_that(model.isSuccessfull).is_equal_to(True)
        except ValidationError:
            logging.error(f"Model error.\n Response body: {response.json()}")
            raise
        else:
            logging.info("Response model: OK")
            return model

    @staticmethod
    def validate_response_model_post_create(response):
        try:
            model = ExampleModelPostCreate(**response.json())
            assert_that(model.isSuccessfull).is_equal_to(True)
        except ValidationError:
            logging.error(f"Model error.\n Response body: {response.json()}")
            raise
        else:
            logging.info("Response model: OK")
            return model

    @staticmethod
    def validate_response_model_put_update(response):
        try:
            model = ExampleModelPutUpdate(**response.json())
            assert_that(model.isSuccessfull).is_equal_to(True)
        except ValidationError:
            logging.error(f"Model error.\n Response body: {response.json()}")
            raise
        else:
            logging.info("Response model: OK")
            return model

    @staticmethod
    def validate_response_model_patch_enabled(response):
        try:
            model = ExampleModelPatchEnabled(**response.json())
            assert_that(model.isSuccessfull).is_equal_to(True)
        except ValidationError:
            logging.error(f"Model error.\n Response body: {response.json()}")
            raise
        else:
            logging.info("Response model: OK")
            return model

    @staticmethod
    def validate_response_model_not_found(response):
        try:
            model = ExampleModelNotFound(**response.json())
            assert_that(model.isSuccessfull).is_equal_to(True)
            assert_that(model.message).is_equal_to("No results found.")
        except ValidationError:
            logging.error(f"Model error.\n Response body: {response.json()}")
            raise
        else:
            logging.info("Response model: OK")
            return model
    # endregion
