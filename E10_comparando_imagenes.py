import unittest																	# hacer uso de unittest
from selenium import webdriver                                                  # uso del modulo de selenium
from selenium.webdriver.common.by import By 									# llamada de caracteristicas especiales de selenium
from selenium.webdriver.support.ui import WebDriverWait							#
from selenium.webdriver.support import expected_conditions as EC  				# implicit e explicit wait
import time
import cv2                                                                      # previamente tuve que haber instalado en cmd "pip install opencv-python". Esta es la libreria de Opencv

class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
 	
	def test_usando_opencv(self):
 		driver = self.driver
 		driver.get("http://www.google.com")
 		driver.save_screenshot('img2.png')										# comando para hacer screenshot, la guardo con el nombre 2 porque se entiende que ya tengo una imagen 1 que es contra la cual la voy a comparar
 		time.sleep(3)

	def test_comparando_imagenes(self):																			# funcion para comparar la imagen
		img1 = cv2.imread('img1.png')																			# declaro la variable para guardar la image que voy a comprar. Va a leer la img1.png
		img2 = cv2.imread('img2.png')
																												# una vez cargadas las 2 imagenes en variables realizo la comparacion
		diferencia = cv2.absdiff(img1, img2)																	# esto es openCV y no selenium, el comando absdiff es de opencv
		imagen_gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)												# Esto es de opencv, convierto las imagenes RGB a escalas de grises ya que es mas facil comparar asi debido a que el sistema es binario (B y N)
		contours,_ = cv2.findContours(imagen_gris,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)     				# se declara coleccion de datos para que sea una comparacion y empezar a trabajar con las imagenes

		for c in contours:																						# hacemos un for para que se haga la comparacion, lectura ciclica de las 2 imagenes. c es un contador cualquiera.
			if cv2.contourArea(c) >= 20:																		# 20 es el rango de escala de grises, cuando menos es el valor mas fina es la busqueda y sera mas propoenso a errores
				posicion_x, posicion_y, ancho,alto = cv2.boundingRect(c)										# declaro variable para encontrar la diferencia. boundingRect, son las dimensiones que hay del cuadrito negro y su ubicacion en x e y
				cv2.rectangle(img1, (posicion_x,posicion_y),(posicion_x+ancho,posicion_y+alto),(0,0,255),2)     # le hago un recuadro para que la remarque la diferencia. Cv2 guardalo en un rectangulo de la img1 

		while (1):																								# muestro las imagenes
			cv2.imshow('Imagen1',img1)
			cv2.imshow('Imagen2',img2)
			cv2.imshow('Diferencias detectadas',diferencia)
			teclado = cv2.waitKey(5) & 0xFF
			if teclado ==27:																				    # if teclado == 27 es la tecla Esc, para que salga, termine y cierre las ventanas	
				break 
		cv2.destroyAllWindows()

if __name__ == '__main__':
	unittest.main()



# tengo que tener definida la imagen base contra la cual voy a comprar. La misma debe estar guardada en la misma carpeta donde esta el caso de prueba