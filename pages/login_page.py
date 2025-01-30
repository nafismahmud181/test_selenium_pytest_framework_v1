import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import logger

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username="admin", password="admin"):
        logger.info("Navigating to login page.")
        self.driver.get("http://10.10.1.10/login")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-password"))
        )
        logger.info("Entering username.")
        self.driver.find_element(By.ID, "login-username").send_keys(username)

        logger.info("Entering password.")
        password_input = self.driver.find_element(By.ID, "login-password")
        password_input.send_keys(password)
        self.driver.save_screenshot("screenshots/login_success.png")
        password_input.send_keys(Keys.ENTER)
        time.sleep(6)
