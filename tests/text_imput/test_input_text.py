import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup_method")
class TestClassInputText:
    driver: WebDriver

    @pytest.mark.usefixtures("navigate_to_text_input")
    def test_input_text(self, navigate_to_text_input, clear_fields):
        # Validar la URL usando la fixture
        assert self.driver.current_url == navigate_to_text_input, (
            f"La URL no es correcta. Se obtuvo: {self.driver.current_url}"
        )
        # Capturar el input
        input_text = self.driver.find_element(By.ID, "newButtonName")
        # Limpia el campo
        clear_fields(input_text)
        # Validar si esta habilitado el input y disponible
        assert input_text.is_displayed(), (f"No esta disponible")
        assert input_text.is_enabled(), (f"No esta habilitado")
        # Capturamos el voton y validamos los pasos anteriones
        button = self.driver.find_element(By.ID, "updatingButton")
        assert button.is_displayed(), (f"No esta disponible el boton")
        assert button.is_enabled(), (f"No esta habilitado el boton")

        # Validar la prueba escribiendo en el input
        input_text.send_keys("Prueba del texto en el boton")
        button.click()
        
        # Usar espera explícita para validar un cambio en el botón o la página
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(
                    (By.ID, "updatingButton"), # localizador del boton
                    "Prueba del texto en el boton"
                )
            )
            print("El texto del botón se actualizó correctamente.")
        except Exception as e:
             pytest.fail(f"El texto del boton no se actualizo dentro del tiempo esperado: {e}")