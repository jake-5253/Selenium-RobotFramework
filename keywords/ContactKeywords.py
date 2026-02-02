import os
import sys
import unittest

sys.path.insert(0, './core/')
sys.path.insert(0, './page_objects/')
sys.path.insert(0, './config')

from page_objects.HomePageObjects import *
from page_objects.ContactPageObjects import *

handle = ElementHandler()
common = CommonPageObjects()
home_page = HomePageObjects()
contact = ContactPageObjects()

class ContactKeywords(unittest.TestCase):

    @classmethod
    def click_submit_button(cls):
        contact.click_submit_button()

    @classmethod
    def verify_validation_on_mandatory_fields(cls):
        contact.verify_invalid_forename()
        contact.verify_required_forename()
        contact.verify_invalid_email()
        contact.verify_required_email()
        contact.verify_invalid_message()
        contact.verify_required_message()

    @classmethod
    def verify_error_messages_for_required_fields_displayed(cls):
        contact.verify_error_message_displayed_forename("Forename is required")
        contact.verify_error_message_displayed_email("Email is required")
        contact.verify_error_message_displayed_message("Message is required")

    @classmethod
    def verify_error_messages_for_required_fields_not_displayed(cls):
        contact.verify_error_message_not_displayed_forename()
        contact.verify_error_message_not_displayed_email()
        contact.verify_error_message_not_displayed_message()

    @classmethod
    def fill_in_contact_form(cls, forename, surname, email, telephone, message):
        contact.enter_forename_textfield(forename)
        contact.enter_surname_textfield(surname)
        contact.enter_email_textfield(email)
        contact.enter_telephone_textfield(telephone)
        contact.enter_message_textarea(message)

    @classmethod
    def verify_successful_contact_submission_message_displayed(cls, message):
        common.wait_until_progress_bar_100()
        contact.verify_contact_submission_message(message)
        contact.verify_contact_submission_message('we appreciate your feedback.')