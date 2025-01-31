import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class TransactionBatchSearch:
    def __init__(self, driver):
        self.driver = driver

    def batch_search_part(self):
        try:
            form_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "form-control"))
            )

            # time.sleep(3)
            self.driver.get("http://10.10.1.10/batch/20250130.100065")
            # if form_elements:
            #     form_elements[1].send_keys(" 20250130.00012 ")
            #     form_elements[1].send_keys(Keys.RETURN)
            #     time.sleep(5)
        except Exception as e:
            logger.error(f"An error occurred while inputting batch ID: {e}")
            raise