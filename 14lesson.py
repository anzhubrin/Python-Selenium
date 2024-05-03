from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

driver.get("https://www.saucedemo.com/")

driver.add_cookie({
    'name': 'username',
    'value': 'user123'
})
driver.refresh()
print(driver.get_cookies())
driver.delete_cookie('username')
print(driver.get_cookies())
