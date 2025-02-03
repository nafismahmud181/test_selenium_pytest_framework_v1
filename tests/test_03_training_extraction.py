import time
from utils.logger import logger
from pages.login_page import LoginPage
from pages.navigation import NavigationToPages
from pages.timeline_open_close import TimelineOpenClose
from pages.training.training_download_json import TrainingJsonDownload
from pages.training.training_extraction_key import KeyExtractionTraining
from pages.training.training_extraction_table import TableExtractionTraining
from pages.training.training_linked_batch import LinkedBatchOpen
from pages.training.training_reset_definition import TrainingResetDefinition
from pages.training.training_search_batch import TrainingBatchSearch
from pages.training.training_zip_upload import TrainingZipUpload


def test_login(setup):
    driver = setup
    logger.info("Starting test: test_login")
    login_page = LoginPage(driver)
    login_page.login()

    navigate_profile_page = NavigationToPages(driver)
    navigate_profile_page.transaction_to_training()

    upload_zip = TrainingZipUpload(driver)
    upload_zip.zip_upload_part()

    Searching_transaction = TrainingBatchSearch(driver)
    Searching_transaction.batch_search_part()

    training_link_batch = LinkedBatchOpen(driver)
    training_link_batch.linked_batch_open_part()

    training_key_extraction = KeyExtractionTraining(driver)
    training_key_extraction.key_extraction_part()

    table_table_extraction = TableExtractionTraining(driver)
    table_table_extraction.table_extraction_part()

    timeline_open_download_jon = TimelineOpenClose(driver)
    timeline_open_download_jon.timeline_open()

    training_json_download = TrainingJsonDownload(driver)
    training_json_download.json_download_trans()

    timeline_close_download_jon = TimelineOpenClose(driver)
    timeline_close_download_jon.timeline_close()

    training_reset_definition = TrainingResetDefinition(driver)
    training_reset_definition.training_reset_definition()



    logger.info("Extraction process completed successfully.")
    time.sleep(10)