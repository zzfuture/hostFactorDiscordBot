from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Función para determinar el estado del servidor y obtener la dirección IP
def obtener_estado_servidor(html):
    soup = BeautifulSoup(html, 'html.parser')
    etiqueta_estado = soup.find('div', class_='ui small bottom right attached label')
    if etiqueta_estado and 'Stopped' in etiqueta_estado.text:
        return 'Apagado'
    etiqueta_ip = soup.find('div', class_='center aligned content')
    if etiqueta_ip:
        ip = etiqueta_ip.find_next('div').text.strip()  # Obtener el texto del siguiente elemento div
        return f'Funcionando (IP: {ip})'
    
    return 'Estado desconocido'

def server():
    # Configura las opciones de Chrome para el modo headless
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Activa el modo headless

    # Crea una instancia del controlador de Chrome con las opciones configuradas
    driver = webdriver.Chrome(options=chrome_options)

    # Credenciales
    usuario = "ikerfdoas@gmail.com"
    contraseña = "1975jeIE"

    # Abre la página web
    driver.get("https://hostfactor.io/")  # Reemplaza con la URL real de tu sitio web

    # Espera a que aparezca el botón "Log In"
    wait = WebDriverWait(driver, 20)
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Log In')]")))

    # Haz clic en el botón "Log In" para abrir el popup
    login_button.click()

    # Espera a que aparezca el campo de entrada de usuario en el popup
    username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']")))

    # Ingresa el nombre de usuario
    username_input.send_keys(usuario)

    # Espera un momento para asegurarse de que el nombre de usuario se haya ingresado correctamente (opcional)
    import time
    time.sleep(2)  # Espera 2 segundos (puede variar según la velocidad de carga del sitio)

    # Ingresa la contraseña en el popup (usando clases)
    password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
    password_input.send_keys(contraseña)

    # Encuentra el botón para enviar el formulario de inicio de sesión
    login_submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")

    # Haz clic en el botón para enviar el formulario de inicio de sesión
    login_submit_button.click()

    # Espera a que se complete el inicio de sesión (opcional, usando clases) By.XPATH, "//div[contains(text(), 'Stopped')]"
    time.sleep(3)
    
    # Espera a que aparezcan las "cards"
    cards_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ui.cards .ui.card"))
    )

    # Hacer clic en la primera "card" para abrir el popup
    cards_elements[0].click()

    # Esperar a que aparezca el botón "Start" en el popup (aumentamos el tiempo de espera)
    
    # Obtener el outerHTML de la primera "card"
    time.sleep(10)
    html_del_elemento = cards_elements[0].get_attribute("outerHTML")

    # Prueba con los dos fragmentos de HTML
    estado_funcionando = obtener_estado_servidor(html_del_elemento)
    print(estado_funcionando)
    if estado_funcionando == 'Apagado' : 
        if int(input('Quieres inciar el servidor?: \n1. Si\n0.No\n')) == 1:
            print('Server inciandose...')
            try:
                start_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Start')]"))
                )
                # Hacer clic en el botón "Start"
                start_button.click()
            except Exception:
                j = 0
            server()
    # Cierra el navegador cuando hayas terminado
    driver.quit()
server()
