from django.test import LiveServerTestCase
from selenium import webdriver

# Create your tests here.
class TestHome(LiveServerTestCase):
    browser = webdriver.Chrome()

    def test_title(self):
        self.browser.get('')
        assert "The install worked" in self.browser.title

    def test_link(self):
        self.browser.get('')