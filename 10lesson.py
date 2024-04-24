from selene import browser, have

browser.open("https://demoqa.com/upload-download")
browser.element("#uploadFile").set_value("/Users/and1qa/PyCharmProjects/Python-Selenium/files/Allure.png")
browser.element("#uploadedFilePath").should(have.text("Allure.png"))
