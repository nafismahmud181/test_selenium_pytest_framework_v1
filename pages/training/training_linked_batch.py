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
            expand = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//div[@class='d-inline'])[1]"))
            )
            expand.click()

            linked_batch = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/a[1]"))
            )
            linked_batch.click()

            logger.info("Waiting for the form control to be visible.")

            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control"))
            )
            time.sleep(10)
        except Exception as e:
            logger.error(f"An error occurred while opening linked batch: {e}")
            raise