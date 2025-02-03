import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class LinkedBatchOpen:
    def __init__(self, driver):
        self.driver = driver

    def linked_batch_open_part(self):
        try:
            logger.info("Waiting for the 'Expand' button to be visible.")
            expand = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//div[@class='d-inline'])[1]"))
            )
            logger.info("Expand button located. Clicking to expand.")
            expand.click()

            logger.info("Waiting for the 'Linked Batch' link to be visible.")
            linked_batch = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]"))
            )
            logger.info("Linked Batch link located. Clicking to open the linked batch.")
            linked_batch.click()

            logger.info("Waiting for the form control to load after opening the linked batch.")
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control"))
            )
            logger.info("Linked batch successfully opened. Waiting for 10 seconds.")
            time.sleep(10)
        except Exception as e:
            logger.error(f"An error occurred while opening linked batch: {e}")
            raise