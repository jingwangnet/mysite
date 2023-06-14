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
        first_title = "第一篇博文"
        first_content = "content"
        self.create_post(first_title, first_content)
        self.browser.find_element(By.LINK_TEXT, first_title)

        # Creation the second post and validation
        self.browser.find_element(By.LINK_TEXT, "ADD POST").click()
        second_title = "第二篇博文"
        second_content = "content 2"
        self.create_post(second_title, second_content)
        self.browser.find_element(By.LINK_TEXT, second_title)

        # looking up the both posts in the home_page
        self.browser.get(self.live_server_url)
        first_post_url = self.browser.find_element(By.LINK_TEXT, first_title)
        first_post_url.click()
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn(first_title, body_text)
        self.assertIn(first_content, body_text)

        logo_url = self.browser.find_element(By.LINK_TEXT, LOGO_TEXT)
        logo_url.click()

        second_post_url = self.browser.find_element(By.LINK_TEXT, second_title)
        second_post_url.click()
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn(second_title, body_text)
        self.assertIn(second_content, body_text)

    def test_add_post_with_tags_and_display_tags_in_the_website(self):
        username, password = self.create_user("jingwang", "jingwang")
        self.login(username, password)

        ## Create first tag
        self.browser.find_element(By.LINK_TEXT, "Tags").click()
        self.browser.find_element(By.LINK_TEXT, "ADD TAG").click()

        tag_input = self.browser.find_element(By.XPATH, '//*[@id="id_tag"]')
        tag_text_1 = "test_tag_1"
        tag_input.send_keys(tag_text_1)
        tag_input.send_keys(Keys.ENTER)
        self.browser.find_element(By.LINK_TEXT, tag_text_1)

        ## Create second tag
        self.browser.find_element(By.LINK_TEXT, "ADD TAG").click()
        tag_input = self.browser.find_element(By.XPATH, '//*[@id="id_tag"]')
        tag_text_2 = "test_tag_2"
        tag_input.send_keys(tag_text_2)
        tag_input.send_keys(Keys.ENTER)
        self.browser.find_element(By.LINK_TEXT, tag_text_2)

        ## Create a blog
        ## back home page of admin
        self.browser.find_element(By.LINK_TEXT, "Home").click()

        self.browser.find_element(By.LINK_TEXT, "Posts").click()
        self.browser.find_element(By.LINK_TEXT, "ADD POST").click()
        first_title = "第一篇博文"
        first_content = "content"
        self.create_post(first_title, first_content, tag_text_1, tag_text_2)

        self.browser.get(self.live_server_url)

        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertIn(tag_text_1, body_text)
        self.assertIn(tag_text_2, body_text)
