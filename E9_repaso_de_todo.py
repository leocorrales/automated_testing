import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

class usando_unittest(unittest.TestCase):
		
	def setUp(self):
		self.driver=webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_hacer_login(self):
		driver = self.driver
		driver.get("http://www.mercadolibre.com.uy")
		time.sleep(3)
		buscar_ingresar = driver.find_element_by_xpath("//*[@id='nav-header-menu']/a[2]")
		buscar_ingresar.send_keys(Keys.ENTER)
		buscar_usuario = driver.find_element_by_xpath("//*[@id='user_id']")
		buscar_usuario.send_keys("xxxxxxxxxxxx@gmail.com")
		buscar_usuario.send_keys(Keys.ENTER)
		time.sleep(3)
		buscar_password = driver.find_element_by_xpath("//*[@id='password']")
		buscar_password.send_keys("xxxxxxxxxxxx")
		buscar_password.send_keys(Keys.ENTER)
		time.sleep(3)
		buscar_peugeot = driver.find_element_by_xpath("/html/body/header/div/form/input")
		buscar_peugeot.send_keys("peugeot 2008")
		buscar_peugeot.send_keys(Keys.ARROW_DOWN)
		buscar_peugeot.send_keys(Keys.ARROW_DOWN)
		buscar_peugeot.send_keys(Keys.RETURN)
		time.sleep(2)
		buscar_pagina_dos = driver.find_element_by_xpath("//*[@id='results-section']/div[2]/ul/li[2]/a")
		buscar_pagina_dos.send_keys(Keys.ENTER)
		time.sleep(3)
		precio = driver.find_element_by_xpath("//*[@id='MLU471391002']/a")         #inspeccione elemento y el xpath es del item-url
		precio.send_keys(Keys.ENTER)            
		time.sleep(2)

		driver.execute_script("window.open('');") 								# esto es de python y no se selenium. Que abra una ventana web nueva. 
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[1])						# le digo que se posicione en la 2da pestania. Arranca en 0, le digo 1 o sea la 2da ventana
		driver.get("https://www.peugeot.com.uy/gama/descubra-nuestra-gama-de-vehiculos-peugeot.html")
		time.sleep(2)
		buscar_gama = driver.find_element_by_xpath("//*[@id='27768_4_1538_150_3389_5d10e50fded75']/div[2]/a[1]")
		time.sleep(2)
		buscar_gama.send_keys(Keys.ENTER)
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[0])						# le digo que se posicione en mercadolibre resultado
		time.sleep(3)
		driver.back()
		driver.back()
		driver.back()
		time.sleep(5)

		
	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()