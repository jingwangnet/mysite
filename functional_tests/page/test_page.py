from ..base import FunctionalTest
from ..const import ABOUT_TITLE
from selenium.webdriver.common.by import By


class PageViewTest(FunctionalTest):
    def test_about_page(self):
        self.browser.get(self.live_server_url)
        about_page = self.browser.find_element(By.LINK_TEXT, "about me")
        about_page.click()

        self.assertEqual(ABOUT_TITLE, self.browser.title)
