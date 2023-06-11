import logging
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


class MoTasks:

    @staticmethod
    def get_element(driver, locator):
        element = None
        try:
            if locator[0] == "xpath":
                element = driver.find_element(By.XPATH, locator[1])
            elif locator[0] == "aid":
                element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, locator[1])
            elif locator[0] == "id":
                element = driver.find_element(By.ID, locator[1])
        except NoSuchElementException:
            logging.info(f"Not found: '{locator[1]}'.")
        else:
            return element

    @staticmethod
    def send_keys(driver, text, field):
        MoTasks.get_element(driver, field).send_keys(text)

    @staticmethod
    def send_keys_and_enter(driver, text, field):
        MoTasks.get_element(driver, field).send_keys(text)
        ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    @staticmethod
    def clear(driver, field):
        MoTasks.get_element(driver, field).clear()

    @staticmethod
    def select_an_option_in_the_combo(driver, combo, option):
        MoTasks.get_element(driver, combo).click()
        MoTasks.get_element(driver, option).click()

    @staticmethod
    def autocomplete(driver, text, autocomplete):
        MoTasks.get_element(driver, autocomplete).send_keys(text)
        MoTasks.get_element(driver, (By.XPATH, "//div[*/@autocomplete]/div/div/div/div")).click()

    @staticmethod
    def scroll(driver, scroll):
        if scroll == 'HOME':
            driver.swipe(start_x=318, start_y=614, end_x=318, end_y=2048, duration=100)
        elif scroll == 'END':
            driver.swipe(start_x=318, start_y=2048, end_x=318, end_y=614, duration=100)
        if scroll == 'UP':
            driver.swipe(start_x=720, start_y=768, end_x=720, end_y=1280, duration=150)
        elif scroll == 'DOWN':
            driver.swipe(start_x=720, start_y=1280, end_x=720, end_y=768, duration=150)
        elif scroll == 'LEFT':
            driver.swipe(start_x=29, start_y=1280, end_x=1152, end_y=1280, duration=100)
        elif scroll == 'RIGHT':
            driver.swipe(start_x=1411, start_y=1280, end_x=288, end_y=1280, duration=100)
        sleep(1)

    @staticmethod
    def click(driver, element):
        MoTasks.get_element(driver, element).click()
