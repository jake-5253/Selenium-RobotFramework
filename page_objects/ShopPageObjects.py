from page_objects.CommonPageObjects import *
from core.DateUtility import *
from core.CommonUtility import *
from core.ElementHandler import ElementHandler

sys.path.insert(0, './/core//')
sys.path.insert(0, './page_objects/')

date_util = DateUtility()
common_util = CommonUtility()
common = CommonPageObjects()

textfield_forename: str = "//input[@id='forename']"
textfield_surname: str = "//input[@id='surname']"
textfield_email: str = "//input[@id='email']"
textfield_telephone: str = "//input[@id='telephone']"
textarea_message: str = "//textarea[@id='message']"
subtotal_dict = {}
subtotal_arr = []

class ShopPageObjects:

    @staticmethod
    def click_buy_button(index: int):
        ElementHandler.click_element_by_index(
            "//a[@ng-click='add(item)']",
            "Buy button", index)

    @staticmethod
    def get_all_items():
        item_size = ElementHandler.get_size(
            "//h4[contains(@class, 'product-title')]",
            "Item title size")
        return item_size

    @staticmethod
    def get_items_title(index):
        items_title = ElementHandler.get_text_by_index(
            "//h4[contains(@class, 'product-title')]",
            "Item title", index)
        return items_title

    @staticmethod
    def get_item_unit_price(index):
        items_unit_price = ElementHandler.get_text_by_index(
            "//span[contains(@class, 'product-price')]",
            "Item Unit Price", index)
        return float(items_unit_price.replace('$', ''))

    @staticmethod
    def click_buy_for_item(item, quantity):
        all_items = ShopPageObjects.get_all_items()
        for i in range(int(quantity)):
            for y in range(all_items):
                item_title = ShopPageObjects.get_items_title(y)
                if item == item_title:
                    ShopPageObjects.click_buy_button(y)

    @staticmethod
    def get_subtotal_price_of_item(item, quantity):
        all_items = ShopPageObjects.get_all_items()
        for y in range(all_items):
            item_title = ShopPageObjects.get_items_title(y)
            if item == item_title:
                unit_price = ShopPageObjects.get_item_unit_price(y)
                subtotal_price = unit_price * float(quantity)
                subtotal_dict.update({item: subtotal_price})
                subtotal_arr.append(float(subtotal_price))

    @staticmethod
    def get_subtotal_per_item():
        return subtotal_dict

    @staticmethod
    def get_subtotal_all_items():
        return subtotal_arr