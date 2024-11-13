# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestUI():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  def teardown_method(self, method):
    self.driver.quit()

  def test_selenium(self):
    self.driver.get("http://localhost:5000/")
    self.driver.set_window_size(1536, 816)
    self.driver.find_element(By.LINK_TEXT,"Sample dataset 4").click()
    self.driver.find_element(By.ID, "btnGroupDropExport132").click()
    self.driver.find_element(By.ID, "btnGroupDropExport132").click()
    self.driver.find_element(By.ID, "btnGroupDrop132").click()
    self.driver.find_element(By.LINK_TEXT,"Syntax check").click()
    self.driver.find_element(By.CSS_SELECTOR,".list-group-item:nth-child(2) .col-12 > .btn").click()
    self.driver.close()
