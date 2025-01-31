import os
import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class TransactionZipUpload:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Set explicit wait

    def zip_upload_part(self):
        try:
            logger.info("Clicking the 'Upload Transaction' button.")
            batch_upload_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Upload Transaction']"))
            )
            batch_upload_button.click()

            logger.info("Selecting the file for upload.")
            batch_upload_field = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".custom-file-input"))
            )

            # Dynamically get the ZIP file path
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get test_selenium_pytest_framework_v1 path
            file_path = os.path.join(base_dir, "utils", "ZIP", "20250130.00012.zip")
            batch_upload_field.send_keys(file_path)

            logger.info("Clicking the 'Upload' button.")
            batch_submit_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Upload']"))
            )
            batch_submit_button.click()

            time.sleep(10)

            logger.info("Waiting for the Batch ID to appear.")
            batch_ID = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div[3]/div[3]/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]/button")
                )
            ).text

            logger.info(f"Batch ID retrieved: {batch_ID}")

            # Save batch_ID to a JSON file
            batch_file_path = os.path.join(base_dir, "utils", "batch_id.json")
            with open(batch_file_path, "w") as batch_file:
                json.dump({"batch_ID": batch_ID}, batch_file)

            return batch_ID

            time.sleep(10)

        except Exception as e:
            logger.error(f"An error occurred while uploading the zip: {e}")
            raise
