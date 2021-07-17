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

class TestLogininvalid():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_logininvalid(self):
    # Test name: Login_invalid
    # Step # | name | target | value
    # 1 | open | http://localhost/penjualan_elektronik/pelanggan/loginPelanggan | 
    self.driver.get("http://localhost/penjualanelektronik/pelanggan/loginPelanggan")
    # 2 | setWindowSize | 889x694 | 
    self.driver.set_window_size(889, 694)
    # 3 | click | name=username | 
    self.driver.find_element(By.NAME, "username").click()
    # 4 | type | name=username | 092736473264
    self.driver.find_element(By.NAME, "username").send_keys("092736473264")
    # 5 | type | name=password | 12344444
    self.driver.find_element(By.NAME, "password").send_keys("12344444")
    # 6 | click | css=.button-box > button | 
    self.driver.find_element(By.CSS_SELECTOR, ".button-box > button").click()
    # 7 | close |  | 
    self.driver.close()
  
