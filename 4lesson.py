from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

PAGE_TITLE = driver.title
print(PAGE_TITLE)
assert driver.title == "Swag Labs", "The page is opened"

driver.refresh()

assert driver.current_url == "https://www.saucedemo.com/"
