import time
from selenium.webdriver.common.keys import Keys
from utils.logger import logger

class RadioButtonsPage:
    def __init__(self, driver):
        self.driver = driver

    def interact_with_radio_buttons(self):
        logger.info("Interacting with ManualValidation radio button.")
        ManualValidation = self.driver.execute_script("return document.activeElement")
        time.sleep(1)
        ManualValidation.send_keys(Keys.SPACE)
        ManualValidation.send_keys(Keys.TAB)

        logger.info("Interacting with MultiShipment radio button.")
        MultiShipment = self.driver.execute_script("return document.activeElement")
        time.sleep(1)
        MultiShipment.send_keys(Keys.TAB)

        logger.info("Interacting with SendTimeStamp radio button.")
        SendTimeStamp = self.driver.execute_script("return document.activeElement")
        time.sleep(1)
        SendTimeStamp.send_keys(Keys.TAB)

        logger.info("Interacting with ParseDocument radio button.")
        ParseDocument = self.driver.execute_script("return document.activeElement")
        time.sleep(1)
        ParseDocument.send_keys(Keys.TAB)

        logger.info("Interacting with IgnoreDensePages radio button.")
        IgnoreDensePages = self.driver.execute_script("return document.activeElement")
        time.sleep(1)
        IgnoreDensePages.send_keys(Keys.TAB)

        logger.info("Interacting with ExceptionalExcel radio button.")
        ExceptionalExcel = self.driver.execute_script("return document.activeElement")
        time.sleep(1)
        ExceptionalExcel.send_keys(Keys.SPACE)
        ExceptionalExcel.send_keys(Keys.TAB)

        logger.info("All radio button interactions completed.")
