import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # test_selenium_pytest_framework_v1
download_dir = os.path.join(base_dir, "utils")

class TansactionJsonDownload:
    def __init__(self, driver):
        self.driver = driver

    def json_download_trans(self):
        try:
            download_json = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "(//button[@type='button'][normalize-space()='Download Output JSON'])[1]"))
            )
            download_json.click()

            time.sleep(2)

        except Exception as e:
            logger.error(f"An error occurred while opening timeline: {e}")
            raise