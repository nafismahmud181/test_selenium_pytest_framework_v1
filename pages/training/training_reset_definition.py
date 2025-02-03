import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class TrainingResetDefinition:
    def __init__(self, driver):
        self.driver = driver

    def training_reset_definition(self):
        try:
            logger.info("Waiting for 'Models' button to be clickable.")
            model_select = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='1. Models']"))
            )
            logger.info("Clicking on 'Models' button.")
            model_select.click()

            logger.info("Locating 'Save' button and navigating to model selection field.")
            save_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
            save_button.send_keys(Keys.TAB)

            logger.info("Selecting 'keysOnly' model.")
            model_box = self.driver.execute_script("return document.activeElement")
            model_box.send_keys("keysOnly")
            model_box.send_keys(Keys.RETURN)
            time.sleep(1)

            logger.info("Saving the selected model.")
            save_button.send_keys(Keys.RETURN)

            logger.info("Navigating to 'Test' section.")
            test_section = self.driver.find_element(By.XPATH, "//button[normalize-space()='6. Test']")
            test_section.send_keys(Keys.RETURN)
            time.sleep(3)

            logger.info("Testing the document.")
            test_document = self.driver.find_element(By.XPATH, "//button[normalize-space()='Test Document']")
            test_document.send_keys(Keys.RETURN)
            time.sleep(5)

            logger.info("Opening key view.")
            key_view = self.driver.find_element(By.XPATH,
                "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/*[name()='svg'][1]"
            )
            key_view.click()
            time.sleep(5)

            logger.info("Deleting key elements.")
            delete_buttons = [
                "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[3]/div[1]/*[name()='svg'][2]",
                "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[3]/div[1]/*[name()='svg'][2]",
                "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[3]/div[1]/*[name()='svg'][2]"
            ]

            for idx, delete_button_xpath in enumerate(delete_buttons, start=1):
                logger.info(f"Clicking delete button {idx}.")
                delete_button = self.driver.find_element(By.XPATH, delete_button_xpath)
                delete_button.click()
                time.sleep(1)

            logger.info("Saving key modifications.")
            key_save_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
            key_save_button.click()
            time.sleep(4)

            logger.info("Re-testing the document after deletion.")
            test_document_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Test Document']")
            test_document_button.click()
            time.sleep(5)

            logger.info("Training reset definition process completed successfully.")

        except Exception as e:
            logger.error(f"An error occurred while resetting the training definition: {e}", exc_info=True)
            raise
