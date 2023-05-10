from selenium import webdriver
from django.test import LiveServerTestCase

# Create your tests here.
class TestHome(LiveServerTestCase):
    browser = webdriver.Chrome()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        assert "The install worked" in self.browser.title

    def test_abrir_perfil(self):
        self.browser.get("")
        perfil = self.browser.find.element(By.CLASS_NAME, 'menu-item')
        assert perfil.get_atribute('herf') == "{% url 'perfil' %}"
        
'''
    def test_link(self):
        self.browser.get('')
        logo = self.browser.find.element(By.CLASS_NAME, 'logo')
        assert logo.get_atribute('herf') == ""
        
'''