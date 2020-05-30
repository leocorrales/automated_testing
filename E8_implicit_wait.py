import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 									
from selenium.webdriver.support.ui import WebDriverWait							 
from selenium.webdriver.support import expected_conditions as EC  

class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_usando_implicit_wait(self):
		driver= self.driver
		driver.implicitly_wait(5)											# Mando a llamar el driver, espera hasta 5 segundos para encontrar el elemento definido abajo. Una vez que lo encuentres salte y deja de esperar
		driver.get("http://www.google.com")
		myDynamicElement = driver.find_element_by_name("q")					# DynamicElement dice que si un componente presenta mas de un valor (uno de ellos es "q"), 
																			# debes de esperar a que aparezca el q porque al ser dinamico puede que este cambiando, por eso debe de esperar. 
																			# Obtiene la propiedad de los elementos que cambian de tamanio, posicion en la pantalla, etc
if __name__ == '__main__':
	unittest.main()




# Implicit wait sería practicamente igual a time.sleep ya que se le especifica que espere por una sentencia o un tiempo en especifico
# es un comando de selenium contra time.sleep que es de python
