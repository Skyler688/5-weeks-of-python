# Chalange scrape the Upcoming Events from the python.org website and place it in a dict, then print out that dict

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# grabing the parent element by XPath because it shares class name and tag with other lists in the html
upcoming_events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

# getting all the li elements from the parent and creating a list of element objects
list_items = upcoming_events.find_elements(By.TAG_NAME, "li")

events = {} 

# looping through all the li objects in the list and appending them to the events dict
for index, item in enumerate(list_items):
    time = item.find_element(By.TAG_NAME, "time")
    name = item.find_element(By.TAG_NAME, "a")
    events[index] = {
        "time": time.text,
        "name": name.text
    }

print(events)    