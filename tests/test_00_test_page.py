import time

from pages.add_documents_page import AddDocumentsPage
from pages.email_setting import EmailSettingClass
from pages.navigate_transaction_page import NavigateTransactionPage
from pages.notification_setting_page import NotificationSettingPage
from pages.radio_buttons_page import RadioButtonsPage
from pages.submit_panel_page import SubmitPanelPage
from utils.logger import logger
from pages.login_page import LoginPage
from pages.create_profile_name import CreateProfileName
from pages.navigate_create_profile_page import NavigateCreateProfilePage


def test_login(setup):
    driver = setup
    logger.info("Starting test: test_login")
    login_page = LoginPage(driver)
    login_page.login()

    Navigate_profile_page = NavigateCreateProfilePage(driver)
    Navigate_profile_page.access_navigate_create_profile_page()

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

    Navigate_transaction_page = NavigateTransactionPage(driver)
    Navigate_transaction_page.access_navigate_transaction_page()


    logger.info("Login test completed successfully.")
    time.sleep(10)
