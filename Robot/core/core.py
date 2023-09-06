from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

#Abrir Chrome
driver_service = Service(executable_path='webdriver//chromedriver.exe')
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

#Abrir Pagina
driver.get("https://www.latamairlines.com/")

# Maximizar la ventana del navegador
driver.maximize_window()

#DATOS DE PRUEBA
mes_ida = "septiembre"
day_ida = "11"

mes_vuelta = "septiembre"
day_vuelta = "16"


#Ciudad Origen
origen = driver.find_element(By.XPATH, '//*[@id="txtInputOrigin_field"]').send_keys("Cali, CLO - Colombia")
driver.find_element(By.XPATH, '//*[@id="btnItemAutoComplete_0"]').click()

#Ciudad Destino
destino = driver.find_element(By.XPATH, '//*[@id="txtInputDestination_field"]').send_keys("Cartagena de Indias, CTG - Colombia")
driver.find_element(By.XPATH, '//*[@id="btnItemAutoComplete_0"]').click()


elemento_input = driver.find_element(By.XPATH,'//*[@id="departureDate"]').click()

#Fecha ida click 1
ida = driver.find_element(By.XPATH, '//div[contains(strong, "'+mes_ida+'")]/following-sibling::table//td[span[text()="'+day_ida+'"]]')
ida.click()

#Fecha vuvelta clikc 2
vuelta = driver.find_element(By.XPATH, '//div[contains(strong, "'+mes_vuelta+'")]/following-sibling::table//td[span[text()="'+day_vuelta+'"]]')
vuelta.click()

#Buscar
boton_buscar = driver.find_element(By.XPATH, '//*[@id="btnSearchCTA"]')
boton_buscar.click()
time.sleep(7)

# Cambiar al controlador de ventana de la segunda pestaña
driver.switch_to.window(driver.window_handles[1])

element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="CenterWrapperBodyFlights"]/ol/li[1]'))
WebDriverWait(driver, 60).until(element_present)

select = driver.find_element(By.XPATH, '//*[@id="CenterWrapperBodyFlights"]/ol/li[1]')
select.click()