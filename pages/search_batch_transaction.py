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
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get test_selenium_pytest_framework_v1 path
            batch_file_path = os.path.join(base_dir, "utils", "batch_id.json")

            with open(batch_file_path, "r") as batch_file:
                data = json.load(batch_file)
                return data.get("batch_ID")

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
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get test_selenium_pytest_framework_v1 path
            batch_file_path = os.path.join(base_dir, "utils", "batch_id.json")

            with open(batch_file_path, "w") as batch_file:
                json.dump({"batch_ID": ""}, batch_file)

            logger.info("Batch ID has been cleared in batch_id.json.")

        except Exception as e:
            logger.error(f"Error while clearing Batch ID: {e}")

    def batch_search_part(self):
        try:
            batch_id = self.get_batch_id()  # Fetch the stored Batch ID

            if not batch_id:
                logger.error("Batch ID not found. Cannot proceed with search.")
                return

            form_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "form-control"))
            )

            if form_elements:
                logger.info(f"Entering Batch ID: {batch_id}")
                form_elements[1].send_keys(batch_id)
                form_elements[1].send_keys(Keys.RETURN)
                time.sleep(5)

                # Clear the batch ID after search
                self.clear_batch_id()

        except Exception as e:
            logger.error(f"An error occurred while inputting batch ID: {e}")
            raise
