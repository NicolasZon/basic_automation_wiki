from pages.article import Article
from re import search

from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class Home(BasePage):

    def open_home_page(self):
        self.driver.get("https://www.wikipedia.com")


    def search_article(self, article_to_search):
        search_input = self.driver.find_element_by_id("searchInput")
        search_input.send_keys(article_to_search)
        search_button = self.driver.find_element_by_xpath('//button[@class="pure-button pure-button-primary-progressive"]')
        search_button.click()
        return Article(self.driver)
        
