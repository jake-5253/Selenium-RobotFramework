from page_objects.CommonPageObjects import *
from core.ElementHandler import ElementHandler

sys.path.insert(0, './/core//')
sys.path.insert(0, './page_objects/')


class HomePageObjects:

    @staticmethod
    def wait_for_start_shopping_button_displayed():
        ElementHandler.wait_until_element_visible(
            "//a[@href='#/shop'][text()='Start Shopping »']",
            "Start Shopping button")
