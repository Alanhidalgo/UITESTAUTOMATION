import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup_method")
class TestLoadDelay:
    driver: WebDriver

    @pytest.mark.usefixtures("navigate_to_load_delays")
    def test_load_delays(self, navigate_to_load_delays):
        # Validar la URL usando la fixture
        assert self.driver.current_url == navigate_to_load_delays, (
            f"La URL no es correcta, se obtuvo: {self.driver.current_url}"
        )
        # Valida el titulo de la pagina
        assert self.driver.title == "Load Delays", (
            f"El titulo no es el correcto, se obtuvo: {self.driver.title}"
        )

    @pytest.mark.usefixtures("navigate_to_ui_testing_automation")
    def test_load_delays_home(self):
        load_delay = self.driver.find_element(By. XPATH, "//a[contains(text(),'Load Delay')]")
        load_delay.click()
        # Usar espera explícita para localizar el botón después del retraso
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Button Appearing After Delay')]"))
            )
            
            print(f"el boton aparecio correctamente despues de la carga")
        except Exception as e:
            pytest.fail(f"El botón no apareció dentro del tiempo esperado: {e}")

        # Validar que el botón es visible y habilitado
        assert button.is_displayed(), "El botón no es visible."
        assert button.is_enabled(), "El botón no está habilitado."

         # 4. Hacer clic en el botón
        button.click()
        print("Se hizo clic en el botón correctamente.")