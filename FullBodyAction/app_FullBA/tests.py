from selenium import webdriver
from django.test import LiveServerTestCase

# Create your tests here.
class TestHome(LiveServerTestCase):
    browser = webdriver.Chrome()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        assert "The install worked" in self.browser.title


class TestAcademia(LiveServerTestCase):
        def test_gym(self):
            driver = webdriver.Chrome()
            driver.get('http://127.0.0.1:8000//academias/')
            driver.quit()

class TestEntrar(LiveServerTestCase):
        def test_login(self):

            driver = webdriver.Chrome()
            driver.get('http://127.0.0.1:8000//login/')
            
            input_email = driver.find_element_by_name('email')
            input_email.send_keys('usuario@teste.com')

            input_senha = driver.find_element_by_name('password')
            input_senha.send_keys('123456')

            enviar = driver.find_element_by_xpath('//button[@type="submit"]')
            enviar.click()

            self.assertIn('http://http://127.0.0.1:8000/', driver.current_url)

            cadastrar = driver.find_element_by_xpath('//button[@type="submit"]')
            cadastrar.click()
            
            driver.quit()

        def test_cadastro(self):

            driver = webdriver.Chrome()
            driver.get('http://127.0.0.1:8000//cadastro/')
            
            input_nome = driver.find_element_by_name('name')
            input_nome.send_keys('usuario')

            input_email = driver.find_element_by_name('email')
            input_email.send_keys('usuario@teste.com')

            input_senha = driver.find_element_by_name('password')
            input_senha.send_keys('123456')

            enviar = driver.find_element_by_xpath('//button[@type="submit"]')
            enviar.click()

            driver.quit()

class TestAvaliar(LiveServerTestCase):
        def test_comentario(self):

            driver = webdriver.Chrome()
            driver.get('http://127.0.0.1:8000//biceps_rosca_com_barra/')
            
            input_nome = driver.find_element_by_name('autor')
            input_nome.send_keys('usuario')

            input_comentario = driver.find_element_by_name('texto')
            input_comentario.send_keys('abcd')

            enviar = driver.find_element_by_xpath('//input[@type="submit"]')
            enviar.click()
            
            driver.quit()