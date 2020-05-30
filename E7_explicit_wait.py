import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 									# importo una nueva libreria, es para trabajar con explicit wait
from selenium.webdriver.support.ui import WebDriverWait							# importo una nueva libreria, es para mandar a llamar uan opcion de ui del driver.wait 
from selenium.webdriver.support import expected_conditions as EC                 # le decimos que vamos a declarar una condicion para poder continuar con la automatizacion. Expected condition es modulo de la libreria de selenium. Mandamos a llamar webdriver, by, webdriverwait y EC 

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_usando_explicit_wait(self):
		driver = self.driver
		driver.get("http://www.google.com")
		try:																							# Cargame en el elemento (lo que tengas en Google) 			
			element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))   # intentalo 10 veces hasta que tengas la presencia localizada del elemento con NAME = q y lo carga en EC.presence..
		finally:		
			driver.quit()																				# si lo encontro o no lo encontro tenemos que finalizarlo, de lo contrario tendremos muchas ventanas abiertas

if __name__ == '__main__':
	unittest.main()					


# Explicit wait: hasta que no se cargue cierto elemento no continues con la automatizacion
# la ventaja de explicit wait frente a time.sleep es que con esta ultime nos llenamos de tiempos de espera que alargan el tiempo de la automatizacion y utilizando 
# el explicit wait una vez que aparece ya lo cargo y no tengo que estar esperando los segundos definidos en el time.sleep