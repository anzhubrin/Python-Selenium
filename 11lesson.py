import time

from selene import browser, have

browser.open("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
browser.element("#populate-text").click()
time.sleep(12)
browser.element("#h2").should(have.text("Selenium Webdriver"))

browser.element("#display-other-button").click()
time.sleep(12)
browser.element("#hidden").should(have.text("Enabled"))
