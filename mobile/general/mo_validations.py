import logging as log

from mobile.general.mo_tasks import MoTasks


class MoValidations:

    @staticmethod
    def validate_text(driver, label, text):
        label = MoTasks.get_element(driver, label)
        try:
            assert text == label.text
        except AssertionError:
            log.error("Expected: '%s'. And got: '%s'", text, label.text)
            raise

    @staticmethod
    def visualize(driver, locator):
        is_visible = bool(driver.find_elements(*locator))
        try:
            assert is_visible
        except AssertionError:
            log.error("Element is not visible: ", locator)
            raise

    @staticmethod
    def is_checked(driver, locator):
        checked = MoTasks.get_element(driver, locator).get_attribute("checked")
        try:
            assert "true" == checked
        except AssertionError:
            log.error("The element: '%s' is not checked.", locator)
            raise

    @staticmethod
    def is_not_checked(driver, locator):
        checked = MoTasks.get_element(driver, locator).get_attribute("checked")
        try:
            assert "false" == checked
        except AssertionError:
            log.error("The element: '%s' is checked.", locator)
            raise
