import os
import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class TrainingZipUpload:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Set explicit wait

    def zip_upload_part(self):
        try:
            logger.info("Clicking the 'Upload Train Batch' button.")
            batch_upload_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Upload Train Batch']"))
            )
            batch_upload_button.click()

            logger.info("Selecting the file for upload.")
            batch_upload_field = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".custom-file-input"))
            )

            # Dynamically get the ZIP file path
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            file_path = os.path.join(base_dir, "utils", "ZIP", "Training_TN20250201.00001.zip")

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"ZIP file not found: {file_path}")

            batch_upload_field.send_keys(file_path)

            time.sleep(3)

            batch_submit_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Upload']"))
            )
            logger.info("File uploaded successfully.")
            batch_submit_button.click()
            time.sleep(10)


            logger.info("Waiting for the Batch ID to appear.")
            batch_ID = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div[3]/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]")
                )
            ).text

            logger.info(f"Batch ID retrieved: {batch_ID}")

            # Save batch_ID to a JSON file
            batch_file_path = os.path.join(base_dir, "utils", "batch_id.json")
            with open(batch_file_path, "w", encoding="utf-8") as batch_file:
                json.dump({"training_batch_ID": batch_ID}, batch_file, ensure_ascii=False, indent=4)

            return batch_ID

        except Exception as e:
            logger.exception("An error occurred while uploading the zip")
            raise
