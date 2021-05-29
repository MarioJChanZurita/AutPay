from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = webdriver.Chrome("chromedriver.exe")
chrome_driver.get("https://outlook.live.com/owa/?state=1&redirectTo=aHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvc2VudGl0ZW1z")

sign_in = chrome_driver.find_element_by_class_name("internal sign-in-link")
sign_in.click()

time.sleep(2)

email = chrome_driver.find_element_by_id("i0116")
email.send_keys("messi25_mcz@hotmail.com")
email.send_keys(Keys.ENTER)
# next_button = chrome_driver.find_element_by_id("idSIButton9")
# next_button.click()

time.sleep(2)

password = chrome_driver.find_element_by_id("i0118")
password.sen_keys("Jesus2505")
password.send_keys(Keys.ENTER)