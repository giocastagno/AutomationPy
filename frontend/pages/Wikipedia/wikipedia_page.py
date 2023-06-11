from selenium.webdriver.common.by import By

from frontend.general.web_tasks import WebTasks
from frontend.general.web_validations import WebValidations
from frontend.pages.web_general_page import WebGeneralPage

# region Input
INPUT_EXAMPLE = (By.XPATH, "//*[@id='example']/div/input")


# endregion

# region List
# endregion


class WikipediaPage:

    def __init__(self, driver):
        self.driver = driver

    # region Actions
    def go_to_new_action(self):
        WebTasks().open_site(self.driver, 'wikipedia')
        WebTasks.send_keys(self.driver, "search test", WebGeneralPage.elem('INPUT', 'Search'))
        WebTasks().click(self.driver, WebGeneralPage.elem('BUTTON', 'Search'))

    # endregion

    # region Validations
    def validate_example_page(self):
        WebValidations.visualize(self.driver, WebGeneralPage.elem('SUBTITLE', 'Example1'))
        WebValidations.visualize(self.driver, WebGeneralPage.elem('LABEL_2', 'Example1'))
        WebValidations.visualize(self.driver, WebGeneralPage.elem('BUTTON', 'Example1'))
    # endregion
