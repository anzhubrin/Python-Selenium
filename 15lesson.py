from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/selectable")
driver.find_element(By.XPATH, "//a[@id='demo-tab-grid']").click()
driver.find_element(By.XPATH, "//div[@id='row1']/li[1]").click()
driver.find_element(By.XPATH, "//div[@id='row1']/li[2]").click()

driver.find_element(By.XPATH, "//div[@id='row1']/li[1]").get_attribute("active")
driver.find_element(By.XPATH, "//div[@id='row1']/li[2]").get_attribute("active")
