import time

from pages.create_profile.add_documents_page import AddDocumentsPage
from pages.create_profile.email_setting import EmailSettingClass
from pages.navigation import NavigationToPages
from pages.create_profile.notification_setting_page import NotificationSettingPage
from pages.create_profile.radio_buttons_page import RadioButtonsPage
from pages.create_profile.submit_panel_page import SubmitPanelPage
from utils.logger import logger
from pages.login_page import LoginPage
from pages.create_profile.create_profile_name import CreateProfileName


def test_login(setup):
    driver = setup
    logger.info("Starting test: test_login")
    login_page = LoginPage(driver)
    login_page.login()

    navigate_profile_page = NavigationToPages(driver)
    navigate_profile_page.transaction_to_create_profile()

    create_profile_name = CreateProfileName(driver)
    create_profile_name.fill_create_profile_form()

    radio_page = RadioButtonsPage(driver)
    radio_page.interact_with_radio_buttons()

    add_documents_page = AddDocumentsPage(driver)
    add_documents_page.add_documents()

    email_settings = EmailSettingClass(driver)
    email_settings.email_setting()

    notification_setting_page = NotificationSettingPage(driver)
    notification_setting_page.configure_notifications()

    submit_panel_page = SubmitPanelPage(driver)
    submit_panel_page.submit_form()

    navigate_transaction_page = NavigationToPages(driver)
    navigate_transaction_page.profile_to_transaction()

    logger.info("Successfully created our profile")
    time.sleep(10)
