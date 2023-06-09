import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        if os.environ.get("ENV") == "dev":
            cls.browser = webdriver.Chrome()
        else:
            options = Options()
            options.headless = True
            cls.browser = webdriver.Chrome(options=options)

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

    def create_post(self, title, content, *tags):
        title_input = self.browser.find_element(By.XPATH, '//*[@id="id_title"]')
        content_input = self.browser.find_element(By.XPATH, '//*[@id="id_content"]')
        submit = self.browser.find_element(
            By.XPATH, '//*[@id="post_form"]/div/div/input[1]'
        )

        if tags:
            select_tags = self.browser.find_element(By.XPATH, '//*[@id="id_tags"]')
            select = Select(select_tags)
            for tag in tags:
                select.select_by_visible_text(tag)

        title_input.send_keys(title)
        content_input.send_keys(content)
        submit.click()

    def create_page(self, title, url, text):
        title_input = self.browser.find_element(By.XPATH, '//*[@id="id_title"]')
        url_input = self.browser.find_element(By.XPATH, '//*[@id="id_url"]')
        text_input = self.browser.find_element(By.XPATH, '//*[@id="id_text"]')
        submit = self.browser.find_element(
            By.XPATH, '//*[@id="page_form"]/div/div/input[1]'
        )

        title_input.send_keys(title)
        url_input.send_keys(url)
        text_input.send_keys(text)
        submit.click()
