import time


from utils.logger import logger
from pages.login_page import LoginPage
from pages.timeline_open_close import TimelineOpenClose
from pages.transaction.transaction_search_batch import TransactionBatchSearch
from pages.transaction.transaction_download_json import TransactionJsonDownload
from pages.transaction.transaction_extraction_key import KeyExtractionTransaction
from pages.transaction.transaction_extraction_table import TableExtractionTransaction
from pages.transaction.transaction_linked_batch import LinkedBatchOpen
from pages.transaction.transaction_reset_definition import TransactionResetDefinition
from pages.transaction.transaction_zip_upload import TransactionZipUpload


def test_login(setup):
    driver = setup
    logger.info("Starting test: test_login")
    login_page = LoginPage(driver)
    login_page.login()


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

    transaction_json_download = TransactionJsonDownload(driver)
    transaction_json_download.json_download_trans()

    timeline_close_download_jon = TimelineOpenClose(driver)
    timeline_close_download_jon.timeline_close()

    transaction_reset_definition = TransactionResetDefinition(driver)
    transaction_reset_definition.transaction_reset_definition()


    logger.info("Extraction process completed successfully.")
    time.sleep(10)