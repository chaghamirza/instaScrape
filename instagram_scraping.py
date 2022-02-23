from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(r"Documents/selenium/chromedriver")
driver.get(r"https://instagram.com")


username = driver.find_element_by_name("username")
username.send_keys("")

time.sleep(0.5)

password = driver.find_element_by_name("password")
password.send_keys("")

time.sleep(1)

driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()

time.sleep(2)