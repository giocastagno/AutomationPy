import logging

from selenium.webdriver.common.by import By

from frontend.general.web_tasks import WebTasks
from frontend.pages.web_general_page import WebGeneralPage

# region Field
FIELD_USERNAME = (By.XPATH, "//input[@name='email']")
FIELD_PASSWORD = (By.XPATH, "//input[@name='password']")


# endregion


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # region Actions
    def log_in(self, user, password):
        logging.info(f"Loging in as: {user}.")
        WebTasks.send_keys(self.driver, user, FIELD_USERNAME)
        WebTasks.send_keys(self.driver, password, FIELD_PASSWORD)
        WebTasks.click(self.driver, WebGeneralPage.elem('BUTTON', 'Login'))
    # endregion

    # region Validations
    # endregion
