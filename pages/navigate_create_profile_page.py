from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.logger import logger

class NavigateCreateProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def access_navigate_create_profile_page(self):
        logger.info("Accessing transaction menu.")
        action = ActionChains(self.driver)
        transaction_menu = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='dropdown nav-item sidebar-group-active active open']"))
        )
        action.move_to_element(transaction_menu).perform()

        logger.info("Navigating to Create Profile page.")
        create_profile = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Create Profile"))
        )
        create_profile.click()
        action.move_by_offset(500, 0).perform()
        logger.info("Navigation to Create Profile page completed.")