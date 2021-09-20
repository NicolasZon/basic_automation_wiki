from pages.basepage import BasePage
import unittest
from pyunitreport import HTMLTestRunner


class Article(BasePage):

    def validate_title(self, tittle):
        
        article_title = self.driver.find_element_by_id("firstHeading")
        assert article_title.text.lower() == tittle.lower(), "The title is not the expected"
