from pages.home import Home
from behave import *


@given('Open wikipedia')
def open_wiki(context):
    context.home_page = Home(context.driver)
    context.home_page.open_home_page()


@when('I search for "{article}"')
def search_on_wiki(context, article):
    context.article = context.home_page.search_article(article)


@then('I can see "{article}"')
def article(context, article):
    context.article.validate_title(article)
