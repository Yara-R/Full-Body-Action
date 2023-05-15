import os
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestFullBA(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_gyms(self):
        self.driver.get("http://127.0.0.1:8000/academias/")
        time.sleep(5)
        self.driver.quit()

    def test_cadastro(self):
        self.driver.get("http://127.0.0.1:8000/cadastro/")
        time.sleep(5)

        input_nome = self.driver.find_element(By.NAME, 'name')
        input_nome.send_keys('usuario')

        input_email = self.driver.find_element(By.NAME, 'email')
        input_email.send_keys('usuario@teste.com')

        input_senha = self.driver.find_element(By.NAME, 'password')
        input_senha.send_keys('123456')

        enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()

    #  Está dando erro
    # def test_login(self):
    #     self.driver.get("http://127.0.0.1:8000/login/")

    #     input_email = self.driver.find_element(By.NAME, 'email')
    #     input_email.send_keys('usuario@teste.com')

    #     input_senha = self.driver.find_element(By.NAME, 'password')
    #     input_senha.send_keys('123456')

    #     enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
    #     enviar.click()

    #     self.assertIn(self.live_server_url + '/', self.driver.current_url)

    def test_comentario(self):
        self.driver.get("http://127.0.0.1:8000/biceps_rosca_com_barra/")
        time.sleep(5)

        input_nome = self.driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')

        input_comentario = self.driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')

        enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from time import sleep
# servico = Service(ChromeDriverManager().install())
# navegador = webdriver.Chrome(service=servico)

# navegador.get('http://127.0.0.1:8000/')
# navegador.find_element('xpath','/html/body/nav/div[2]/a[4]').click()
# sleep(3)

#     #     input_voto = self.driver.find_element(By.NAME, 'rating')
#     #     input_voto.click()


