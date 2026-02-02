import time

from page_objects.CommonPageObjects import *
from core.DateUtility import *
from core.CommonUtility import *
from core.ElementHandler import ElementHandler

sys.path.insert(0, './/core//')
sys.path.insert(0, './page_objects/')

date_util = DateUtility()
common_util = CommonUtility()
common = CommonPageObjects()

textfield_forename: tuple = ("//input[@id='forename']", "Forename textfield")
textfield_surname: tuple = ("//input[@id='surname']", "Surname textfield")
textfield_email: tuple = ("//input[@id='email']", "Email textfield")
textfield_telephone: tuple = ("//input[@id='telephone']", "Telephone textfield")
textarea_message: tuple = ("//textarea[@id='message']", "Message textarea")

class ContactPageObjects:

    @staticmethod
    def click_submit_button():
        time.sleep(1)
        ElementHandler.click(
            "//a[text()='Submit']",
            "Submit button")

    @staticmethod
    def verify_error_contains_messages(data: str):
        ElementHandler.verify_text_contains(
            "//div[contains(@class, 'error')]",
            "Error message: " + data, data)

    @staticmethod
    def verify_required_forename():
        ElementHandler.verify_attribute(
            textfield_forename[0],
            textfield_forename[1], "required", "true")

    @staticmethod
    def verify_invalid_forename():
        ElementHandler.verify_attribute_contains(
            textfield_forename[0],
            textfield_forename[1], "class", "invalid")

    @staticmethod
    def verify_required_email():
        ElementHandler.verify_attribute(
            textfield_email[0],
            textfield_email[1], "required", "true")

    @staticmethod
    def verify_invalid_email():
        ElementHandler.verify_attribute_contains(
            textfield_email[0],
            textfield_email[1], "class", "invalid")

    @staticmethod
    def verify_invalid_message():
        ElementHandler.verify_attribute(
            textarea_message[0],
            textarea_message[1],"required", "true")

    @staticmethod
    def verify_required_message():
        ElementHandler.verify_attribute_contains(
            textarea_message[0],
            textarea_message[1], "class", "invalid")

    @staticmethod
    def verify_error_message_displayed_forename(data):
        ElementHandler.verify_text(
            "//span[@id='forename-err']",
            "Forename Error Label", data)

    @staticmethod
    def verify_error_message_displayed_email(data):
        ElementHandler.verify_text(
            "//span[@id='email-err']",
            "Email Error Label", data)

    @staticmethod
    def verify_error_message_displayed_message(data):
        ElementHandler.verify_text(
            "//span[@id='message-err']",
            "Message Error Label", data)

    @staticmethod
    def verify_error_message_not_displayed_forename():
        ElementHandler.assert_element_not_visible(
            "//span[@id='forename-err']",
            "Forename Error Label")

    @staticmethod
    def verify_error_message_not_displayed_email():
        ElementHandler.assert_element_not_visible(
            "//span[@id='email-err']",
            "Email Error Label")

    @staticmethod
    def verify_error_message_not_displayed_message():
        ElementHandler.assert_element_not_visible(
            "//span[@id='message-err']",
            "Message Error Label")

    @staticmethod
    def enter_forename_textfield(data):
        ElementHandler.send_keys(
            textfield_forename[0],
            textfield_forename[1], data)

    @staticmethod
    def enter_surname_textfield(data):
        ElementHandler.send_keys(
            textfield_surname[0],
            textfield_surname[1], data)

    @staticmethod
    def enter_email_textfield(data):
        ElementHandler.send_keys(
            textfield_email[0],
            textfield_email[1], data)

    @staticmethod
    def enter_telephone_textfield(data):
        ElementHandler.send_keys(
            textfield_telephone[0],
            textfield_telephone[1], data)

    @staticmethod
    def enter_message_textarea(data):
        ElementHandler.send_keys(
            textarea_message[0],
            textarea_message[1], data)

    @staticmethod
    def verify_contact_submission_message(data):
        ElementHandler.verify_text_contains(
            "//div[@ui-if='contactValidSubmit']",
            "Contact Feedback message", data)

