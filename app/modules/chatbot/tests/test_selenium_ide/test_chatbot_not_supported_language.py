# Generated by Selenium IDE
from selenium.webdriver.common.by import By
from core.selenium.common import initialize_driver, close_driver

class TestChatbotnotsupportedlanguage():
  def setup_method(self, method):
    self.driver = initialize_driver()
    self.vars = {}

  def teardown_method(self, method):
    close_driver(self.driver)

  def test_chatbotnotsupportedlanguage(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1920, 1048)
    self.driver.find_element(By.LINK_TEXT, "Romeo").click()
    self.driver.find_element(By.ID, "chatInput").click()
    self.driver.find_element(By.ID, "chatInput").send_keys("Hi Romeo, how is going on?")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()