import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Navegador para las pruebas: chrome o firefox")

@pytest.fixture(scope="class")
def setup_method(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = ChromeOptions()
        # Descomentar la siguiente línea para ejecutar en modo headless (sin interfaz gráfica)
        # options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    else:
        raise ValueError(f"Navegador no soportado: {browser}")
    
    driver.maximize_window()  # Maximiza la ventana del navegador

    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)  # Espera explícita configurada a 10 segundos
    yield driver
    driver.quit()

# Limpieza de campos para manejar tanto listas como elementos individuales
@pytest.fixture(scope="session")
def clear_fields():
    def _clear_fields(fields):
        # Si se pasa un único elemento en lugar de una lista
        if isinstance(fields, WebElement):
            fields = [fields]  # Convierte el elemento en una lista
        for field in fields:
            if field.get_attribute("value"):
                field.clear()
    return _clear_fields

# fixture para navegar a google.com
@pytest.fixture
def navigate_to_google(request):
    # Usa el driver que está en request.cls.driver
    request.cls.driver.get("https://www.google.com/")  

# fixture para navegar a UI Test Automation
@pytest.fixture
def navigate_to_ui_testing_automation(request):
    # Usa el driver que está en request.cls.driver
    request.cls.driver.get("http://uitestingplayground.com/")

# fixture para navegar a UI Test Automation - sección dynamic ID
@pytest.fixture
def navigate_to_dynamic_id(request):
    # Usa el driver que está en request.cls.driver
    url = "http://uitestingplayground.com/dynamicid"
    request.cls.driver.get(url)
    return url

# fixture para navegar a UI Test Automation - Class Attribute
@pytest.fixture
def navigate_to_class_attribute(request):
    # Usa el driver que está en request.cls.driver
    url = "http://uitestingplayground.com/classattr"
    request.cls.driver.get(url)
    return url

# fixture para navegar a UI Test Automation - load delays
@pytest.fixture
def navigate_to_load_delays(request):
    # Usa el driver que está en request.cls.driver
    url = "http://uitestingplayground.com/loaddelay"
    request.cls.driver.get(url)
    return url

# fixture para navegar a UI Test Automation - ajax data
@pytest.fixture
def navigate_to_ajax_data(request):
    # Usa el driver que está en request.cls.driver
    url = "http://uitestingplayground.com/ajax"
    request.cls.driver.get(url)
    return url

# fixture para navegar a UI Test Automation - textinput
@pytest.fixture
def navigate_to_text_input(request):
    # Usa el driver que está en request.cls.driver
    url = "http://uitestingplayground.com/textinput"
    request.cls.driver.get(url)
    return url