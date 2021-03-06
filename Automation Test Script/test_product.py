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

class TestProduct():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_product(self):
    # Test name: product
    # Step # | name | target | value
    # 1 | open | http://localhost/penjualan_elektronik/pelanggan/ | 
    self.driver.get("http://localhost/penjualanelektronik/pelanggan/")
    # 2 | setWindowSize | 884x694 | 
    self.driver.set_window_size(884, 694)
    # 3 | click | linkText=Product | 
    self.driver.find_element(By.LINK_TEXT, "Product").click()
    # 4 | click | linkText=Lampu | 
    self.driver.find_element(By.LINK_TEXT, "Lampu").click()
    # 5 | click | linkText=Laptop | 
    self.driver.find_element(By.LINK_TEXT, "Laptop").click()
    # 6 | click | linkText=Kabel | 
    self.driver.find_element(By.LINK_TEXT, "Kabel").click()
    # 7 | close |  | 
    self.driver.close()
  
