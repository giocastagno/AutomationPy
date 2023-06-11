import logging
import pathlib
from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config_loader import read_config_from_current_env
from frontend.pages.web_general_page import WebGeneralPage


class WebTasks:

    # region Global
    @staticmethod
    def open_site(driver, site):
        base_url = read_config_from_current_env(site)
        driver.get(base_url)

    @staticmethod
    def get_element(driver, locator, timeout=20):
        try:
            element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        except (NoSuchElementException, TimeoutException):
            logging.info(f"Not found: '{locator[1]}'.")
        else:
            sleep(0.5)
            return element

    @staticmethod
    def click(driver, element):
        element = WebTasks.get_element(driver, element)
        return element.click()

    @staticmethod
    def wait_load_page(driver, timeout=5):
        sleep(2)
        try:
            WebDriverWait(driver, timeout).until_not(
                EC.presence_of_element_located((By.XPATH, "//body//span[text()='Loading...']")))
        except (NoSuchElementException, TimeoutException):
            print()

    @staticmethod
    def send_keys(driver, text, field):
        element = WebTasks.get_element(driver, field)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        return element.send_keys(text)

    @staticmethod
    def select_option(driver, combo, option):
        WebTasks.click(driver, combo)
        option = WebTasks.get_element(driver, WebGeneralPage.elem('OPTION', option))
        WebTasks.click(driver, option)

    @staticmethod
    def autocomplete(driver, autocomplete, option):
        WebTasks.send_keys(driver, option, autocomplete)
        WebTasks.click(driver, WebGeneralPage.elem('OPTION', option))

    @staticmethod
    def redirect_to_site(driver, site):
        base_url = read_config_from_current_env(site)
        driver.get(base_url)

    @staticmethod
    def open_new_tab(driver):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

    @staticmethod
    def scroll(driver, scroll):
        html: WebElement = driver.find_element_by_xpath('/html')
        if scroll == 'PAGE_UP':
            html.send_keys(Keys.PAGE_UP)
        elif scroll == 'PAGE_DOWN':
            html.send_keys(Keys.PAGE_DOWN)
        elif scroll == 'HOME':
            html.send_keys(Keys.HOME)
        elif scroll == 'END':
            html.send_keys(Keys.END)

    @staticmethod
    def focus_and_click(driver, element):
        element = WebTasks.get_element(driver, element)
        sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(false);", element)
        return WebTasks.click(driver, element)

    @staticmethod
    def paste_in(driver, field):
        element = WebTasks.get_element(driver, field)
        return element.send_keys(Keys.CONTROL, 'v')

    @staticmethod
    def upload_file(driver, file, section=1):
        field = WebTasks.get_element(driver, WebGeneralPage.elem('FILE', section))
        return field.send_keys(str(pathlib.Path(
            __file__).parent.parent.parent.parent.absolute()) + f"/frontend/src/resources/files/{file}")
    # endregion
