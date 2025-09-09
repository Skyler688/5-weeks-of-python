# Chalange -> fill out and submit the form from the website provided by the course resorces

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
submit = driver.find_element(By.CLASS_NAME, "btn")

first_name.send_keys("Skyler")
last_name.send_keys("Clark")
email.send_keys("notarealemail@gmail.com")

submit.click()
