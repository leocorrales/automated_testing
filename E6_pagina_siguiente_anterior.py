import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

class usando_unittest(unittest.TestCase):
		
	def setUp(self):
		self.driver=webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_usando_pag_sig_o_anterior(self):
		driver=self.driver
		driver.get("http://www.gmail.com")
		time.sleep(3)
		driver.get("http://www.google.com")														# abro google en la misma pestania que gmail
		time.sleep(3)
		driver.get("http://www.youtube.com")													# abro youtube en la misma pestania que los anteriores
		time.sleep(3)
		driver.back()																			# funcion de selenium que me permite volver a la pagina anterior. Seria a Google
		time.sleep(3)
		driver.back()																			# me permite volver a la 1er pagina. seria Gmail
		time.sleep(3)																		
		driver.forward()																		# me permite avanzar 1 pagina. Iria a Google	
		time.sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()