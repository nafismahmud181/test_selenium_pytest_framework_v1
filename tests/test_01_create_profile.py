# import time
#
# from pages.create_profile.add_documents_section import AddDocumentsSection
# from pages.create_profile.email_setting_section import EmailSettingSection
# from pages.navigation import NavigationToPages
# from pages.create_profile.notification_setting_section import NotificationSettingSection
# from pages.create_profile.radio_buttons_section import RadioButtonsSection
# from pages.create_profile.submit_panel_section import SubmitPanelSection
# from utils.logger import logger
# from pages.login_page import LoginPage
# from pages.create_profile.create_profile_name_section import CreateProfileNameSection
#
#
# def test_login(setup):
#     driver = setup
#     logger.info("Starting test: test_login")
#     login_page = LoginPage(driver)
#     login_page.login()
#
#     navigate_profile_page = NavigationToPages(driver)
#     navigate_profile_page.transaction_to_create_profile()
#
#     create_profile_name = CreateProfileNameSection(driver)
#     create_profile_name.fill_create_profile_form()
#
#     radio_page = RadioButtonsSection(driver)
#     radio_page.interact_with_radio_buttons()
#
#     add_documents_page = AddDocumentsSection(driver)
#     add_documents_page.add_documents()
#
#     email_settings = EmailSettingSection(driver)
#     email_settings.email_setting()
#
#     notification_setting_page = NotificationSettingSection(driver)
#     notification_setting_page.configure_notifications()
#
#     submit_panel_page = SubmitPanelSection(driver)
#     submit_panel_page.submit_form()
#
#     navigate_transaction_page = NavigationToPages(driver)
#     navigate_transaction_page.profile_to_transaction()
#
#     logger.info("Successfully created our profile")
#     time.sleep(10)
