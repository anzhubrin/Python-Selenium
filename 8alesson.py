from selene import browser, have

browser.open("https://the-internet.herokuapp.com/status_codes")
browser.element("//a[contains(text(), '200')]").click()
assert browser.driver.current_url == "https://the-internet.herokuapp.com/status_codes/200"
