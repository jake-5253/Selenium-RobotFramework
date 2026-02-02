import os
import sys
import unittest
import xml.etree.ElementTree as ET
import datetime
import allure
import time
import platform
from allure_commons.types import AttachmentType
from allure_commons._allure import attach
from selenium import webdriver
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver import chrome, firefox, ie, safari
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from ElementHandler import *
from builtins import set

sys.path.insert(0, './config')

import config


class WebHandler(object):

    def setup(self):
        self.this = self
        global INSTANCE

        # define browser & environment
        browser = config.CONFIG_BROWSER

        # set environment variables, set default environment to UAT
        # if os.environ.get('TEST_ENVIRONMENT') is None:
        #     os.environ['TEST_ENVIRONMENT'] = 'UAT'
        # os.environ['TEST_USER'] = os.environ.get(os.environ.get('TEST_ENVIRONMENT') + '_TEST_USER')
        # os.environ['TEST_PASSWORD'] = os.environ.get(os.environ.get('TEST_ENVIRONMENT') + '_TEST_PASSWORD')
        # os.environ['TEST_FE_URL'] = os.environ.get(os.environ.get('TEST_ENVIRONMENT') + '_TEST_FE_URL')
        # os.environ['TEST_BE_URL'] = os.environ.get(os.environ.get('TEST_ENVIRONMENT') + '_TEST_BE_URL')

        # declare additional chrome options
        options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--incognito')
        options.add_argument('--hide-scrollbars')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--log-level=3')  # fatal
        options.add_argument('--window-size=1920,1080')
        options.add_experimental_option("detach", True)
        # initialize driver INSTANCE and capabilities
        if browser.lower() == 'ff' or browser.lower() == 'firefox':
            caps = DesiredCapabilities.FIREFOX
            if platform.system() == 'Windows':
                driver = webdriver.Firefox(executable_path='./resources/drivers/windows/geckodriver.exe')
            elif platform.system() == 'Linux':
                driver = webdriver.Firefox(executable_path='./resources/drivers/linux/geckodriver')
        elif browser.lower() == 'ie':
            # caps = DesiredCapabilities.INTERNETEXPLORER
            if platform.system() == 'Windows':
                driver = webdriver.Ie(executable_path='./resources/drivers/windows/IEDriverServer.exe')
            elif platform.system() == 'Linux':
                raise ValueError('Download Linux IEdriver')
        elif browser.lower() == 'chrome':
            caps = DesiredCapabilities.CHROME
            caps["pageLoadStrategy"] = "normal"
            if platform.system() == 'Windows':
                driver = webdriver.Chrome(options)
            elif platform.system() == 'Linux':
                driver = webdriver.Chrome(chrome_options=options)
        elif browser.lower() == 'opera':
            caps = DesiredCapabilities.OPERA
            if platform.system() == 'Windows':
                driver = webdriver.Opera(executable_path='./resources/drivers/windows/operadriver.exe')
            elif platform.system() == 'Linux':
                raise ValueError('Download Linux OperaDriver')
        elif browser.lower() == 'safari':
            caps = DesiredCapabilities.SAFARI
            if platform.system() == 'Windows':
                driver = webdriver.Safari(executable_path='./resources/drivers/windows/safaridriver.exe')
            elif platform.system() == 'Linux':
                raise ValueError('Download Linux SafariDriver')

        # start driver
        print('Opening on ' + browser.upper() + ' browser. Run started at: ' + str(datetime.datetime.now()))
        INSTANCE = driver
        return INSTANCE

    # close driver
    def teardown(self):
        self.this = self
        attach(INSTANCE.get_screenshot_as_png(), 'Screenshot', AttachmentType.PNG)
        print('Run completed at: ' + str(datetime.datetime.now()))
        if ElementHandler.flag_warning(self) == True:
            INSTANCE.stop_client()
            INSTANCE.close()
            raise ValueError('Test Failed: Check logged WARNINGS')
        else:
            INSTANCE.stop_client()
            INSTANCE.close()

    def refresh_page(self):
        self.this = self
        time.sleep(1)
        INSTANCE.refresh()

    def get_filename(self, path):
        temp = os.path.splitext(path)
        name = (os.path.basename(temp[0]))
        extension = (os.path.basename(temp[1]))
        return name + extension

    def get_test_tag(self):
        expected_tags = ['']
        actual_tags = BuiltIn().replace_variables('@{TEST_TAGS}')
        for a_tag in actual_tags:
            for e_tag in expected_tags:
                if a_tag in expected_tags:
                    if a_tag == e_tag:
                        return a_tag
                elif a_tag not in expected_tags:
                    raise ValueError('Use valid test tags')

    @staticmethod
    def scroll_to_bottom_page():
        INSTANCE.execute_script("window.scrollTo(0, document.body.scrollHeight);")
