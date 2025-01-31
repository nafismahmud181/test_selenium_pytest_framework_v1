import time

from pages.add_documents_page import AddDocumentsPage
from pages.email_setting import EmailSettingClass
from pages.navigate_transaction_page import NavigateTransactionPage
from pages.notification_setting_page import NotificationSettingPage
from pages.radio_buttons_page import RadioButtonsPage
from pages.search_batch_transaction import TransactionBatchSearch
from pages.submit_panel_page import SubmitPanelPage
from pages.timeline_open_close import TimelineOpenClose
from pages.transaction_download_json import TansactionJsonDownload
from pages.transaction_extraction_key import KeyExtractionTransaction
from pages.transaction_extraction_table import TableExtractionTransaction
from pages.transaction_linked_batch import LinkedBatchOpen
from pages.transaction_reset_definition import TransactionResetDefinition
from pages.transaction_zip_upload import TransactionZipUpload
from utils.logger import logger
from pages.login_page import LoginPage
from pages.create_profile_name import CreateProfileName
from pages.navigate_create_profile_page import NavigateCreateProfilePage


def test_login(setup):
    driver = setup
    logger.info("Starting test: test_login")
    login_page = LoginPage(driver)
    login_page.login()

    # Navigate_profile_page = NavigateCreateProfilePage(driver)
    # Navigate_profile_page.access_navigate_create_profile_page()
    #
    # create_profile_name = CreateProfileName(driver)
    # create_profile_name.fill_create_profile_form()
    #
    # radio_page = RadioButtonsPage(driver)
    # radio_page.interact_with_radio_buttons()
    #
    # add_documents_page = AddDocumentsPage(driver)
    # add_documents_page.add_documents()
    #
    # email_settings = EmailSettingClass(driver)
    # email_settings.email_setting()
    #
    # notification_setting_page = NotificationSettingPage(driver)
    # notification_setting_page.configure_notifications()
    #
    # submit_panel_page = SubmitPanelPage(driver)
    # submit_panel_page.submit_form()
    #
    # Navigate_transaction_page = NavigateTransactionPage(driver)
    # Navigate_transaction_page.access_navigate_transaction_page()
    #

    upload_zip = TransactionZipUpload(driver)
    upload_zip.zip_upload_part()

    Searching_transaction = TransactionBatchSearch(driver)
    Searching_transaction.batch_search_part()

    Transaction_link_batch = LinkedBatchOpen(driver)
    Transaction_link_batch.linked_batch_open_part()
    #
    Transaction_key_extraction = KeyExtractionTransaction(driver)
    Transaction_key_extraction.key_extraction_part()

    Transaction_table_extraction = TableExtractionTransaction(driver)
    Transaction_table_extraction.table_extraction_part()

    timeline_open_download_jon = TimelineOpenClose(driver)
    timeline_open_download_jon.timeline_open()

    transaction_json_download = TansactionJsonDownload(driver)
    transaction_json_download.json_download_trans()

    timeline_close_download_jon = TimelineOpenClose(driver)
    timeline_close_download_jon.timeline_close()

    transaction_reset_definition = TransactionResetDefinition(driver)
    transaction_reset_definition.transaction_reset_definition()

    logger.info("Login test completed successfully.")
    time.sleep(10)
