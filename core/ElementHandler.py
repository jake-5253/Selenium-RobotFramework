import logging
import time
import re

import WebHandler
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException, \
    StaleElementReferenceException, ElementNotVisibleException, WebDriverException, ElementNotInteractableException, \
    ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from robot.api import logger

class ElementHandler(object):

    def warning_switch(self):
        global HAS_RUN
        HAS_RUN = True
        global CHECK_RUN
        CHECK_RUN = HAS_RUN

    def flag_warning(self):
        try:
            if CHECK_RUN:
                return CHECK_RUN
        except NameError:
            pass

    def find_element(locator, name):
        element = None
        try:
            for i in range(3):
                element = wait(WebHandler.INSTANCE, 10).until(
                    EC.visibility_of_element_located((By.XPATH, locator)))
                if element is not None:
                    return element
        except (StaleElementReferenceException, ElementNotInteractableException):
            for i in range(3):
                element = wait(WebHandler.INSTANCE, 10).until(
                    EC.visibility_of_element_located((By.XPATH, locator)))
                if element is not None:
                    return element
                else:
                    b_64 = WebHandler.INSTANCE.get_screenshot_as_base64()
                    logger.info(f'<img width="500" src="data:image/png;base64, {b_64}" alt="Red dot"/>', html=True)
                    attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
                    raise ValueError(name + ' is missing')
        except TimeoutException:
            b_64 = WebHandler.INSTANCE.get_screenshot_as_base64()
            logger.info(f'<img width="500" src="data:image/png;base64, {b_64}" alt="Red dot"/>', html=True)
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError(name + ' is missing')

    def find_elements(locator, name):
        elements = []
        try:
            for i in range(3):
                elements = wait(WebHandler.INSTANCE, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, locator)))
        except TimeoutException:
            raise ValueError(name + ' is missing')
        return elements

    @staticmethod
    def click_element_by_index(locator, name, index):
        elements = ElementHandler.find_elements(locator, name)
        try:
            elements[int(index)].click()
            logging.info('Clicked ' + name + ' with index: ' + str(index))
        except StaleElementReferenceException and ElementClickInterceptedException:
            ElementHandler.click_element_by_index(locator, name, index)

    def find_element_presence(locator, name):
        element = None
        try:
            for i in range(3):
                element = wait(WebHandler.INSTANCE, 3).until(
                    EC.presence_of_element_located((By.XPATH, locator)))
                return element
        except TimeoutException:
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError(name + ' is not present')

    def find_element_clickable(locator, name):
        element = None
        try:
            for i in range(3):
                element = wait(WebHandler.INSTANCE, 3).until(
                    EC.element_to_be_clickable((By.XPATH, locator)))
                if element is not None:
                    return element
        except (StaleElementReferenceException, ElementNotInteractableException):
            for i in range(3):
                element = wait(WebHandler.INSTANCE, 3).until(
                    EC.visibility_of_element_located((By.XPATH, locator)))
                if element is not None:
                    return element
                else:
                    attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
                    raise ValueError(name + ' is missing')
        except TimeoutException:
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError(name + ' is missing')

    @staticmethod
    def get_size(locator, name):
        count = 0
        elements = []
        try:
            for i in range(3):
                elements = wait(WebHandler.INSTANCE, 3).until(
                    EC.presence_of_all_elements_located((By.XPATH, locator)))
                count = elements.__len__()
        except TimeoutException:
            pass
        return count

    @staticmethod
    def click(locator, name):
        try:
            element = ElementHandler.find_element(locator, name)
            element.click()
            logging.info('Clicked ' + name)
        except StaleElementReferenceException and ElementClickInterceptedException:
            ElementHandler.click(locator, name)

    def double_click(locator, name):
        for i in range(3):
            try:
                action = ActionChains(WebHandler.INSTANCE)
                element = ElementHandler.find_element(locator, name)
                action.double_click(element).perform()
                logging.info('Double-clicked ' + name)
                break
            except StaleElementReferenceException:
                ElementHandler.double_click(locator, name)
                if i == 2:
                    attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
                    raise ValueError('Loop Ended. ' + name + 'not found.')

    @staticmethod
    def send_keys(locator, name, data):
        element = ElementHandler.find_element(locator, name)
        element.send_keys(data)
        logging.info('Entered ' + data + ' to ' + name)

    def enter_username_email(locator, name, data):
        element = ElementHandler.find_element(locator, name)
        element.send_keys(data)
        logging.info('Entered username/email on ' + name)

    def enter_user_password(locator, name, data):
        element = ElementHandler.find_element(locator, name)
        element.send_keys(data)
        logging.info('Entered password on ' + name)

    def send_keys_by_index(locator, name, data, index):
        elements = ElementHandler.find_elements(locator, name)
        try:
            elements[int(index)].send_keys(data)
            logging.info('Entered ' + data + ' with index ' + str(index) + ' to ' + name)
        except StaleElementReferenceException:
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError('Loop Ended. ' + name + 'not found.')

    def clear(locator, name):
        element = ElementHandler.find_element(locator, name)
        element.clear()

    def select_by_text(locator, name, text):
        element = ElementHandler.find_element(locator, name)
        select = Select(element)
        select.select_by_visible_text(text)
        logging.info('Selected ' + text + ' on ' + name)

    def select_by_value(locator, name, value):
        element = ElementHandler.find_element(locator, name)
        select = Select(element)
        select.select_by_value(value)
        logging.info('Selected ' + value + ' on ' + name)

    def select_by_index(locator, name, index):
        element = ElementHandler.find_element(locator, name)
        select = Select(element)
        select.select_by_index(index)
        logging.info('Selected ' + str(index) + ' on ' + name)

    def get_text(locator, name):
        for i in range(3):
            try:
                element = ElementHandler.find_element(locator, name)
                get_text = element.text
                return get_text
            except StaleElementReferenceException:
                ElementHandler.get_text(locator, name)
                if i == 2:
                    attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
                    raise ValueError('Loop Ended. ' + name + 'not found.')

    @staticmethod
    def get_text_by_index(locator, name, index):
        elements = ElementHandler.find_elements(locator, name)
        try:
            get_text = elements[int(index)].text
            return get_text
        except StaleElementReferenceException:
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError('Loop Ended. ' + name + 'not found.')

    def get_attribute(locator, name, attribute):
        element = ElementHandler.find_element(locator, name)
        get_attribute = element.get_attribute(attribute)
        return get_attribute

    def tick(select_check, locator, name):
        if select_check != 'none':
            try:
                element_selected = wait(WebHandler.INSTANCE, 1).until(
                    EC.visibility_of_element_located((By.XPATH, select_check)))
                if element_selected.is_displayed():
                    logging.info('Already ticked ' + name)
            except TimeoutException:
                element = ElementHandler.find_element(locator, name)
                element.click()
                logging.info('Ticked ' + name)
        else:
            element = ElementHandler.find_element(locator, name)
            if element.is_selected():
                logging.info('Already ticked ' + name)
            else:
                element.click()
                logging.info('Ticked ' + name)

    def verify_url(text):
        try:
            wait(WebHandler.INSTANCE, 5).until(
                EC.url_contains(text))
            logging.info('Current URL verified to contain: ' + text)
        except TimeoutException:
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError('Current URL does not contain: ' + text)


    @staticmethod
    def verify_attribute(locator, name, att, value):
        element = ElementHandler.find_element(locator, name)
        try:
            get_attribute = element.get_attribute(att)
            assert get_attribute == value
            logging.info('Correct expected attribute(' + att + '=' + value + ') on: ' + name)
        except AssertionError:
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError('Incorrect expected attribute on: ' + name)


    @staticmethod
    def verify_attribute_contains(locator, name, att, value):
        element = ElementHandler.find_element(locator, name)
        try:
            get_attribute = element.get_attribute(att)
            assert value in get_attribute
            logging.info('Correct expected attribute(' + att + 'contains' + value + ') on: ' + name)
        except AssertionError:
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError('Incorrect expected attribute on: ' + name)


    @staticmethod
    def verify_text(locator, name, text):
        element = ElementHandler.find_element(locator, name)
        try:
            get_text = element.text
            pattern = re.compile(re.escape(get_text), re.IGNORECASE)
            assert pattern.match(text)
            logging.info('Correct expected text (' + text + ') on: ' + name)
        except AssertionError:
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError('Incorrect expected text (' + text + ') on: ' + name)


    @staticmethod
    def verify_element_has_no_text(locator, name, text):
        element = ElementHandler.find_element(locator, name)
        try:
            get_text = element.text
            pattern = re.compile(re.escape(get_text), re.IGNORECASE)
            assert not pattern.match(text)
            logging.info('Expected element ' + name + ' verified has no (' + text + ')')
        except AssertionError:
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError('Incorrect expected text (' + text + ') on: ' + name)


    @staticmethod
    def verify_page_contains(locator, name, data_list):
        element = ElementHandler.find_element(locator, name)
        try:
            wait(WebHandler.INSTANCE, 5).until(
                EC.text_to_be_present_in_element((By.XPATH, locator), ' '))
            get_text = element.text
            for data in data_list:
                if data is None:
                    continue
                elif data in get_text:
                    logging.info('Correct expected text (' + data + ') on: ' + name)
                else:
                    logging.warning('Incorrect expected text (' + data + ') on: ' + name)
                    ElementHandler.warning_switch()
                    attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
        except TimeoutException:
            logging.info(name + ' is verified non-existent')
            assert not element.is_displayed()

    def verify_title(title):
        try:
            wait(WebHandler.INSTANCE, 5).until(
                EC.title_is(title))
            logging.info('Correct expected page title: ' + title)
        except TimeoutException:
            current_title = WebHandler.INSTANCE.title
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError('Incorrect expected page title: ' + current_title)

    def assert_element_visible(locator, name):
        for i in range(3):
            try:
                element = ElementHandler.find_element(locator, name)
                assert element.is_displayed()
                logging.info(name + ' is verified visible')
                break
            except StaleElementReferenceException:
                ElementHandler.assert_element_visible(locator, name)
                if i == 2:
                    attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
                    raise ValueError('Loop Ended. ' + name + 'not found.')

    def is_element_visible(locator, name):
        try:
            element = ElementHandler.find_element(locator, name)
            return element.is_displayed()
        except ValueError:
            logging.info(name + ' is not displayed')
            return False

    @staticmethod
    def assert_element_not_visible(locator, name):
        try:
            ElementHandler.find_element(locator, name)
        except ValueError:
            logging.info(name + ' is verified non-existent')

    def assert_text_equals(expected, actual, name):
        logging.info("EXPECTED SET OF DATA IN: " + name + '\n' + expected)
        logging.info("ACTUAL SET OF DATA IN: " + name + '\n' + actual)
        if expected == actual:
            logging.info('Equal texts verified')
        else:
            logging.warning("Set of data in " + name + " not equal")
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)

    def move_to_element(locator, name):
        action = ActionChains(WebHandler.INSTANCE);
        element = ElementHandler.find_element(locator, name)
        action.move_to_element(element).perform();
        logging.info('Mouse over on ' + name)

    def loop_until_sub_menu_selected(menu, menu_name, sub_menu, sub_menu_name):
        cur_url = WebHandler.INSTANCE.current_url
        get_menu = menu
        get_menu_name = menu_name
        get_sub_menu = sub_menu
        get_sub_menu_name = sub_menu_name
        action = ActionChains(WebHandler.INSTANCE)
        menu = ElementHandler.find_element(get_menu, get_menu_name)
        try:
            action.move_to_element(menu).perform()
            element = wait(WebHandler.INSTANCE, 4).until(
                EC.element_to_be_clickable((By.XPATH, sub_menu)))
            if element is not None and element.is_displayed():
                ElementHandler.click(get_sub_menu, get_sub_menu_name)
                new_url = WebHandler.INSTANCE.current_url
                if cur_url == new_url:
                    ElementHandler.loop_until_sub_menu_selected(get_menu, get_menu_name, get_sub_menu,
                                                                get_sub_menu_name)
                else:
                    logging.info("Navigated to " + get_sub_menu_name)
            else:
                ElementHandler.loop_until_sub_menu_selected(get_menu, get_menu_name, get_sub_menu, get_sub_menu_name)
        except (TimeoutException, ElementNotVisibleException, WebDriverException):
            ElementHandler.loop_until_sub_menu_selected(get_menu, get_menu_name, get_sub_menu, get_sub_menu_name)

    def upload_file(locator, name, file_path):
        element = ElementHandler.find_element_presence(locator, name)
        element.send_keys(file_path)
        logging.info('File Uploaded: ' + file_path)


    def go_to_page(self, site):
        WebHandler.INSTANCE.get(site)

    def switch_to_new_opened_window(self):
        try:
            wait(WebHandler.INSTANCE, 10).until(
                EC.number_of_windows_to_be(2))
            windows = WebHandler.INSTANCE.window_handles
            WebHandler.INSTANCE.switch_to.window(windows[1])
            wait(WebHandler.INSTANCE, 5).until(
                EC.text_to_be_present_in_element((By.XPATH, '//body'), ' '))
        except TimeoutException:
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError('Expected new window was not opened')

    def close_window_and_switch_handle(self):
        WebHandler.INSTANCE.close()
        windows = WebHandler.INSTANCE.window_handles
        WebHandler.INSTANCE.switch_to.window(windows[0])

    @staticmethod
    def wait_until_attribute_contains_value(locator, name, attribute, value):
        element = ElementHandler.find_element(locator, name)
        loop_check = True
        while loop_check:
            get_attribute = element.get_attribute(attribute)
            attribute_in_float = float(get_attribute[6:].replace('%;', ''))
            print(attribute_in_float)
            if value in get_attribute:
                loop_check = False
                logging.info(name + " found to have an attribute of " + attribute + " with value " + value)
            elif attribute_in_float > float(value):
                loop_check = False
                logging.info(name + " found to have an attribute of " + attribute + " with value " + value)


    @staticmethod
    def wait_until_element_visible(locator, name):
        for i in range(3):
            try:
                wait(WebHandler.INSTANCE, 20).until(
                    EC.visibility_of_element_located((By.XPATH, locator)))
                break
            except TimeoutException:
                attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
                raise ValueError(name + ' was not visible')

    def wait_until_element_invisible(locator, name):
        for i in range(5):
            try:
                wait(WebHandler.INSTANCE, 40).until_not(
                    EC.visibility_of_element_located((By.XPATH, locator)))
                break
            except TimeoutException:
                attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
                raise ValueError(name + ' remained visible')

    def loop_until_element_can_be_selected(locator, name, refresh_button, refresh_button_name):
        for i in range(40):
            try:
                element = wait(WebHandler.INSTANCE, 2).until(
                    EC.visibility_of_element_located((By.XPATH, locator)))
                if element.is_displayed():
                    ElementHandler.double_click(locator, name)
                    break
            except (TimeoutException, StaleElementReferenceException):
                ElementHandler.click(refresh_button, refresh_button_name)
                if i == 39:
                    attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
                    raise ValueError('Loop Ended. Transaction not found.')

    def loop_until_action_reviewed(locator, name, action_button, action_button_name):
        try:
            for i in range(10):
                element = wait(WebHandler.INSTANCE, 1).until(
                    EC.visibility_of_element_located((By.XPATH, locator)))
                if element.is_displayed():
                    ElementHandler.click(locator, name)
                    ElementHandler.click(action_button, action_button_name)
        except (TimeoutException, StaleElementReferenceException):
            logging.info('All Action Items Reviewed')

    def loop_until_element_displayed(locator, name, refresh_button, refresh_button_name):
        for i in range(40):
            try:
                element = wait(WebHandler.INSTANCE, 2).until(
                    EC.visibility_of_element_located((By.XPATH, locator)))
                if element.is_displayed():
                    break
            except (TimeoutException, StaleElementReferenceException):
                ElementHandler.click(refresh_button, refresh_button_name)
                if i == 39:
                    attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
                    raise ValueError('Loop Ended. Transaction not found.')

    @staticmethod
    def verify_text_contains(locator, name, data):
        element = ElementHandler.find_element(locator, name)
        try:
            get_text = element.text
            if data in get_text:
                logging.info('Verified contains text (' + data + ') on: ' + name)
            else:
                logging.warning('Expected text (' + data + ') was not found on element ' + name + ' with text (' + get_text + ')')
                attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
        except TimeoutException:
            logging.info(name + ' is verified non-existent')
            assert not element.is_displayed()

    @staticmethod
    def verify_text_contains_by_index(locator, name, data, index):
        elements = ElementHandler.find_elements(locator, name)
        try:
            get_text = elements[int(index)].text
            if data in get_text:
                logging.info('Verified contains text (' + data + ') on: ' + name)
            else:
                logging.warning(
                    'Expected text (' + data + ') was not found on element ' + name + ' with text (' + get_text + ')')
                attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
        except StaleElementReferenceException:
            attach(WebHandler.INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
            raise ValueError('Loop Ended. ' + name + 'not found.')

    def is_text_contains(locator, name, data):
        element = ElementHandler.find_element(locator, name)
        try:
            wait(WebHandler.INSTANCE, 5).until(
                EC.text_to_be_present_in_element((By.XPATH, locator), ' '))
            get_text = element.text
            if data in get_text:
                return True
            else:
                return False
        except TimeoutException:
            logging.info(name + ' is verified non-existent')
            assert not element.is_displayed()

    def scroll_into_view_until_last_count(locator, name, expected_count):
        for i in range(expected_count):
            element_count = ElementHandler.get_size(locator, name)
            elements = ElementHandler.find_elements(locator, name)
            print(element_count)
            if element_count <= expected_count:
                try:
                    WebHandler.INSTANCE.execute_script("arguments[0].scrollIntoView();", elements[i * 1])
                    time.sleep(1)
                except IndexError:
                    WebHandler.INSTANCE.execute_script("arguments[0].scrollIntoView();", elements[element_count])
                    time.sleep(2)
            else:
                break

    def scroll_into_view_target_element(locator, name):
        element = ElementHandler.find_element(locator, name)
        WebHandler.INSTANCE.execute_script("arguments[0].scrollIntoView();", element)
        logging.info('Scrolled into view ' + name)


