import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
	
	def setUp(self):
		self.driver=webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_cambiar_ventana(self):
		driver = self.driver										
		driver.get("http://www.google.com")
		time.sleep(3)
		driver.execute_script("window.open('');") 								# esto es de python y no se selenium. Que abra una ventana web nueva. 
		time.sleep(2)
		driver.switch_to.window(driver.window_handles[1])						# le digo que se posicione en la 2da pestania. Arranca en 0, le digo 1 o sea la 2da ventana
		driver.get("http://stackoverflow.com")
		time.sleep(3)
		driver.switch_to.window(driver.window_handles[0])						# le digo que se posicione en la 1ra
		time.sleep(3)
		
	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
		unittest.main()	