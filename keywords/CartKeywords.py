import os
import sys
import unittest

sys.path.insert(0, './core/')
sys.path.insert(0, './page_objects/')
sys.path.insert(0, './config')

from page_objects.CartPageObjects import *
from page_objects.ShopPageObjects import *

cart = CartPageObjects()
shop = ShopPageObjects()

class CartKeywords(unittest.TestCase):

    @classmethod
    def verify_item_subtotals_per_item(cls, item):
        subtotal_per_item = shop.get_subtotal_per_item()
        cart.verify_subtotal_per_item(item, subtotal_per_item[item])

    @classmethod
    def verify_subtotal_equal_to_total(cls):
        subtotal_all_items = 0
        get_subtotal_all_items = shop.get_subtotal_all_items()
        for i in get_subtotal_all_items:
            subtotal_all_items = subtotal_all_items + i
        cart.verify_subtotal_equal_to_total(str(subtotal_all_items))


