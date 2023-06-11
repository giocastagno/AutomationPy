import allure
import pytest

from frontend.general.web_tasks import WebTasks
from frontend.general.web_validations import WebValidations
from frontend.pages.web_general_page import WebGeneralPage

pytestmark = [
    allure.parent_suite('FrontEnd'),
    allure.suite('Wikipedia'),
]


@pytest.mark.PBI("number PBI")
@pytest.mark.WEB
class TestEnterWikipediaWEB:

    @pytest.mark.SMOKE
    def test_enter_to_wikipedia(self, driverWEB):
        """
        Wikipedia - Enter to de page
        Validate ok
        """
        WebTasks().open_site(driverWEB, 'wikipedia')
        WebValidations.visualize(driverWEB, WebGeneralPage.elem('BUTTON', 'Bienvenidos'))
