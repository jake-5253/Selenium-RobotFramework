import os
import sys
import unittest

from page_objects.ShopPageObjects import ShopPageObjects

sys.path.insert(0, './core/')
sys.path.insert(0, './page_objects/')
sys.path.insert(0, './config')

from page_objects.ContactPageObjects import *

common = CommonPageObjects()
shop = ShopPageObjects()

class ShopKeywords(unittest.TestCase):

    @classmethod
    def add_item_with_quantity(cls, item, quantity):
        shop.click_buy_for_item(item, quantity)
        shop.get_subtotal_price_of_item(item, quantity)
