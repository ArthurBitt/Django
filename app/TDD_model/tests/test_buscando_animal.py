from django.test import TestCase, LiveServerTestCase, RequestFactory

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class AnimaisBuscaTestCase(LiveServerTestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_buscando_novo_animal(self):
        home_page = self.driver.get(self.live_server_url + '/')
        '''teste unitário para buscar input do animal'''

        brand_element = self.driver.find_element(by=By.CLASS_NAME, value='navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        buscar_animal_input = self.driver.find_element(by=By.ID,
                                                       value='buscar-animal')

        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: Leão')

        buscar_animal_input.send_keys('leão')
        time.sleep(2)
        self.driver.find_element(by=By.CLASS_NAME, value='form-button')


        caracteristicas = self.driver.find_elements(by=By.CLASS_NAME, value='results-caracteristicas')
        self.assertGreater(len(caracteristicas),3)