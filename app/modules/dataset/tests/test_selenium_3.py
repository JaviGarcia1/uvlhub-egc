# Generated by Selenium IDE
# import pytest
# import time
# import json
# from selenium import webdriver
from selenium.webdriver.common.by import By
from core.selenium.common import initialize_driver

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTest2:
    def setup_method(self, method):
        self.driver = initialize_driver()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test2(self):
        self.driver.get("http://localhost:5000/")
        self.driver.set_window_size(1490, 840)
        self.driver.find_element(By.LINK_TEXT, "Elephants").click()
        self.driver.find_element(By.ID, "btnGroupDropExport3").click()
        self.driver.find_element(By.ID, "search").click()
        self.driver.find_element(By.ID, "btnGroupDropExport3").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "li:nth-child(1) > .dropdown-item"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "li:nth-child(2) > .dropdown-item"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "li:nth-child(1) > .dropdown-item"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "li:nth-child(3) > .dropdown-item"
        ).click()
        self.driver.close()