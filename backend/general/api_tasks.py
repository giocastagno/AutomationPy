import json
import logging
import pathlib
import random

import requests

from config_loader import read_config_from_current_env


class ApiTasks:

    @staticmethod
    def body_constructor(api, body=None, *list_name, **kwargs):
        if "{" not in api:
            body = json.load(
                open(str(pathlib.Path(__file__).parent.parent.absolute()) + f"/resources/body/{api}/{body}.json", 'r'))
        else:
            body = json.loads(api)
        for key, value in kwargs.items():
            if value == 'delete-param':
                if len(list_name) == 0:
                    del body[key]
                else:
                    del body[list_name[0]][key]
            else:
                if len(list_name) == 0:
                    body[key] = value
                else:
                    body[list_name[0]][key] = value
        return json.dumps(body)

    @staticmethod
    def __get_token(token='postAuthenticate(Required)'):
        base_url = read_config_from_current_env('base_url_api')
        url_token = f"{base_url}/path/authenticator"
        headers = {"Content-Type": "application/json"}
        payload = ApiTasks.body_constructor('identity', token)
        response = requests.post(url=url_token, data=payload, headers=headers)
        if response.status_code == 200:
            return response.json()['data']['token']
        else:
            logging.error(f"Get token error.\n Status: {response.status_code}\n Body: {response.json()}")
            return False

    @staticmethod
    def scenario_constructor(**kwargs):
        """
        Build test scenarios with parameters to send request.
        :param kwargs: method, endpoint, query_params, scenario, payload.
        :return: response
        """
        # region Argumentos
        arg = {"method": "",
               "endpoint": "",
               "query_params": {},
               "scenario": "",
               "payload": {}}
        # endregion

        # region Constructor de parámetros
        for key, value in kwargs.items():
            arg[key] = value
        # endregion

        # region URL
        base_url = read_config_from_current_env('base_url_api')
        url = f"{base_url}{arg['endpoint']}"
        if arg['query_params'] != {}:
            query_paramss = ''
            n = 0
            for key, value in arg['query_params'].items():
                query_paramss += f"{key}={value}"
                if n < len(arg["query_params"]) - 1:
                    query_paramss += "&"
                n += 1
            url += f"?{query_paramss}"
        # endregion

        # region Headers
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {ApiTasks.__get_token()}"}
        # endregion

        # region Test scenarios
        if len(arg['scenario']) == 0:
            response = ApiTasks.send_request(method=arg['method'], url=url, headers=headers,
                                             payload=arg['payload'])
        elif arg['scenario'][0] == "without token":
            logging.info("Sending request without token")
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer "
            }
            response = ApiTasks.send_request(method=arg['method'], url=url, headers=headers, payload=arg['payload'])
        elif arg['scenario'][0] == "without bearer":
            logging.info("Sending request without bearer")
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"{ApiTasks.__get_token()}"
            }
            response = ApiTasks.send_request(method=arg['method'], url=url, headers=headers, payload=arg['payload'])
        elif arg['scenario'][0] == "wrong token":
            logging.info("Sending request with wrong token")
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ6WTcwTnJDZUEwTW",
            }
            response = ApiTasks.send_request(method=arg['method'], url=url, headers=headers, payload=arg['payload'])
        elif arg['scenario'][0] == "without authorization":
            logging.info("Sending request with wrong token")
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            response = ApiTasks.send_request(method=arg['method'], url=url, headers=headers,
                                             payload=arg['payload'])
        elif arg['scenario'][0] == 'without required path parameters':
            logging.info("Sending request without required path parameters")
            url_without_req_path_param = url.split('/None')[0]
            response = ApiTasks.send_request(method=arg['method'], url=url_without_req_path_param, headers=headers,
                                             payload=arg['payload'])
        else:
            response = None
        return response
        # endregion

    @staticmethod
    def send_request(**kwargs):
        """
        Send http method with parameters to get api response.
        :param kwargs: method, url, headers, payload.
        :return: response
        """

        # region Parameters
        params = {"method": "",
                  "url": "",
                  "headers": "",
                  "payload": {}}
        # endregion

        # region Build parameters
        for key, value in kwargs.items():
            params[key] = value
        # endregion

        # region HTTP methods
        if params['method'] == 'GET':
            logging.info("Sending GET request")
            response = requests.get(url=params['url'], headers=params['headers'])
        elif params['method'] == 'POST':
            logging.info("Sending POST request")
            response = requests.post(url=params['url'], data=params['payload'], headers=params['headers'])
        elif params['method'] == 'PUT':
            logging.info("Sending PUT request")
            response = requests.put(url=params['url'], data=params['payload'], headers=params['headers'])
        elif params['method'] == 'PATCH':
            logging.info("Sending PATCH request")
            response = requests.patch(url=params['url'], data=params['payload'], headers=params['headers'])
        else:
            response = None
        return response
        # endregion

    @staticmethod
    def random_rfc():
        return f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}" \
               f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randrange(100000, 999999)}" \
               f"{random.randrange(110, 999)}"
