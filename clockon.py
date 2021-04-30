#!/usr/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://microkeeper.com.au/login.php")
username = driver.find_element_by_id("username")
username.clear()
username.send_keys("USERNAME GOES HERE")
password = driver.find_element_by_id("password")
password.clear()
password.send_keys("PASSWORD GOES HERE")
password.send_keys(Keys.ENTER)

actions = ActionChains(driver)
clockon = driver.find_element_by_xpath("//input[@value='Clock on']")
actions.move_to_element(clockon)
actions.click(clockon)
actions.perform()

time.sleep(3)

driver.close()
