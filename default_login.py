from selene import browser, have

browser.open("https://www.saucedemo.com/")
browser.element("#user-name").set_value("standard_user")
browser.element("#password").set_value("secret_sauce")
browser.element("#login-button").click()
browser.element(".title").should(have.text("Products"))
