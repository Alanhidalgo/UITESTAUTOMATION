import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup_method")
class TestClassAjax:
    driver: WebDriver

    @pytest.mark.usefixtures("navigate_to_ajax_data")
    def test_ajax_data_appear(self, navigate_to_ajax_data):
        # Validar la URL usando la fixture
        assert self.driver.current_url == navigate_to_ajax_data, (
            f"La URL no es correcta. Se obtuvo: {self.driver.current_url}"
        )
        # Capturar el boton ajax request y hacer las pruebas.
        button = self.driver.find_element(By.ID, "ajaxButton")
        # Validar que este visible y disponible.
        assert button.is_displayed(), (f"El boton no esta visible")
        assert button.is_enabled(), (f"El boton no esta habilitado")

        # Validar hacer click al boton
        button.click()
        # Esperar hasta que aparezca el mensaje de éxito.
        try:
            message = WebDriverWait(self.driver, 16).until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Data loaded with AJAX get request.')]"))
            )
            print(f"Mensaje encontrado: {message.text}")
        except Exception as e:
            pytest.fail(f"El mensaje AJAX no apareció dentro del tiempo esperado: {e}")
        
        # Validar que el mensaje es visible
        assert message.is_displayed(), (f"El mensaje AJAX no es visible.")