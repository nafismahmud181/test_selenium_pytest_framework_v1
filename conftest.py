import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.set_window_size(1440, 900)
    driver.set_window_position(0, 0)
    yield driver
    driver.quit()
