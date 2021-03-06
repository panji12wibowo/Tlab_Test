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

class TestLoginvalid():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginvalid(self):
    # Test name: Login_valid
    # Step # | name | target | value
    # 1 | open | http://localhost/penjualan_elektronik/pelanggan/ | 
    self.driver.get("http://localhost/penjualan_elektronik/pelanggan/")
    # 2 | setWindowSize | 884x695 | 
    self.driver.set_window_size(884, 695)
    # 3 | click | css=.sli-settings | 
    self.driver.find_element(By.CSS_SELECTOR, ".sli-settings").click()
    # 4 | click | linkText=Login | 
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    # 5 | click | name=username | 
    self.driver.find_element(By.NAME, "username").click()
    # 6 | type | name=username | 092736473264
    self.driver.find_element(By.NAME, "username").send_keys("092736473264")
    # 7 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 8 | type | name=password | 092736473264
    self.driver.find_element(By.NAME, "password").send_keys("092736473264")
    # 9 | click | css=.button-box > button | 
    self.driver.find_element(By.CSS_SELECTOR, ".button-box > button").click()
    # 10 | click | css=.sli-settings | 
    self.driver.find_element(By.CSS_SELECTOR, ".sli-settings").click()
    # 11 | click | css=li:nth-child(1) li:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) li:nth-child(1)").click()
    # 12 | verifyText | css=li:nth-child(1) li:nth-child(1) | Welcome, Pelanggan Kota Jakarta
    assert self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) li:nth-child(1)").text == "Welcome, Pelanggan Kota Jakarta"
    # 13 | close |  | 
    self.driver.close()
  
