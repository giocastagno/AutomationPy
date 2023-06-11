from selenium.webdriver.common.by import By


class WebGeneralPage:
    elements = {
        "OPTION": "//li[@role='option'][text()='{}']",
        "MENU": "//*[local-name() = 'span'][contains(@class,'menu-title')][text()='{}']",
        "BUTTON": "//*[local-name() = 'a' or local-name() = 'button'][text()='{}']",
        "BUTTON_CONT": "//*[local-name() = 'a' or local-name() = 'button'][contains(text(),'{}')]",
        "MODAL_BUTTON": "//div[contains(@class,'modal')]//button[contains(text(),'{}')]",
        "COMBO": "//div[label/span[text()='{}']]//span[@role='combobox']",
        "INPUT": "//div[label/span[text()='{}']]//input",
        "INPUT_VALUE": "//div[label/span[text()='{}']]/span",
        "INPUT_NAME": "//input[@name='{}']",
        "SWITCH": "//div[span[text()='{}']]/input[@type='checkbox']",
        "TEXTBOX": "//div[//text()='{}']//textarea",
        "CHECKBOX": "//div[contains(label/text(),'{}')]/input[@type='checkbox']",
        "TITLE": "//*[local-name() = 'h1' or local-name() = 'h2' or local-name() = 'h3'][text()='{}']",
        "SUBTITLE": "//*[local-name() = 'h4' or local-name() = 'h5' or local-name() = 'h6'][text()='{}']",
        "LABEL": "//*[local-name() = 'label'][text()='{}']",
        "TEXT_AREA": "//textarea[text()='{}']",
        "IMG": "//img[contains(@src, '{}')]",
        "FIELD_VAL": "//div[label/span[contains(text(),'{}')]]/span/div[contains(@class, 'invalid-feedback')]",
        "COLUM_NAME": "//table/thead/tr/th[text()='{}']",
        "ITEM": "//li/span[contains(@id, 'select2-list')][text()='{}']",
    }

    ancestors = [
        "@style='display: none;'",
        "@class='modal fade'"
    ]

    """
    Example
    [not(ancestor::*[@style='display: none;'] or ancestor::*[@class='modal fade'])]
    """
    @staticmethod
    def not_ancestors():
        not_ancestors = "[not("
        for a in WebGeneralPage.ancestors:
            if WebGeneralPage.ancestors.index(a) != 0:
                not_ancestors += " or "
            not_ancestors += f"ancestor::*[{a}]"
        not_ancestors += ")]"
        return not_ancestors

    @staticmethod
    def elem(element, param):
        elem = (By.XPATH, WebGeneralPage.elements.get(element).format(param) + WebGeneralPage.not_ancestors())
        return elem
