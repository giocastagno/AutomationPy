import logging
from time import sleep

from mobile.general.mo_tasks import MoTasks
from mobile.general.mo_validations import MoValidations
from mobile.pages.mo_general_page import MoGeneralPage

# region Button
BUTTON_1 = ("ID", "com.android.calculator2:id/digit_1")
BUTTON_MUL = ("ID", "com.android.calculator2:id/op_mul")
BUTTON_EQUAL = ("ID", "com.android.calculator2:id/eq")
# endregion

# region Combo
COMBO_INDUSTRY = ("XPATH", "//*[@resource-id='input_1_9']")
COMBO_STUDENT = ("XPATH", "//*[@resource-id='input_1_11']")
COMBO_SYSTEM = ("XPATH", "//*[@resource-id='input_1_10']")
COMBO_COUNTRY = ("XPATH", "//*[@resource-id='input_1_13']")
# endregion

# region Field
FIELD_FNAME = ("XPATH", "//*[@resource-id='input_1_3']")
FIELD_LNAME = ("XPATH", "//*[@resource-id='input_1_4']")
FIELD_BMAIL = ("XPATH", "//*[@resource-id='input_1_30']")
FIELD_COMPANY = ("XPATH", "//*[@resource-id='input_1_6']")
FIELD_JOB = ("XPATH", "//*[@resource-id='input_1_8']")
FIELD_PHONE = ("XPATH", "//*[@resource-id='input_1_31']")
# endregion

# region Option
OPTION_EDUCATION = ("XPATH", "//*[@text='Education']")
OPTION_NO = ("XPATH", "//*[@text='No']")
OPTION_WIN64 = ("XPATH", "//*[@text='Windows 64-bit']")
OPTION_USA = ("XPATH", "//*[@text='United States']")
# endregion

# region Checkbox
CHECKBOX_RECAPTCHA = ("XPATH", "//*[@resource-id='recaptcha-anchor']")
# endregion

# region Label
LABEL_RESULT = ("ID", "com.android.calculator2:id/result")
# endregion


class ExamplePage:

    def __init__(self, driver):
        self.driver = driver

    # region Actions
    def multiply(self):
        logging.info("Multiplying")
        MoTasks.click(self.driver, BUTTON_1)
        MoTasks.click(self.driver, MoGeneralPage.elem('CALCULATOR', 'digit_2'))
        MoTasks.click(self.driver, BUTTON_MUL)
        MoTasks.click(self.driver, MoGeneralPage.elem('CALCULATOR', 'digit_2'))
        MoTasks.click(self.driver, BUTTON_EQUAL)

    def search(self):
        logging.info("Searching")
        MoTasks.click(self.driver, MoGeneralPage.elem('CHROME', 'url_field'))
        MoTasks.clear(self.driver, MoGeneralPage.elem('CHROME', 'url_field'))
        MoTasks.send_keys_and_enter(self.driver, 'ranorex.com/free-trial/', MoGeneralPage.elem('CHROME', 'url_field'))

    def complete_form(self):
        logging.info("Completing")
        sleep(4)
        MoTasks.scroll(self.driver, 'DOWN')
        MoTasks.scroll(self.driver, 'DOWN')
        MoTasks.scroll(self.driver, 'DOWN')
        MoTasks.send_keys(self.driver, 'Robot', FIELD_FNAME)
        MoTasks.send_keys(self.driver, 'Automatizado', FIELD_LNAME)
        MoTasks.send_keys(self.driver, 'robon.qaa@test.com', FIELD_BMAIL)
        MoTasks.send_keys(self.driver, 'TESTING', FIELD_COMPANY)
        MoTasks.send_keys(self.driver, 'QAA', FIELD_JOB)
        MoTasks.send_keys(self.driver, '3512345678', FIELD_PHONE)
        MoTasks.scroll(self.driver, 'DOWN')
        MoTasks.scroll(self.driver, 'DOWN')
        MoTasks.select_an_option_in_the_combo(self.driver, COMBO_INDUSTRY, OPTION_EDUCATION)
        MoTasks.select_an_option_in_the_combo(self.driver, COMBO_STUDENT, OPTION_NO)
        MoTasks.select_an_option_in_the_combo(self.driver, COMBO_SYSTEM, OPTION_WIN64)
        MoTasks.select_an_option_in_the_combo(self.driver, COMBO_COUNTRY, OPTION_USA)
        MoTasks.scroll(self.driver, 'DOWN')
        MoTasks.click(self.driver, CHECKBOX_RECAPTCHA)
    # endregion

    # region Validations
    def validate_result(self):
        logging.info("Validating result")
        MoValidations.validate_text(self.driver, LABEL_RESULT, '24')
    # endregion
