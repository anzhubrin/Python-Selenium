from selene import browser, have

browser.open("https://demoqa.com/text-box")

browser.element("#userName").set_value("And")
browser.element("#userEmail").set_value("and@mail.ru")
browser.element("#currentAddress").set_value("Lenina 1")
browser.element("#permanentAddress").set_value("No")
browser.element("//button[@id='submit']").click()

browser.element("//div[contains(@class, 'col-md-12')]").should(have.text("And"))
browser.element("//div[contains(@class, 'col-md-12')]").should(have.text("and@mail.ru"))
browser.element("//div[contains(@class, 'col-md-12')]").should(have.text("Lenina 1"))
browser.element("//div[contains(@class, 'col-md-12')]").should(have.text("No"))
