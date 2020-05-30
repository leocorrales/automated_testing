import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select 									# Esta libreria nos permite hacer interaccion con el UI. Modulo de Select
from selenium.webdriver.common.keys import Keys 
import time


class usando_unittest(unittest.TestCase):
	
	def setUp(self):
		self.driver=webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_usando_select(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
		time.sleep(3)
		select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
		opcion = select.find_elements_by_tag_name("option")							# Encuentra los elements que estan en select y guardalos en Opcion. El option entre comillas lo consigo desplegando el xpath
		time.sleep(1)
		for option in opcion:														# Le agrego un for porque voy a recorrer los valores que almacene en opcion. Del tag name option que me guardaste en opcion voy a recorrer la lista
			print("Los valores son: %s" % option.get_attribute("text"))			    # #s se usa en python para concatenar una cadena. El "value" es el que se encuentra en el desplegable del xpath, a la derecha del option. Con value lista 0,1 2,3,4.. Con text me devuelve los nombres de las marcas
			option.click()															# hay que darle un click para verificar que se encuentra el componente en la lista
			time.sleep(1)
		seleccionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))	 # Select es una opcion del suppor UI, vuelvo a acceder al xpath para identificar una posicion en especifico
		seleccionar.select_by_value("10")											# Nissan se encuentra en la posicion nro 10 de value
		time.sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
