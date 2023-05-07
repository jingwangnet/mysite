import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ..base import FunctionalTest
from ..const import HOME_TITLE, LOGO_TEXT


class HomePageTest(FunctionalTest):
    def test_home_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn(HOME_TITLE, self.browser.title)

        logo = self.browser.find_element(By.CLASS_NAME, "logo")
        self.assertEqual(logo.text, LOGO_TEXT)

    def test_index_display_posts(self):
        # Creation superuser of jingwang
        username, password = self.create_user("jingwang", "jingwang")
        self.login(username, password)

        # Creation the first post and validation
        self.browser.find_element(By.LINK_TEXT, "Posts").click()
        self.browser.find_element(By.LINK_TEXT, "ADD POST").click()
        first_title = "The first post"
        first_content = "content"
        self.create_post(first_title, first_content)
        self.browser.find_element(By.LINK_TEXT, first_title)

        # Creation the second post and validation
        self.browser.find_element(By.LINK_TEXT, "ADD POST").click()
        second_title = "The second post"
        second_content = "content 2"
        self.create_post(second_title, second_content)
        self.browser.find_element(By.LINK_TEXT, second_title)

        # looking up the both posts in the home_page
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.LINK_TEXT, first_title)
        self.browser.find_element(By.LINK_TEXT, second_title)
