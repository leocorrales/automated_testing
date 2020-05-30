import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_buscar_por_xpath(self):
		driver = self.driver
		driver.get("http://www.google.com")
		time.sleep(5)
		buscar_por_xpath = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
		time.sleep(3)
		buscar_por_xpath.send_keys("selenium")
		time.sleep(2)
		buscar_por_xpath.send_keys(Keys.ARROW_DOWN)							# usar la flecha hacia abajo para seleccionar algun valor
		buscar_por_xpath.send_keys(Keys.ARROW_DOWN)
		buscar_por_xpath.send_keys(Keys.ARROW_DOWN)
		buscar_por_xpath.send_keys(Keys.ARROW_DOWN)
		buscar_por_xpath.send_keys(Keys.ARROW_DOWN) 
		buscar_por_xpath.send_keys(Keys.RETURN)
		time.sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()








# xpath es una estructura de objetos
# existen 2 tipos: relativos y absolutos
#Relativo: tiene una gran ventaja frente al absoluto. Parte de un nodo especifico y permite que si un archivo cambia de carpeta pueda ser encontrado siempre y cuando se encuentre bajo el nodo qeu definimos. Es el mas usado cuando se automatiza. Este es el xpath del buscador de google:   //*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input 
#Absoluto, es toda la ruta y si alguien mueve una carpeta nos marcara error ya que no lo encontrara 
