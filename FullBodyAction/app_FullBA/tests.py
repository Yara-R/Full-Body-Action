import os
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
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_gyms(self):
        self.driver.get(self.live_server_url + '/academias/')
        self.driver.quit()

    def test_login(self):
        self.driver.get(self.live_server_url + '/login/')

        input_email = self.driver.find_element(By.NAME, 'email')
        input_email.send_keys('usuario@teste.com')

        input_senha = self.driver.find_element(By.NAME, 'password')
        input_senha.send_keys('123456')

        enviar = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        enviar.click()

        self.assertIn(self.live_server_url + '/', self.driver.current_url)

    def test_cadastro(self):
        self.driver.get(self.live_server_url + '/cadastro/')

        input_nome = self.driver.find_element(By.NAME, 'name')
        input_nome.send_keys('usuario')

        input_email = self.driver.find_element(By.NAME, 'email')
        input_email.send_keys('usuario@teste.com')

        input_senha = self.driver.find_element(By.NAME, 'password')
        input_senha.send_keys('123456')

        enviar = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        enviar.click()

    def test_comentario(self):
        self.driver.get(self.live_server_url + '/biceps_rosca_com_barra/')

        input_nome = self.driver.find_element(By.NAME, 'autor')
        input_nome.send_keys('usuario')

        input_comentario = self.driver.find_element(By.NAME, 'texto')
        input_comentario.send_keys('abcd')

        enviar = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        enviar.click()
