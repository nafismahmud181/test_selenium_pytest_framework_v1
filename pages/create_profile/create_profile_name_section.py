import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class CreateProfileNameSection:
    def __init__(self, driver):
        self.driver = driver

    def fill_create_profile_form(self):
        logger.info("Filling out the Create Profile form.")

        try:
            CustomerName = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "customer-name"))
            )
            CustomerName.send_keys("E2E Selenium Testing (1)")
            CustomerName.send_keys(Keys.TAB)

            project = self.driver.execute_script("return document.activeElement")
            project.send_keys("ShipmentCreate")
            time.sleep(1)
            project.send_keys(Keys.RETURN)
            project.send_keys(Keys.TAB)

            country = self.driver.execute_script("return document.activeElement")
            country.send_keys("Bangladesh")
            time.sleep(1)
            country.send_keys(Keys.RETURN)
            country.send_keys(Keys.TAB)

            transport = self.driver.execute_script("return document.activeElement")
            transport.send_keys("All")
            time.sleep(1)
            transport.send_keys(Keys.RETURN)
            transport.send_keys(Keys.TAB)

            logger.info("Create Profile form successfully filled.")

        except Exception as e:
            logger.error(f"An error occurred while filling the form: {e}")
            raise
