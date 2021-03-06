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

class TestTransaksi():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_transaksi(self):
    # Test name: transaksi
    # Step # | name | target | value
    # 1 | open | http://localhost/penjualan_elektronik/pelanggan/ | 
    self.driver.get("http://localhost/penjualanelektronik/pelanggan/")
    # 2 | setWindowSize | 889x694 | 
    self.driver.set_window_size(889, 694)
    # 3 | click | linkText=List Transaksi Pembelian | 
    self.driver.find_element(By.LINK_TEXT, "List Transaksi Pembelian").click()
    # 4 | click | linkText=Upload | 
    self.driver.find_element(By.LINK_TEXT, "Upload").click()
    # 5 | click | name=gambar | 
    self.driver.find_element(By.NAME, "gambar").click()
    # 6 | type | name=gambar | C:\fakepath\_1_4ea086c4be0c5a28efa20302fe72344f.jpg
    self.driver.find_element(By.NAME, "gambar").send_keys("C:\\fakepath\\_1_4ea086c4be0c5a28efa20302fe72344f.jpg")
    # 7 | click | css=.button-box > button | 
    self.driver.find_element(By.CSS_SELECTOR, ".button-box > button").click()
    # 8 | verifyText | css=.btn-success | Sudah Diupload
    assert self.driver.find_element(By.CSS_SELECTOR, ".btn-success").text == "Sudah Diupload"
  
