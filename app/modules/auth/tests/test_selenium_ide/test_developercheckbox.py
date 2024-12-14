# Generated by Selenium IDE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from core.selenium.common import initialize_driver, close_driver


class TestDevelopercheckbox:
    def setup_method(self, method):
        self.driver = initialize_driver()
        self.vars = {}

    def teardown_method(self, method):
        close_driver(self.driver)

    def test_developercheckbox(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(971, 1092)
        self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("saSAsaS")
        self.driver.find_element(By.ID, "surname").click()
        self.driver.find_element(By.ID, "surname").send_keys("dasdasdas")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").click()
        element = self.driver.find_element(By.ID, "email")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("user11@example.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("1234")
        element = self.driver.find_element(By.ID, "password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "is_developer").click()
        self.driver.find_element(By.ID, "submit").click()
