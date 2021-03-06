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

class TestAddcart():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addcart(self):
    # Test name: addcart
    # Step # | name | target | value
    # 1 | open | http://localhost/penjualan_elektronik/pelanggan/ | 
    self.driver.get("http://localhost/penjualan_elektronik/pelanggan/")
    # 2 | setWindowSize | 884x696 | 
    self.driver.set_window_size(884, 696)
    # 3 | click | linkText=Product | 
    self.driver.find_element(By.LINK_TEXT, "Product").click()
    # 4 | click | linkText=Add to Cart | 
    self.driver.find_element(By.LINK_TEXT, "Add to Cart").click()
    # 5 | verifyText | linkText=Lampu Tidur | Lampu Tidur
    assert self.driver.find_element(By.LINK_TEXT, "Lampu Tidur").text == "Lampu Tidur"
    # 6 | click | css=.pt-40 .cart-price | 
    self.driver.find_element(By.CSS_SELECTOR, ".pt-40 .cart-price").click()
    # 7 | click | css=.show .default-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".show .default-btn").click()
    # 8 | mouseDownAt | css=.col-xl-3 > .header-right-wrap | 224.25,53
    element = self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3 > .header-right-wrap")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 9 | mouseMoveAt | css=.col-xl-3 > .header-right-wrap | 224.25,53
    element = self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3 > .header-right-wrap")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 10 | mouseUpAt | css=.col-xl-3 > .header-right-wrap | 224.25,53
    element = self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3 > .header-right-wrap")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 11 | click | css=.col-xl-3 > .header-right-wrap | 
    self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3 > .header-right-wrap").click()
    # 12 | verifyText | css=.pt-40 .cart-price | Rp. 90.000
    assert self.driver.find_element(By.CSS_SELECTOR, ".pt-40 .cart-price").text == "Rp. 90.000"
    # 13 | click | linkText=Product | 
    self.driver.find_element(By.LINK_TEXT, "Product").click()
    # 14 | click | css=.shop-list-price-action-wrap:nth-child(5) .list-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".shop-list-price-action-wrap:nth-child(5) .list-cart").click()
    # 15 | click | css=.pt-40 .cart-price | 
    self.driver.find_element(By.CSS_SELECTOR, ".pt-40 .cart-price").click()
    # 16 | mouseDownAt | css=.show > ul | 273.25,89.56666564941406
    element = self.driver.find_element(By.CSS_SELECTOR, ".show > ul")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 17 | mouseMoveAt | css=.show > ul | 273.25,89.56666564941406
    element = self.driver.find_element(By.CSS_SELECTOR, ".show > ul")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 18 | mouseUpAt | css=.show > ul | 273.25,89.56666564941406
    element = self.driver.find_element(By.CSS_SELECTOR, ".show > ul")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 19 | click | css=.show > .shopping-cart-bottom h4 | 
    self.driver.find_element(By.CSS_SELECTOR, ".show > .shopping-cart-bottom h4").click()
    # 20 | verifyText | css=.show .shop-total | Rp. 140000
    assert self.driver.find_element(By.CSS_SELECTOR, ".show .shop-total").text == "Rp. 140000"
    # 21 | click | css=.show .default-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".show .default-btn").click()
    # 22 | click | css=tr:nth-child(2) .sli | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) .sli").click()
    # 23 | click | css=.cart-shiping-update > a | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-shiping-update > a").click()
    # 24 | click | css=.pt-40 .cart-price | 
    self.driver.find_element(By.CSS_SELECTOR, ".pt-40 .cart-price").click()
    # 25 | click | css=.show .default-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".show .default-btn").click()
    # 26 | close |  | 
    self.driver.close()
  
