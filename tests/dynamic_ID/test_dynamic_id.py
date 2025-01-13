import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures("setup_method")
class TestHomeUIPlayground:
    driver: WebDriver

    @pytest.mark.usefixtures("navigate_to_ui_testing_automation")
    def test_home_page(self):
        assert self.driver.title == "UI Test Automation Playground", "El titulo de la pagina no coincide"
        #print(f"El titulo '{self.driver.title}' de la pagina es correcto")
        #time.sleep(10)

    @pytest.mark.usefixtures("navigate_to_dynamic_id")
    def test_dynamic_id_validate(self, navigate_to_dynamic_id):
         # Validar la URL usando la fixture
        assert self.driver.current_url == navigate_to_dynamic_id, (
            f"La URL no es correcta. Se obtuvo: {self.driver.current_url}"
        )
        # localizar el boton del ID Dinamico
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]"))
        )
        # Validar el texto del boton
        expected_text = "Button with Dynamic ID"
        assert button.text == expected_text, f"El texto del botón no coincide. Se obtuvo: {button.text}"

        # Validar si el boton esta habilitado
        assert button.is_enabled(), "El botón no está habilitado y no se puede hacer clic."
         # Hacer clic en el botón
        button.click()
        print("El botón con ID dinámico fue encontrado, está habilitado y se clickeó exitosamente.")