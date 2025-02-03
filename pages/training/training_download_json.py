import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
download_dir = os.path.join(base_dir, "utils")

class TrainingJsonDownload:
    def __init__(self, driver):
        self.driver = driver

    def json_download_trans(self):
        try:
            logger.info("Attempting to click 'Download Output JSON' button...")
            download_json = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "(//button[@type='button'][normalize-space()='Download Output JSON'])[1]"))
            )
            download_json.click()
            logger.info("Download button clicked successfully.")
            time.sleep(2)

        except Exception as e:
            logger.error(f"An error occurred while downloading JSON: {e}")
            raise