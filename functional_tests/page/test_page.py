from ..base import FunctionalTest
from ..const import ABOUT_TITLE
from selenium.webdriver.common.by import By
import time


class PageViewTest(FunctionalTest):
    def test_about_page(self):
        username, password = self.create_user("jingwang", "jingwang")
        self.login(username, password)

        # Creation the first post and validation
        self.browser.find_element(By.LINK_TEXT, "Pages").click()
        self.browser.find_element(By.LINK_TEXT, "ADD PAGE").click()
        title = "about me"
        url = "about-me"
        text = "content"

        self.create_page(title, url, text)

        self.browser.get(self.live_server_url)
        about_page = self.browser.find_element(By.LINK_TEXT, "about me")
        about_page.click()
        self.assertEqual(ABOUT_TITLE, self.browser.title)
