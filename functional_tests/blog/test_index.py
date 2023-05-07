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
        username, password = self.create_user("jingwang", "jingwang")
        self.login(username, password)

        self.browser.find_element(By.LINK_TEXT, "Posts").click()
        self.browser.find_element(By.LINK_TEXT, "ADD POST").click()

        title = "The first post"
        content = "content"
        self.create_post(title, content)
        self.browser.find_element(By.LINK_TEXT, title)

        self.browser.find_element(By.LINK_TEXT, "ADD POST").click()
        title = "The second post"
        content = "content 2"
        self.create_post(title, content)
        self.browser.find_element(By.LINK_TEXT, title)

        time.sleep(5)
        self.browser.get(self.live_server_url)
