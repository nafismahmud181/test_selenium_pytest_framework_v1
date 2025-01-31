import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class KeyExtractionTransaction:
    def __init__(self, driver):
        self.driver = driver

    def key_extraction_part(self):
        try:
            add_keys = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control"))
            )

            time.sleep(5)
            logger.info("Filling the form with initial data.")
            add_keys.send_keys("3")
            add_keys.send_keys(Keys.RETURN)
            time.sleep(3)
            add_keys.send_keys(Keys.TAB)

            save_button = self.driver.execute_script("return document.activeElement")
            save_button.send_keys(Keys.TAB)

            test_batch = self.driver.execute_script("return document.activeElement")
            test_batch.send_keys(Keys.TAB)

            test_document = self.driver.execute_script("return document.activeElement")
            test_document.send_keys(Keys.TAB)

            more = self.driver.execute_script("return document.activeElement")
            more.send_keys(Keys.TAB)

            keyfieldName = self.driver.execute_script("return document.activeElement")
            time.sleep(2)

            # Define the key data to be processed
            key_data = [
                {"key_field_name": "assembly", "type": "static", "label": "ab"},
                {"key_field_name": "country code", "type": "static", "label": "BD"},
                {"key_field_name": "consignee city", "type": "selector"}
            ]

            # Process each key field in the data
            for keyItem in key_data:
                logger.info(f"Processing key field: {keyItem['key_field_name']}")
                keyfieldName.send_keys(keyItem['key_field_name'])
                keyfieldName.send_keys(Keys.RETURN)
                time.sleep(1)
                keyfieldName.send_keys(Keys.TAB)

                types = self.driver.execute_script("return document.activeElement")
                types.send_keys(keyItem['type'])
                types.send_keys(Keys.RETURN)
                time.sleep(1)
                types.send_keys(Keys.TAB)

                if keyItem['type'] == "selector":
                    logger.info(f"Handling selector for key field: {keyItem['key_field_name']}")
                    # Click the selector icon to open the selector
                    selector_icon_open = self.driver.find_element(By.XPATH,
                                                             "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[7]/*[name()='svg'][1]")
                    selector_icon_open.click()

                    # Use ActionChains to simulate dragging
                    actions = ActionChains(self.driver)
                    start_x, start_y = 560, 225
                    end_x, end_y = 680, 300
                    actions.move_by_offset(start_x, start_y).click_and_hold().move_by_offset(end_x - start_x,
                                                                                             end_y - start_y).release().perform()
                    actions.reset_actions()

                    time.sleep(2)
                    capture_icon = self.driver.find_element(By.XPATH,
                                                       "(//*[name()='svg'][@title='Capture'])[1]")
                    capture_icon.click()

                    # Close the selector icon
                    selector_icon_close = self.driver.find_element(By.XPATH,
                                                              "/html[1]/body[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[7]/*[name()='svg'][1]")
                    selector_icon_close.click()
                else:
                    logger.info(f"Entering label data for key field: {keyItem['key_field_name']}")
                    label = self.driver.execute_script("return document.activeElement")
                    if 'label' in keyItem:
                        label.send_keys(keyItem['label'])
                    label.send_keys(Keys.RETURN)
                    time.sleep(1)
                    label.send_keys(Keys.TAB)

                keyfieldName = self.driver.execute_script("return document.activeElement")

            # Submit the form
            logger.info("Submitting the form.")
            save_button.send_keys(Keys.RETURN)
            time.sleep(5)

            # Interact with the document
            logger.info("Interacting with the document.")
            test_document.send_keys(Keys.RETURN)
            time.sleep(5)

            logger.info("Form submission test completed successfully.")

        except Exception as e:
            logger.error(f"An error occurred while reprocessing a batch: {e}")
            raise