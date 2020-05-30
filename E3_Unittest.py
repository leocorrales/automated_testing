import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_buscar(self):
		driver = self.driver													# esto es para abrir o cargar nuestras paginas
		driver.get("http://www.google.com")
		self.assertIn("Google", driver.title)		  							# Busca que exista Google en el titulo						
		elemento = driver.find_element_by_name("q")
		elemento.send_keys("selenium")
		elemento.send_keys(Keys.RETURN)											# RETURN es igual que ENTER
		time.sleep(5)
		assert "No se encontro el elemento:" not in driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()