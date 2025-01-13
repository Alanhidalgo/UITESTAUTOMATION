import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup_method")
class TestHomeGoogle:
    driver: WebDriver

    @pytest.mark.usefixtures("navigate_to_google")
    def test_homepage_google(self):
        assert self.driver.title == "Google", "El titulo de la pagina no coincide"
        #print(f"El titulo '{self.driver.title}' de la pagina es correcto")