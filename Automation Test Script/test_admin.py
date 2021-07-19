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

class TestAdmin():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_admin(self):
    # Test name: admin
    # Step # | name | target | value
    # 1 | open | http://localhost/penjualan_elektronik/ | 
    self.driver.get("http://localhost/penjualan_elektronik/")
    # 2 | setWindowSize | 884x698 | 
    self.driver.set_window_size(884, 698)
    # 3 | click | name=username | 
    self.driver.find_element(By.NAME, "username").click()
    # 4 | type | name=username | admin
    self.driver.find_element(By.NAME, "username").send_keys("admin")
    # 5 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 6 | type | name=password | admin
    self.driver.find_element(By.NAME, "password").send_keys("admin")
    # 7 | click | css=.btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # 8 | click | css=.pull-left > p | 
    self.driver.find_element(By.CSS_SELECTOR, ".pull-left > p").click()
    # 9 | verifyText | css=.pull-left > p | Administrator
    assert self.driver.find_element(By.CSS_SELECTOR, ".pull-left > p").text == "Administrator"
    # 10 | click | css=li:nth-child(2) span | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) span").click()
    # 11 | click | css=h1 | 
    self.driver.find_element(By.CSS_SELECTOR, "h1").click()
    # 12 | verifyText | css=h1 | Dashboard
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Dashboard"
    # 13 | click | css=li:nth-child(3) span | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) span").click()
    # 14 | click | css=h1 | 
    self.driver.find_element(By.CSS_SELECTOR, "h1").click()
    # 15 | verifyText | css=h1 | Data Produk
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Data Produk"
    # 16 | click | css=.box-tools .fa | 
    self.driver.find_element(By.CSS_SELECTOR, ".box-tools .fa").click()
    # 17 | click | name=id_produk | 
    self.driver.find_element(By.NAME, "id_produk").click()
    # 18 | type | name=id_produk | K123
    self.driver.find_element(By.NAME, "id_produk").send_keys("K123")
    # 19 | click | name=nama_produk | 
    self.driver.find_element(By.NAME, "nama_produk").click()
    # 20 | type | name=nama_produk | KABEL
    self.driver.find_element(By.NAME, "nama_produk").send_keys("KABEL")
    # 21 | mouseOver | id=cke_32 | 
    element = self.driver.find_element(By.ID, "cke_32")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 22 | selectFrame | index=0 | 
    self.driver.switch_to.frame(0)
    # 23 | click | css=html | 
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 24 | editContent | css=.cke_editable | <p>KABEL MURAH<br></p>
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>KABEL MURAH<br></p>'}", element)
    # 25 | selectFrame | relative=parent | 
    self.driver.switch_to.default_content()
    # 26 | click | name=harga | 
    self.driver.find_element(By.NAME, "harga").click()
    # 27 | type | name=harga | 18000
    self.driver.find_element(By.NAME, "harga").send_keys("18000")
    # 28 | click | name=stok | 
    self.driver.find_element(By.NAME, "stok").click()
    # 29 | type | name=stok | 10
    self.driver.find_element(By.NAME, "stok").send_keys("10")
    # 30 | click | css=.select2-selection | 
    self.driver.find_element(By.CSS_SELECTOR, ".select2-selection").click()
    # 31 | click | name=gambar | 
    self.driver.find_element(By.NAME, "gambar").click()
    # 32 | type | name=gambar | C:\fakepath\3-0.jpg
    self.driver.find_element(By.NAME, "gambar").send_keys("C:\\fakepath\\3-0.jpg")
    # 33 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # 34 | click | css=.alert | 
    self.driver.find_element(By.CSS_SELECTOR, ".alert").click()
    # 35 | verifyText | css=.alert | ×\nTambah Data Produk Gagal.
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert").text == "×\\\\nTambah Data Produk Gagal."
    # 36 | click | css=.box-tools .fa | 
    self.driver.find_element(By.CSS_SELECTOR, ".box-tools .fa").click()
    # 37 | click | name=id_produk | 
    self.driver.find_element(By.NAME, "id_produk").click()
    # 38 | type | name=id_produk | LAMP12
    self.driver.find_element(By.NAME, "id_produk").send_keys("LAMP12")
    # 39 | click | name=nama_produk | 
    self.driver.find_element(By.NAME, "nama_produk").click()
    # 40 | type | name=nama_produk | LAMPU
    self.driver.find_element(By.NAME, "nama_produk").send_keys("LAMPU")
    # 41 | selectFrame | index=0 | 
    self.driver.switch_to.frame(0)
    # 42 | click | css=html | 
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 43 | editContent | css=.cke_editable | <p>LAMPU MURAH<br></p>
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>LAMPU MURAH<br></p>'}", element)
    # 44 | selectFrame | relative=parent | 
    self.driver.switch_to.default_content()
    # 45 | click | name=harga | 
    self.driver.find_element(By.NAME, "harga").click()
    # 46 | type | name=harga | 20000
    self.driver.find_element(By.NAME, "harga").send_keys("20000")
    # 47 | click | name=stok | 
    self.driver.find_element(By.NAME, "stok").click()
    # 48 | type | name=stok | 10
    self.driver.find_element(By.NAME, "stok").send_keys("10")
    # 49 | click | id=select2-kategori-zo-container | 
    self.driver.find_element(By.ID, "select2-kategori-zo-container").click()
    # 50 | click | name=gambar | 
    self.driver.find_element(By.NAME, "gambar").click()
    # 51 | type | name=gambar | C:\fakepath\3-0.jpg
    self.driver.find_element(By.NAME, "gambar").send_keys("C:\\fakepath\\3-0.jpg")
    # 52 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # 53 | click | css=.box-tools .fa | 
    self.driver.find_element(By.CSS_SELECTOR, ".box-tools .fa").click()
    # 54 | click | name=id_produk | 
    self.driver.find_element(By.NAME, "id_produk").click()
    # 55 | type | name=id_produk | LAMP12
    self.driver.find_element(By.NAME, "id_produk").send_keys("LAMP12")
    # 56 | click | name=nama_produk | 
    self.driver.find_element(By.NAME, "nama_produk").click()
    # 57 | type | name=nama_produk | LAMPU
    self.driver.find_element(By.NAME, "nama_produk").send_keys("LAMPU")
    # 58 | selectFrame | index=0 | 
    self.driver.switch_to.frame(0)
    # 59 | click | css=html | 
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 60 | editContent | css=.cke_editable | <p>LAMPU<br></p>
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>LAMPU<br></p>'}", element)
    # 61 | selectFrame | relative=parent | 
    self.driver.switch_to.default_content()
    # 62 | click | name=harga | 
    self.driver.find_element(By.NAME, "harga").click()
    # 63 | type | name=harga | 2
    self.driver.find_element(By.NAME, "harga").send_keys("2")
    # 64 | sendKeys | name=harga | ${KEY_DOWN}
    self.driver.find_element(By.NAME, "harga").send_keys(Keys.DOWN)
    # 65 | type | name=harga | 20000
    self.driver.find_element(By.NAME, "harga").send_keys("20000")
    # 66 | click | name=stok | 
    self.driver.find_element(By.NAME, "stok").click()
    # 67 | type | name=stok | 10
    self.driver.find_element(By.NAME, "stok").send_keys("10")
    # 68 | click | name=gambar | 
    self.driver.find_element(By.NAME, "gambar").click()
    # 69 | type | name=gambar | C:\fakepath\_1_4ea086c4be0c5a28efa20302fe72344f.jpg
    self.driver.find_element(By.NAME, "gambar").send_keys("C:\\fakepath\\_1_4ea086c4be0c5a28efa20302fe72344f.jpg")
    # 70 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # 71 | click | css=.alert | 
    self.driver.find_element(By.CSS_SELECTOR, ".alert").click()
    # 72 | verifyText | css=.alert | ×\nTambah Data Produk Berhasil.
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert").text == "×\\\\nTambah Data Produk Berhasil."
    # 73 | click | css=.odd:nth-child(1) .btn-primary > .fa | 
    self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) .btn-primary > .fa").click()
    # 74 | click | name=harga | 
    self.driver.find_element(By.NAME, "harga").click()
    # 75 | type | name=harga | 290000
    self.driver.find_element(By.NAME, "harga").send_keys("290000")
    # 76 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # 77 | click | css=.alert | 
    self.driver.find_element(By.CSS_SELECTOR, ".alert").click()
    # 78 | verifyText | css=.alert | ×\nEdit Data Produk Berhasil.
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert").text == "×\\\\nEdit Data Produk Berhasil."
    # 79 | click | css=li:nth-child(4) span | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) span").click()
    # 80 | click | css=h1 | 
    self.driver.find_element(By.CSS_SELECTOR, "h1").click()
    # 81 | verifyText | css=h1 | Data Transaksi Produk
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Data Transaksi Produk"
    # 82 | click | linkText=List Penjualan | 
    self.driver.find_element(By.LINK_TEXT, "List Penjualan").click()
    # 83 | click | css=.content-header | 
    self.driver.find_element(By.CSS_SELECTOR, ".content-header").click()
    # 84 | verifyText | css=.content-header | Data Penjualan
    assert self.driver.find_element(By.CSS_SELECTOR, ".content-header").text == "Data Penjualan"
    # 85 | verifyText | linkText=Nota Belum Diupload | Nota Belum Diupload
    assert self.driver.find_element(By.LINK_TEXT, "Nota Belum Diupload").text == "Nota Belum Diupload"
    # 86 | click | linkText=Next | 
    self.driver.find_element(By.LINK_TEXT, "Next").click()
    # 87 | click | linkText=Kirim Barang | 
    self.driver.find_element(By.LINK_TEXT, "Kirim Barang").click()
    # 88 | click | css=.alert | 
    self.driver.find_element(By.CSS_SELECTOR, ".alert").click()
    # 89 | verifyText | css=.alert | ×\nBarang Dikirimkan. Transaksi Selesai.
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert").text == "×\\\\nBarang Dikirimkan. Transaksi Selesai."
    # 90 | click | linkText=Next | 
    self.driver.find_element(By.LINK_TEXT, "Next").click()
    # 91 | click | css=.content-wrapper | 
    self.driver.find_element(By.CSS_SELECTOR, ".content-wrapper").click()
    # 92 | mouseDownAt | css=.even:nth-child(4) > td:nth-child(4) | 232.0999755859375,27.66668701171875
    element = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(4) > td:nth-child(4)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 93 | mouseMoveAt | css=.even:nth-child(4) > td:nth-child(4) | 232.0999755859375,27.66668701171875
    element = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(4) > td:nth-child(4)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 94 | mouseUpAt | css=.even:nth-child(4) > td:nth-child(4) | 232.0999755859375,27.66668701171875
    element = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(4) > td:nth-child(4)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 95 | click | css=.even:nth-child(4) | 
    self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(4)").click()
    # 96 | mouseDownAt | css=.even:nth-child(4) > td:nth-child(4) | 232.0999755859375,27.66668701171875
    element = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(4) > td:nth-child(4)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 97 | mouseMoveAt | css=.even:nth-child(4) > td:nth-child(5) | 128.33331298828125,16.66668701171875
    element = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(4) > td:nth-child(5)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 98 | mouseUpAt | css=.even:nth-child(4) > td:nth-child(5) | 128.33331298828125,16.66668701171875
    element = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(4) > td:nth-child(5)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 99 | verifyText | linkText=Barang Sudah Dikirim | Barang Sudah Dikirim
    assert self.driver.find_element(By.LINK_TEXT, "Barang Sudah Dikirim").text == "Barang Sudah Dikirim"
    # 100 | click | css=li:nth-child(5) span | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) span").click()
    # 101 | mouseOver | linkText=List Penjualan | 
    element = self.driver.find_element(By.LINK_TEXT, "List Penjualan")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 102 | mouseOut | linkText=List Penjualan | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 103 | click | linkText=Next | 
    self.driver.find_element(By.LINK_TEXT, "Next").click()
    # 104 | click | linkText=Administrator | 
    self.driver.find_element(By.LINK_TEXT, "Administrator").click()
    # 105 | click | linkText=Sign out | 
    self.driver.find_element(By.LINK_TEXT, "Sign out").click()
    # 106 | close |  | 
    self.driver.close()
  