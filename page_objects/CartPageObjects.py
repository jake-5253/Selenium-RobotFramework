import logging
import sys
from xml.etree.ElementTree import Element

from page_objects.CommonPageObjects import *
from core.DateUtility import *
from core.CommonUtility import *
from core.ElementHandler import ElementHandler
from core.JSONValidator import JSONValidator

sys.path.insert(0, './/core//')
sys.path.insert(0, './page_objects/')

date_util = DateUtility()
common = CommonPageObjects()


class CartPageObjects:

    @staticmethod
    def get_rows_cart_items():
        count = ElementHandler.get_size(
            "//tr[@ng-repeat='item in cart.items()']",
            "Cart Item in rows")
        return count

    @staticmethod
    def get_rows_cart_item_title(index: int):
        item_title = ElementHandler.get_text_by_index(
            "//tr[@ng-repeat='item in cart.items()']/td[1]",
            "Cart Item Title", index)
        return item_title

    @staticmethod
    def verify_subtotal_per_item(item: str, subtotal: float):
        for i in range(CartPageObjects.get_rows_cart_items()):
            if item in CartPageObjects.get_rows_cart_item_title(i):
                ElementHandler.verify_text_contains_by_index(
                    "//tr[@ng-repeat='item in cart.items()']/td[4]",
                    "Item Subtotal", str(subtotal), i)

    @staticmethod
    def verify_subtotal_equal_to_total(data: str):
        print(data)
        ElementHandler.verify_text_contains(
            "//strong[contains(@class, 'total')]",
            "Total Cart label", data)

