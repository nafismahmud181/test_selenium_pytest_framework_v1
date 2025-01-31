import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class TransactionResetDefinition:
    def __init__(self, driver):
        self.driver = driver

    def transaction_reset_definition(self):
        try:
            model_select = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='1. Models']"))
            )
            model_select.click()
            save_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
            save_button.send_keys(Keys.TAB)
            model_box = self.driver.execute_script("return document.activeElement")
            model_box.send_keys("keysOnly")
            model_box.send_keys(Keys.RETURN)
            time.sleep(1)
            save_button.send_keys(Keys.RETURN)

            test_section = self.driver.find_element(By.XPATH, "//button[normalize-space()='6. Test']")
            test_section.send_keys(Keys.RETURN)
            time.sleep(3)

            # Test document
            logger.info("Testing the document.")
            test_document = self.driver.find_element(By.XPATH, "//button[normalize-space()='Test Document']")
            test_document.send_keys(Keys.RETURN)
            time.sleep(5)

            key_view = self.driver.find_element(By.XPATH,
                                                  "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/*[name()='svg'][1]")
            key_view.click()
            time.sleep(5)

            delete_button_1 = self.driver.find_element(By.XPATH,
                                                  "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[3]/div[1]/*[name()='svg'][2]")
            delete_button_1.click()
            time.sleep(1)

            delete_button_2 = self.driver.find_element(By.XPATH,
                                                  "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[3]/div[1]/*[name()='svg'][2]")
            delete_button_2.click()
            time.sleep(1)

            delete_button_3 = self.driver.find_element(By.XPATH,
                                                  "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[3]/div[1]/*[name()='svg'][2]")
            delete_button_3.click()
            time.sleep(1)

            key_save_button = self.driver.find_element(By.XPATH,
                                                  "//button[normalize-space()='Save']")
            key_save_button.click()
            time.sleep(4)

            key_save_button = self.driver.find_element(By.XPATH,
                                                              "//button[normalize-space()='Test Document']")
            key_save_button.click()
            time.sleep(10)





        except Exception as e:
            logger.error(f"An error occurred while opening timeline: {e}")
            raise
