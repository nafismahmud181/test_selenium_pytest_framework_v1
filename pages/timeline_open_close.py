import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class TimelineOpenClose:
    def __init__(self, driver):
        self.driver = driver

    def timeline_open(self):
        try:
            timeline = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "timeline-wrapper"))
            )
            timeline.click()
            time.sleep(5)
        except Exception as e:
            logger.error(f"An error occurred while opening timeline: {e}")
            raise

    def timeline_close(self):
        try:
            timeline_close = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "mb-50"))
            )
            timeline_close.click()
        except Exception as e:
            logger.error(f"An error occurred while opening timeline: {e}")
            raise

