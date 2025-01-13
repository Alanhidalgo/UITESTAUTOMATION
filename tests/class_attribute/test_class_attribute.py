import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup_method")
class TestClassAttribute:
    driver: WebDriver

    @pytest.mark.usefixtures("navigate_to_class_attribute")
    def test_class_attribute(self, navigate_to_class_attribute):
         # Validar la URL usando la fixture
         assert self.driver.current_url == navigate_to_class_attribute, (
              f"La URL no es correcta. Se obtuvo: {self.driver.current_url}"
         )
         # Validar el titulo de la pagina.
         assert self.driver.title == "Class Attribute", "El titulo de la pagina no coincide"

         # Escenario: Validar el boton azul y presionar ok en la alerta.
         # Localizar los botones
         buttons = self.driver.find_elements(By.TAG_NAME, "button")
         # Validar que los botones son visibles y están habilitados
         for button in buttons:
            # Obtener el texto y la clase del botón para identificarlo mejor
            button_text = button.text.strip()
            button_class = button.get_attribute("class") # Obtener la clase para identificar el color

             # Ignorar botones irrelevantes basados en atributos
            if not button.is_displayed() or button_class == "navbar-toggler":
               print(f"Ignorando el botón '{button_text}' con clase '{button_class}'.")
               continue

            assert button.is_displayed(), (
                f"El boton '{button_text}' con clase '{button_class}' no es visible."
            )
            assert button.is_enabled(), (
                f"El boton '{button_text}' con su clase '{button_class}' no esta habilitado."
            )
            print(f"El boton '{button_text}' con clase '{button_class}' es visible y habilitado.")

             # Si el botón es el botón azul, simular clic y manejar la alerta
            if "btn-primary" in button_class: # Clase del boton azul
                button.click()
                WebDriverWait(self.driver, 5).until(
                    EC.alert_is_present()
                )
                alert = self.driver.switch_to.alert
                print(f"Alerta encontrada con texto: {alert.text}")
                alert.accept()
                print(f"Alerta cerrada.")