import time

from selenium.webdriver.common.keys import Keys
from utils.logger import logger

class NotificationSettingPage:
    def __init__(self, driver):
        self.driver = driver

    def configure_notifications(self):
        logger.info("Configuring success notifications.")
        SuccessNotifyEmailSubject = self.driver.execute_script("return document.activeElement")
        SuccessNotifyEmailSubject.send_keys(Keys.SPACE)
        time.sleep(1)
        SuccessNotifyEmailSubject.send_keys(Keys.TAB)

        SuccessNotifyEmailSender = self.driver.execute_script("return document.activeElement")
        # SuccessNotifyEmailSender.send_keys(Keys.SPACE)
        time.sleep(1)
        SuccessNotifyEmailSender.send_keys(Keys.TAB)

        SuccessNotifyEmailRecipients = self.driver.execute_script("return document.activeElement")
        # SuccessNotifyEmailRecipients.send_keys(Keys.SPACE)
        time.sleep(1)
        SuccessNotifyEmailRecipients.send_keys(Keys.TAB)

        SuccessNotifyCCUsers = self.driver.execute_script("return document.activeElement")
        # SuccessNotifyCCUsers.send_keys(Keys.SPACE)
        time.sleep(1)
        SuccessNotifyCCUsers.send_keys(Keys.TAB)

        SuccessNotifyAdditionalEmails = self.driver.execute_script("return document.activeElement")
        # SuccessNotifyAdditionalEmails.send_keys(Keys.SPACE)
        time.sleep(1)
        SuccessNotifyAdditionalEmails.send_keys(Keys.TAB)

        # Failure Notification Settings
        FailureNotifyEmailSubject = self.driver.execute_script("return document.activeElement")
        FailureNotifyEmailSubject.send_keys(Keys.SPACE)
        time.sleep(1)
        FailureNotifyEmailSubject.send_keys(Keys.TAB)

        FailureNotifyEmailSender = self.driver.execute_script("return document.activeElement")
        # FailureNotifyEmailSender.send_keys(Keys.SPACE)
        time.sleep(1)
        FailureNotifyEmailSender.send_keys(Keys.TAB)

        FailureNotifyEmailRecipients = self.driver.execute_script("return document.activeElement")
        # FailureNotifyEmailRecipients.send_keys(Keys.SPACE)
        time.sleep(1)
        FailureNotifyEmailRecipients.send_keys(Keys.TAB)

        FailureNotifyCCUsers = self.driver.execute_script("return document.activeElement")
        # FailureNotifyCCUsers.send_keys(Keys.SPACE)
        time.sleep(1)
        FailureNotifyCCUsers.send_keys(Keys.TAB)

        FailureNotifyAdditionalEmails = self.driver.execute_script("return document.activeElement")
        # FailureNotifyAdditionalEmails.send_keys(Keys.SPACE)
        time.sleep(1)
        FailureNotifyAdditionalEmails.send_keys(Keys.TAB)

        logger.info("Notification settings updated.")
