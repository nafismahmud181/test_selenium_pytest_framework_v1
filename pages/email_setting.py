import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class EmailSettingClass:
    def __init__(self, driver):
        self.driver = driver

    def email_setting(self):
        logger.info("Filling email, domain and subject details.")
        EmailDomain = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email-domains"))
        )
        EmailDomain.send_keys("aidocbuilder.com")
        logger.info("Email domain(s) updated.")
        EmailDomain.send_keys(Keys.TAB)

        EmailFrom = self.driver.execute_script("return document.activeElement")
        EmailFrom.send_keys("nafis@aidocbuilder.com")
        logger.info("Email from updated.")
        time.sleep(1)
        EmailFrom.send_keys(Keys.TAB)

        EmailSubjectMatchCriteria = self.driver.execute_script("return document.activeElement")
        EmailSubjectMatchCriteria.send_keys("Startswith")
        time.sleep(1)
        EmailSubjectMatchCriteria.send_keys(Keys.RETURN)
        EmailSubjectMatchCriteria.send_keys(Keys.TAB)

        EmailSubjectMatchCriteriaText = self.driver.execute_script("return document.activeElement")
        EmailSubjectMatchCriteriaText.send_keys("Demo email subject selenium")
        logger.info("Email subject updated.")
        time.sleep(1)
        EmailSubjectMatchCriteriaText.send_keys(Keys.TAB)