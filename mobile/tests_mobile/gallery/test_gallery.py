import allure
import pytest

from mobile.pages.Gallery.gallery import GalleryPage

pytestmark = [
    allure.parent_suite('Mobile'),
    allure.suite('Galery'),
]


@pytest.mark.PBI("number PBI")
@pytest.mark.MO
class TestGalery:

    @pytest.mark.SMOKE
    def test_visualize_elements(self, driverMO):
        """
        TC- Visualize all elements in login page
        """
        GalleryPage(driverMO).elements_gallery()
