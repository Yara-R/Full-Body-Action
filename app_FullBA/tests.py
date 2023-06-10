import os
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)


class TestHome(LiveServerTestCase):
    def test_title(self):
        driver.get('http://127.0.0.1:8000/')
        assert "The install worked" in driver.title

