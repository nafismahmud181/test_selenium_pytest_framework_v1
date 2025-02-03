import time
from selenium.webdriver.common.keys import Keys
from utils.logger import logger

class SubmitPanelPage:
    def __init__(self, driver):
        self.driver = driver

    def submit_form(self):
        logger.info("Submitting the form.")
        submit_button = self.driver.execute_script("return document.activeElement")
        submit_button.send_keys(Keys.RETURN)
        time.sleep(5)
        logger.info("Form submitted successfully.")
