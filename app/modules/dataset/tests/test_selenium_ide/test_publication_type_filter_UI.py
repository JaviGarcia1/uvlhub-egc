# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestpublicationtypefilterUI():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testpublicationtypefilterUI(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1761, 962)
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-item:nth-child(3) .align-middle:nth-child(2)").click()
    self.driver.find_element(By.ID, "publication_type").click()
    dropdown = self.driver.find_element(By.ID, "publication_type")
    dropdown.find_element(By.XPATH, "//option[. = 'Data Management Plan']").click()
    self.driver.find_element(By.ID, "search-button").click()
    dropdown = self.driver.find_element(By.ID, "publication_type")
    dropdown.find_element(By.XPATH, "//option[. = 'Book']").click()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "search-button").click()
  
