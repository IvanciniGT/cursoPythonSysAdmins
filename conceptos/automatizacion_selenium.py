from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# 1º Configurar driver (que navegador? otras configuraciones? perfil, headless)
configuracion_navegador = Options()
configuracion_navegador.headless = True
# 2º Abrir un navegador
navegador=webdriver.Firefox(executable_path='../geckodriver', options=configuracion_navegador )
# 3º Hago operaciones en él
#navegador.get("https://google.es")
navegador.get("http://www.itnow.es/")
navegador.implicitly_wait(10)
print(navegador.title)
# Buscar un elemento en la página que hemos cargado. A través de XPATH (usando el atributo name o el id)
#navegador.find_element_by_xpath("//input[@name='q']").send_keys("ITNOW"+ Keys.ENTER)
#print(navegador.find_element_by_xpath("//div[@id='result-stats']").text)

#print(navegador.find_element_by_xpath("//*[@id='rso']//cite").text)
#navegador.find_element_by_xpath("//*[@id='rso']//a").click()
#print(navegador.title)

print(navegador.find_element_by_xpath('//div[@id="footer"]//a[1]').text)
navegador.find_element_by_xpath('//*[@id="ctl00_SelectorVariaciones1_varCA"]').click()
print(navegador.find_element_by_xpath('//div[@id="footer"]//a[1]').text)
print(navegador.find_element_by_xpath('//body').text)
    # Realizar una operación sobre él
# 4º Cierro el navegador
navegador.quit()