import time
import os
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class TransactionBatchSearch:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_batch_id():
        """Retrieve batch_ID from the JSON file."""
        try:
            logger.info("Attempting to retrieve batch ID from batch_id.json.")
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            batch_file_path = os.path.join(base_dir, "utils", "batch_id.json")

            with open(batch_file_path, "r") as batch_file:
                data = json.load(batch_file)
                batch_id = data.get("transaction_batch_ID")
                if batch_id:
                    logger.info(f"Successfully retrieved Batch ID: {batch_id}")
                else:
                    logger.warning("Batch ID is missing in the JSON file.")
                return batch_id

        except FileNotFoundError:
            logger.error("Batch ID file not found.")
            return None
        except Exception as e:
            logger.error(f"Error while retrieving Batch ID: {e}")
            return None

    @staticmethod
    def clear_batch_id():
        """Clear the batch_ID in the JSON file after use."""
        try:
            logger.info("Attempting to clear the batch ID in the batch_id.json file.")
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            batch_file_path = os.path.join(base_dir, "utils", "batch_id.json")

            with open(batch_file_path, "w") as batch_file:
                json.dump({"transaction_batch_ID": ""}, batch_file)

            logger.info("Batch ID has been cleared in batch_id.json.")

        except Exception as e:
            logger.error(f"Error while clearing Batch ID: {e}")

    def batch_search_part(self):
        try:
            batch_id = self.get_batch_id()  # Fetch the stored Batch ID

            if not batch_id:
                logger.error("Batch ID not found. Cannot proceed with search.")
                return

            logger.info(f"Waiting for form elements to load.")
            form_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "form-control"))
            )
            logger.info(f"Form elements found.")

            time.sleep(5)

            if form_elements:
                logger.info(f"Entering Batch ID: {batch_id} into the form.")
                form_elements[1].send_keys(batch_id)
                time.sleep(5)
                form_elements[1].send_keys(Keys.RETURN)
                logger.info(f"Batch ID entered and submitted successfully.")
                time.sleep(5)

                # Clear the batch ID after search
                logger.info(f"Clearing the Batch ID after search.")
                self.clear_batch_id()

        except Exception as e:
            logger.error(f"An error occurred while inputting batch ID: {e}")
            raise
