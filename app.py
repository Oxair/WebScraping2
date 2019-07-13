from selenium import webdriver
from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    author = input("Enter the author: ")
    tag = input("Enter your tag: ")

    chrome= webdriver.Chrome(executable_path="chromedriver\chromedriver.exe")
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))

except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("Try again. Unknown error.")