import time

from selene import browser
from selenium import webdriver


def test_text_in_downloaded_file_by_click():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": r"/Users/and1qa/PyCharmProjects/Python-Selenium/files",
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

    browser.open("https://the-internet.herokuapp.com/download")
    browser.element("//a[@href='download/test.txt']").click()