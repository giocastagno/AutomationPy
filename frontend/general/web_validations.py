import logging
import logging as log

from assertpy import assert_that
from selenium.webdriver.common.by import By

from frontend.general.web_tasks import WebTasks
from frontend.pages import web_general_page


class WebValidations:

    # region Global
    @staticmethod
    def validate_text(driver, label, text):
        label = WebTasks.get_element(driver, label)
        try:
            assert_that(text).is_equal_to(label.text)
            logging.info(f"Text is: '{text}'.")
        except AssertionError:
            log.error("Expected: '%s'. And got: '%s'", text, label.text)
            raise

    @staticmethod
    def validate_placeholder(driver, field, placeholder):
        field = WebTasks.get_element(driver, field)
        try:
            assert_that(placeholder).is_equal_to(field.get_attribute('placeholder'))
            logging.info(f"Placeholder is: '{placeholder}'.")
        except AssertionError:
            log.error("Expected: '%s'. And got: '%s'", placeholder, field.get_attribute('placeholder'))
            raise

    @staticmethod
    def visualize(driver, locator):
        is_visible = bool(driver.find_elements(*locator))
        try:
            assert_that(is_visible)
            logging.info(f"Is visible: '{locator}'.")
        except AssertionError:
            log.error("Element is not visible: ", locator)
            raise

    @staticmethod
    def is_selected(driver, locator):
        element = driver.find_element(By.XPATH, locator[1])
        loc = locator[1].split("text()")[1].split("'")[1]
        try:
            assert element.is_selected()
            logging.info(f"Is selected: '{loc}'.")
        except AssertionError:
            log.error("Element is not selected: ", loc)
            raise

    @staticmethod
    def is_not_selected(driver, locator):
        element = driver.find_element(By.XPATH, locator[1])
        loc = locator[1].split("text()")[1].split("'")[1]
        try:
            assert not element.is_selected()
            logging.info(f"Is not selected: '{loc}'.")
        except AssertionError:
            log.error("Element is selected: ", loc)
            raise

    @staticmethod
    def validate_text_list(driver, locator, texts):
        colum_titles = []
        visible_head_table = driver.find_elements(By.XPATH, locator[1])
        try:
            for colum in visible_head_table:
                colum_titles.append(colum.text)
            assert_that(texts).is_equal_to(colum_titles)
            logging.info(f"Texts are: '{texts}'.")
        except AssertionError:
            log.error("\nExpected: \n'%s'. \nAnd got: \n'%s'", texts, colum_titles)
            raise

    @staticmethod
    def validate_text_of_colum(driver, colum, text):
        label = WebTasks.get_element(driver, (By.XPATH, f"//table/tbody/tr[1]/td[{colum}]"))
        try:
            assert_that(text).is_equal_to(label.text)
            logging.info(f"Text is: '{text}' in colum {colum}.")
        except AssertionError:
            log.error("Expected: '%s'. And got: '%s'", text, label.text)
            raise

    @staticmethod
    def is_disabled(driver, field):
        field = WebTasks.get_element(driver, field)
        try:
            assert_that(field.get_attribute('class')).contains("disabled")
            logging.info(f"Is disabled: '{field}'.")
        except AssertionError:
            log.error("Expected: '%s', disabled, and it is enabled", field)
            raise
    # endregion
