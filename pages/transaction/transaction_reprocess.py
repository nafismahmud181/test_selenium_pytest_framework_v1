import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class ReprocessInTransaction:
    def __init__(self, driver):
        self.driver = driver

    def reprocess_part(self):
        try:
            reprocess_checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@class='custom-control custom-checkbox'])[2]"))
            )
            reprocess_checkbox.click()
            print("Reprocess checkbox clicked.")

            dropdown_reprocess = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//ul[@class='dropdown-menu']//li[2]"))
            )
            dropdown_reprocess.click()
            print("Dropdown option selected.")

            reprocess_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Re-Process')]"))
            )
            reprocess_button.click()
            print("Reprocess button clicked.")

        except Exception as e:
            logger.error(f"An error occurred while reprocessing a batch: {e}")
            raise