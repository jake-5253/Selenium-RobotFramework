import os
import sys
import unittest

sys.path.insert(0, './core/')
sys.path.insert(0, './page_objects/')
sys.path.insert(0, './config')

from page_objects.CommonPageObjects import *
from page_objects.HomePageObjects import *

handle = ElementHandler()
common = CommonPageObjects()
home_page = HomePageObjects()


class CommonKeywords(unittest.TestCase):

    @classmethod
    def go_to_menu(cls, data):
        common.click_menu(data)

    @classmethod
    def go_to_jupiter_toys_home_page(cls):
        ''' Stored TEST_URL as environment variable but will keep url exposed for now'''
        # handle.go_to_page(os.environ.get('TEST_URL'))
        handle.go_to_page('https://jupiter.cloud.planittesting.com/')
        home_page.wait_for_start_shopping_button_displayed()

    @classmethod
    def go_to_cart(cls):
        common.click_cart_link()

