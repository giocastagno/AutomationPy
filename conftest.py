import json
import os
import pathlib

import allure
import pytest
from allure_commons.types import AttachmentType


@pytest.fixture()
def driverMO(request):
    if request.cls.pytestmark[0].name == 'MO':
        from appium import webdriver
        driverMO = None
        config = configuration()
        if config["mobile"]["device"] == 'Android_11':
            desired_cap = {
                "appium:deviceName": "emulator-5554",
                "platformName": "Android",
                "appium:appPackage": "com.android.gallery3d",
                "appium:appActivity": ".app.GalleryActivity"
            }
            driverMO = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
            driverMO.implicitly_wait(config["mobile"]["implicitly_wait"])
        yield driverMO
        driverMO.quit()


@pytest.fixture()
def driverWEB(request):
    if request.cls.pytestmark[0].name == 'WEB':
        from distutils import util
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        config = configuration()
        headless = util.strtobool(os.environ.get('headless'))
        driverWEB = None
        browser = config["web"]["browser"]
        if browser == 'Chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--lang=en")
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--window-size=1920,1080")
            if headless:
                chrome_options.add_argument('--headless')
            driverWEB = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        elif browser == 'MicrosoftEdge':
            edge_options = webdriver.EdgeOptions()
            edge_options.add_argument("--lang=en")
            edge_options.add_argument("--incognito")
            edge_options.add_argument("--window-size=2560,1440")
            if headless:
                edge_options.add_argument('--headless')
            driverWEB = webdriver.Edge(EdgeChromiumDriverManager().install(), options=edge_options)
        driverWEB.implicitly_wait(config["web"]["implicitly_wait"])
        yield driverWEB
        driverWEB.quit()


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='tst')
    parser.addoption('--headless', action='store', default='true', help='Hide=true. Display=false.')


def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["headless"] = config.getoption('headless')


def configuration():
    config_path = str(pathlib.Path(__file__).parent.absolute()) + '/config.json'
    with open(config_path) as config_file:
        config = json.load(config_file)
    return config


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Check if a test has failed and set a report attribute.
    :param item: request.node
    :return: item.setup/call/teardown.passed/failed
    """
    outcome = yield
    if item.cls.pytestmark[0].name != 'API':
        rep = outcome.get_result()
        if rep.when == 'call' or rep.when == 'setup':
            if rep.failed:
                # take screenshot
                file_name = f"{item.name}.png"
                path_screenshot = f"{pathlib.Path(__file__).parent.absolute()}/.screenshots/{file_name}"
                item.funcargs[item.fixturenames[0]].get_screenshot_as_file(path_screenshot)
                # attach screenshot to allure report
                allure.attach(item.funcargs[item.fixturenames[0]].get_screenshot_as_png(), name=file_name,
                              attachment_type=AttachmentType.PNG)
