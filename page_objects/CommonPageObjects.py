import sys

from core.DateUtility import *
from core.CommonUtility import *
from core.ElementHandler import ElementHandler

sys.path.insert(0, './/core//')
date_util = DateUtility()
common_util = CommonUtility()


class CommonPageObjects:

    @staticmethod
    def click_menu(data: str):
        ElementHandler.click(
            "//a[text()='" + data + "']",
            "Menu tab: " + data)

    @staticmethod
    def wait_until_progress_bar_100():
        ElementHandler.wait_until_element_visible(
            "//div[@class='progress progress-info wait']/div",
            "Progress Bar")
        ElementHandler.wait_until_attribute_contains_value(
            "//div[@class='progress progress-info wait']/div",
            "Progress Bar", "style", "100")

    @staticmethod
    def click_cart_link():
        ElementHandler.click(
            "//a[@href='#/cart']",
            "Cart link")