from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://micuenta.oca.com.uy/index.aspx")

usuario = driver.find_element_by_name("txtusuario")								# encontrar elemento por atributo name, tambien es posible por Id
usuario.send_keys("xxxxxxx")
	
clave = driver.find_element_by_name("txtpassword")
clave.send_keys("xxxxxxx")														# acciones
clave.send_keys(Keys.ENTER)

driver.close()
