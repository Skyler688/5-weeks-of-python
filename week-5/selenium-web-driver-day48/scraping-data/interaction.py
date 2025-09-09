# Challange grab the total articles from the wikipidia home page and print it to the terminal

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')

print(total_articles.text)

# NOTES

# Finding a link by the links text
login = driver.find_element(By.LINK_TEXT, "Log in")
# login.click()

# finding a input by name
search = driver.find_element(By.NAME, "search")

# sending keyboard input using the Keys class
search.send_keys("Python", Keys.ENTER)