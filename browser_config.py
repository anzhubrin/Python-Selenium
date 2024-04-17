from selene import browser, have

from selenium import webdriver

driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--headless')
browser.config.driver_options = driver_options

browser.open("https://www.saucedemo.com/")
browser.element("#user-name").set_value("standard_user")
browser.element("#password").set_value("secret_sauce")
browser.element("#login-button").click()
browser.element(".title").should(have.text("Products"))

# "--headless"
# "--incognito"
# "--ignore-certificate-errors"
# "--window-size=X,Y"
# "--disable-cache"
