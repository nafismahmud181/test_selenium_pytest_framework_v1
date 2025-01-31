import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class TableExtractionTransaction:
    def __init__(self, driver):
        self.driver = driver

    def table_extraction_part(self):
        try:
            logger.info("Starting the table extraction test.")

            # Click the table view button
            logger.info("Locating and clicking the table view button.")
            time.sleep(10)
            table_view = self.driver.find_element(By.XPATH,
                                             "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[2]/*[name()='svg'][1]")
            table_view.click()

            time.sleep(5)

            # Scroll through the section
            logger.info("Scrolling the scrollable section.")
            scrollable_section = self.driver.find_element(By.XPATH,
                                                     "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]")
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 530;", scrollable_section)
            time.sleep(1)

            # Save the table pattern
            logger.info("Saving the table pattern.")
            save_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
            save_button.send_keys(Keys.TAB)
            model_box = self.driver.execute_script("return document.activeElement")
            model_box.send_keys("tablePattern")
            model_box.send_keys(Keys.RETURN)
            time.sleep(1)
            model_box.send_keys(Keys.TAB)
            set_pattern = self.driver.execute_script("return document.activeElement")
            set_pattern.send_keys(Keys.BACKSPACE)
            time.sleep(1)

            # Select and drag over the table
            logger.info("Selecting and dragging over the table area.")
            start_x, start_y = 144, 300
            end_x, end_y = 1140, 300
            actions = ActionChains(self.driver)
            actions.move_by_offset(start_x, start_y).perform()
            time.sleep(10)
            time.sleep(1)
            actions.key_down(Keys.SHIFT)
            for x in range(start_x, end_x, 40):
                actions.move_by_offset(40, 0).perform()
                time.sleep(0.1)
            actions.key_up(Keys.SHIFT)
            actions.click()
            actions.perform()
            time.sleep(1)

            save_button.send_keys(Keys.RETURN)
            time.sleep(3)

            # Test section
            logger.info("Navigating to the test section.")
            test_section = self.driver.find_element(By.XPATH, "//button[normalize-space()='6. Test']")
            test_section.send_keys(Keys.RETURN)
            time.sleep(3)

            # Test document
            logger.info("Testing the document.")
            test_document = self.driver.find_element(By.XPATH, "//button[normalize-space()='Test Document']")
            test_document.send_keys(Keys.RETURN)
            time.sleep(5)

        except Exception as e:
            logger.error(f"An error occurred while reprocessing a batch: {e}")
            raise