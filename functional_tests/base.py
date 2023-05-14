import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    @staticmethod
    def create_user(username, password):
        User = get_user_model()
        User.objects.create_superuser(username=username, password=password)
        return username, password

    def login(self, username, password):
        ADMIN_URL = self.live_server_url + "/admin/"
        self.browser.get(ADMIN_URL)

        username_input = self.browser.find_element(By.XPATH, '//*[@id="id_username"]')
        password_input = self.browser.find_element(By.XPATH, '//*[@id="id_password"]')
        submit = self.browser.find_element(
            By.XPATH, '//*[@id="login-form"]/div[3]/input'
        )
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit.click()

    def create_post(self, title, content):
        title_input = self.browser.find_element(By.XPATH, '//*[@id="id_title"]')
        content_input = self.browser.find_element(By.XPATH, '//*[@id="id_content"]')
        submit = self.browser.find_element(
            By.XPATH, '//*[@id="post_form"]/div/div/input[1]'
        )

        title_input.send_keys(title)
        content_input.send_keys(content)
        submit.click()
