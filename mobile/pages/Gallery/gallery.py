import logging

from mobile.general.mo_tasks import MoTasks
from mobile.general.mo_validations import MoValidations
from mobile.pages.mo_general_page import MoGeneralPage


class GalleryPage:

    def __init__(self, driver):
        self.driver = driver

    # region Actions
    def example_action(self, param1, param2):
        logging.info(f"This is an example: {param1}")
        MoTasks.send_keys(self.driver, param1, MoGeneralPage.elem('id', 'IdExample'))
        MoTasks.send_keys(self.driver, param2, MoGeneralPage.elem('id', 'IdExample2'))
        MoTasks.click(self.driver, MoGeneralPage.elem('id', 'IdExample3'))
    # endregion

    # region Validations
    def elements_gallery(self):
        MoValidations.visualize(self.driver, MoGeneralPage.elem('text', 'Camera'))
    # endregion
