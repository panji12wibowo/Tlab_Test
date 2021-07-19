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

class TestLogout():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_logout(self):
    # Test name: logout
    # Step # | name | target | value
    # 1 | open | http://localhost/penjualanelektronik/pelanggan/ | 
    self.driver.get("http://localhost/penjualanelektronik/pelanggan/")
    # 2 | setWindowSize | 884x697 | 
    self.driver.set_window_size(884, 697)
    # 3 | click | css=.sli-settings | 
    self.driver.find_element(By.CSS_SELECTOR, ".sli-settings").click()
    # 4 | click | linkText=Login | 
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    # 5 | click | name=username | 
    self.driver.find_element(By.NAME, "username").click()
    # 6 | type | name=username | 1
    self.driver.find_element(By.NAME, "username").send_keys("1")
    # 7 | click | css=.sli-settings | 
    self.driver.find_element(By.CSS_SELECTOR, ".sli-settings").click()
    # 8 | click | linkText=Logout | 
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    # 9 | close |  | 
    self.driver.close()
    # 10 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 11 | type | name=password | 1
    self.driver.find_element(By.NAME, "password").send_keys("1")
    # 12 | click | css=.button-box > button | 
    self.driver.find_element(By.CSS_SELECTOR, ".button-box > button").click()
  