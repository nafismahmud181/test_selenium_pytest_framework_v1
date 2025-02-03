import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.logger import logger

class NavigationToPages:
    def __init__(self, driver):
        self.driver = driver

    def transaction_to_create_profile(self):
        try:
            logger.info("Accessing transaction menu.")
            action = ActionChains(self.driver)
            transaction_menu = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//li[@class='dropdown nav-item sidebar-group-active active open']"))
            )
            action.move_to_element(transaction_menu).perform()

            logger.info("Navigating to Create Profile page.")
            create_profile = WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Create Profile"))
            )
            create_profile.click()
            action.move_by_offset(500, 0).perform()
            action.reset_actions()
            logger.info("Navigation to Create Profile page completed.")
            time.sleep(5)
        except Exception as e:
            logger.error(f"An error occurred while navigating to create profile page: {e}")
            raise


    def transaction_to_training(self):
        try:
            logger.info("Accessing transaction menu.")
            action = ActionChains(self.driver)
            training_menu = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.XPATH, "(//li[@class='dropdown nav-item'])[1]"))
            )
            action.move_to_element(training_menu).perform()

            logger.info("Navigating to training page.")
            training = WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Training"))
            )
            training.click()
            action.move_by_offset(500, 0).perform()
            action.reset_actions()
            logger.info("Navigation to training page completed.")
            time.sleep(5)
        except Exception as e:
            logger.error(f"An error occurred while navigating to training page: {e}")
            raise

    def profile_to_transaction(self):
        try:
            logger.info("Accessing transaction menu.")
            action = ActionChains(self.driver)
            transaction_menu = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//li[@class='dropdown nav-item sidebar-group-active active open']"))
            )
            action.move_to_element(transaction_menu).perform()

            logger.info("Navigating to Transactions page.")
            create_profile = WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Transactions"))
            )
            create_profile.click()
            action.move_by_offset(500, 0).perform()
            action.reset_actions()
            logger.info("Navigation to Transactions page completed.")
            time.sleep(5)

        except Exception as e:
            logger.error(f"An error occurred while filling the form: {e}")
            raise

