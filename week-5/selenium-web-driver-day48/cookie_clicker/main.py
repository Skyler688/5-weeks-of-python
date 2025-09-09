# Challange -> make a bot that playes cookie clicker automaticaly puchasing upgrades

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

# function to strip out the comas and return a int
def filter_num(num_text):
    split_num = num_text.split(",")
    num_string = ""
    for num_peace in split_num:
        num_string += num_peace

    return int(num_string)

try:

    start_time = datetime.now()
    product_pull_delay = 5
    
    while True:
        
        game_time = datetime.now()
        
        # after 5 minutes stop the bot
        if game_time >= start_time + timedelta(minutes=5):
            break

        # waits for the cookie to be clickable for a max of 10 seconds
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "bigCookie"))
        )
        cookie_button.click()


        # grab the unlocked products every 5 seconds, if it fails create a empty array 
        if game_time >= start_time + timedelta(seconds=product_pull_delay):
            product_pull_delay += 5 # add 5 more seconds to the delay
            
            # waits for the score to be redable
            cookies = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "cookies"))
            )

            # extract the score from cookies
            score_raw = cookies.text.split()[0]
            
            score = filter_num(score_raw)

            try:
                products = driver.find_elements(By.CLASS_NAME, "unlocked")
            except:
                products = []    

            # find the index of the highest avalable product to purchas
            purchase_index = -1
            for index, product in enumerate(products):
                price = product.find_element(By.CLASS_NAME, "price")
                if score >= filter_num(price.text):
                    purchase_index = index

            # if a item is avlable purchace the highest value one 
            if purchase_index != -1 and len(products) > 0:
                products[purchase_index].click() 
         

    cookies_per_sec = cookies.find_element(By.TAG_NAME, "div")

    per_sec = float(cookies_per_sec.text.split(":")[1])
    print(f"You have {per_sec} cookies per second")

    driver.quit()
except:
    print("Somthing went wrong :(")
    driver.quit()            