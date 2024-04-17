import time
from selene import browser, have

browser.open("https://www.saucedemo.com/")
# simple css selector
browser.element("#user-name").set_value("standard_user")
# xpath
browser.element("//input[@data-test='password']").set_value("secret_sauce")
# css selector (find 0oi id "login-button" on the page, from class By)
browser.driver.find_elements("id", "login-button")[0].click()
# 1st variant of check
assert browser.driver.current_url == "https://www.saucedemo.com/inventory.html", "Not correct URL"
# 2nd variant of check
browser.element(".title").should(have.text("Products"))
# time.sleep(4)
# browser.driver.refresh()
