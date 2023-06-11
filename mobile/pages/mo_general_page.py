class MoGeneralPage:
    elements = {
        "id": "elementId/{}",
        "modal-id": "android:id/{}",
        "text": "//*[@text='{}']",
        "resource-id": "//*[@resource-id='{}']",
    }

    @staticmethod
    def elem(by, param):
        elem = ''
        if by == "text" or by == "resource-id":
            elem = ("xpath", MoGeneralPage.elements.get(by).format(param))
        elif by == "id" or by == "modal-id":
            elem = ("id", MoGeneralPage.elements.get(by).format(param))
        return elem
