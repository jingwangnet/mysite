from selenium.webdriver.common.by import By
from ..base import FunctionalTest
from ..const import HOME_TITLE, LOGO_TEXT


class HomePageTest(FunctionalTest):
    def test_home_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn(HOME_TITLE, self.browser.title)

        logo = self.browser.find_element(By.CLASS_NAME, "logo")
        self.assertEqual(logo.text, LOGO_TEXT)
