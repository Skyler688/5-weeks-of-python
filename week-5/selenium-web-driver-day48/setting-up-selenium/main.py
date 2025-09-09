from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# To keep chrome open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/ref=sr_1_1?crid=QFJMW3EQTNE9&dib=eyJ2IjoiMSJ9.EtIvgEdcfrulD7Yb3iGe3B6eMjzSidKaYvbN7n8SZTsChfBO3qr80VEtARDlMQaOEgXjbyQq_lmY4M0TJSsBDtu6tzcxXglY89WiJjXGkJyJgfbj2v4mUt6AkCnnopzL9uBnQ47Dxn-rLxQb6w51G7EG2L9c2JAL360ci4nv8KKCrEnPjfPd38Sdu9xKO3y8l6lAYiG0ski6LLBebdU8fIDqJB4mxMGKf5zi2ghyKyY.MWN4k_svjICiuwaTRlr3bEJapvXhBqVF8TF-O520C94&dib_tag=se&keywords=instant%2Bpot&qid=1757082819&sprefix=insta%2Caps%2C138&sr=8-1&th=1")

# Amazon puts a continue shoping page when using the bot, this code clicks that button
continue_shopping = driver.find_element(By.CLASS_NAME, value="a-button-text")
continue_shopping.click()
# waiting 5 seconds to allow the html to load
sleep(5)

# grabing the price of the amazon listing from the html using the class name selector
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is ${price_dollar.text}.{price_cents.text}")

# grabing elements by XPath, and grabing attributes
reveiws = driver.find_element(By.XPATH, '//*[@id="acrCustomerReviewLink"]')
reveiws_link = reveiws.get_attribute("href")

print(reveiws_link)

# closes the tab
# driver.close() 

# closes the entire browser instance
driver.quit()
