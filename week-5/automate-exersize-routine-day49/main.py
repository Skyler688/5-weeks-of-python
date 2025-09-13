from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# for selenium or network error handling
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException
)

import os
import time
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASS = os.getenv("PASS")

retries = 0

def book_class(class_day, class_time, class_name):
    # Checking for valid inputs
    day_check = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    if class_day not in day_check:
        raise Exception(f"Invalid argument for class_day, received -> {class_day}")
    
    if class_time < 0 or class_time > 2300:
        raise Exception(f"Invalid argument for class_time, received -> {class_time}")
    
    name_check = ["spin", "yoga", "hiit", "any"]
    if class_name not in name_check:
        raise Exception(f"Invalid argument for class_name, received -> {class_name}")

    # Extracting todays date from the title.
    title = schedule_page.find_element(By.TAG_NAME, "h1").text
    month = title.split("/")[0].split(" ")[3]
    if len(month) < 2:
        month = "0" + month
    year = title.split("/")[2].replace(")", "")
    
    schedule_groups = schedule_page.find_elements(By.CLASS_NAME, "Schedule_dayGroup__y79__")

    # Find class in the schedule groups
    print("Searching for class...")
    for index, schedule_group in enumerate(schedule_groups):
        # Extract the day from the text in the h2 element
        date = schedule_group.find_element(By.TAG_NAME, "h2").text

        # NOTE -> The string returnd can look like the following Today (Fri, Sep 12), or Sun, Sep 14
        date_raw = date.split("(")
        if len(date_raw) > 1:
            day_of_week = date_raw[1].split(",")[0].lower()
            day = date_raw[1].split(" ")[2].replace(")", "")
        else:
            day_of_week = date_raw[0].split(",")[0].lower()
            day = date_raw[0].split(" ")[2]

        if len(day) < 1:
            day = "0" + day

        # Check if day matches, will not book if today is the class_day
        if (day_of_week == class_day and index != 0):
            if class_name == "any":
                class_options = ["yoga", "spin", "hiit"]
            else:
                class_options = [class_name]

            target_class = None
            for class_ in class_options:
                try:
                    target_class = schedule_group.find_element(By.ID, f"class-card-{class_}-{year}-{month}-{day}-{class_time}")
                    print("Class found")
                    break
                except:
                    None

            if target_class == None:
                print("No class was found matching the arguments passed")
                return # nothing found return to exit the function
            else: 
                # Challenge -> Add smart booking that check's if the state of the class, booked, waitlist, or join.
                # target class names for button state
                # ClassCard_waitlist__F_d1f (join waitlist)
                # ClassCard_booked__cxTZ1 (class booked)
                # ClassCard_available__qnHvf (class available)
                # ClassCard_waitlisted__ExoHW (waiting)
                book_button = target_class.find_element(By.TAG_NAME, "button")

                # Class is available
                if "ClassCard_available__qnHvf" in book_button.get_attribute("class"):
                    book_button.click()
                    print(f"{class_.title()} class booked, for {day_of_week.title()} at {class_time}.")
                    summary["classes_booked"] += 1
                    detailed_list.append(f"* [New Booking] {class_.title()} on {class_day}, {month.title()} {day} at {class_time}")
                # Class is available for waitlist
                elif "ClassCard_waitlist__F_d1f" in book_button.get_attribute("class"):
                    book_button.click()
                    print(f"Joined waitlist for {class_.title()} class, on {day_of_week.title} at {class_time}")
                    summary["waitlists_joined"] += 1
                    detailed_list.append(f"* [New Waitlist] {class_.title()} on {class_day}, {month.title()} {day} at {class_time}")
                # Class is already waitlisted
                elif "ClassCard_waitlisted__ExoHW" in book_button.get_attribute("class"):
                    print(f"{class_.title()} class is waitlisted for {day_of_week.title()} at {class_time}")
                    summary["booked_or_waitlisted"] += 1
                # Class is already booked 
                elif "ClassCard_booked__cxTZ1" in book_button.get_attribute("class"):
                    print(f"{class_.title()} class is already booked, {day_of_week.title()} at {class_time}")  
                    summary["booked_or_waitlisted"] += 1
                else:
                    raise Exception("Failed to find class button state")  
                
                summary["classes_processed"] += 1;    
                break # if the class is found break the for loop
                
        # if today is the target class day dont book any classes
        elif (day_of_week == class_day and index == 0):
            print(f"Today is {class_day}, no classes booked.") 
            return 

while True:
    try:
        summary = {
            "classes_booked": 0,
            "waitlists_joined": 0,
            "booked_or_waitlisted": 0,
            "classes_processed": 0
        }
        detailed_list = []

        if retries > 7:
            raise Exception("Maximum number of retries attempted, quitting program...")

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        # This tells chrome to use the specified path to save data
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://appbrewery.github.io/gym/")

        # ------------- LOGIN ---------------

        # NOTE -> Only need to wait when a new page is loaded, else if the page is static it can be assumed the element is already loaded and ready.
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )
        login_button.click()

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email-input"))
        )
        email_input.send_keys(EMAIL)

        password_input = driver.find_element(By.ID, "password-input")
        password_input.send_keys(PASS)

        submit_button = driver.find_element(By.ID, "submit-button")
        submit_button.click()

        # ------------ BOOK CLASS ------------
        # Challenge -> Find the next Tuesday 6pm class (any type - Yoga, Spin, or HIIT) and Click the "Book Class" or "Join Waitlist" button,
        # then print a success message like: Booked: Spin Class on Tue, Aug 12

        # New page so am waiting for element
        schedule_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "schedule-page"))
        )

        # NOTE -> functions use millatary time so 6pm translates to 18:00
        book_class("tue", 1800, "any")
        book_class("thu", 1800, "any") 


        # Challenge -> Add a script summary to print out a neat summary of what happen'd during the script.
        print("\n\n--- BOOKING SUMMARY ---")
        print(f"Classes booked: {summary['classes_booked']}")
        print(f"Waitlists Joined: {summary['waitlists_joined']}")
        print(f"Already booked/waitlisted: {summary['booked_or_waitlisted']}")
        print(f"Total classes processed: {summary['classes_processed']}\n\n")    
        
        # Detailed list
        print(f"--- DETAILED CLASS LIST ---")
        if len(detailed_list) > 0:
            for detailed_class in detailed_list:
                print(detailed_class)
        else:
            print("* [NONE] No classes where booked or waitlisted")        
        print("\n\n")
        
        # Challenge -> Verify that the bookings have bean made from the my bookings page.
        my_bookings = driver.find_element(By.ID, "my-bookings-link")
        my_bookings.click()

        bookings_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "confirmed-bookings-section"))
        )

        print("--- VERIFYING ON BOOKINGS PAGE ---")
        confirmed_bookings = bookings_section.find_elements(By.CLASS_NAME, "MyBookings_bookingCard__VRdrR")
        for confirmed_booking in confirmed_bookings:
            class_type = confirmed_booking.find_element(By.TAG_NAME, "h3").text
            when = confirmed_booking.find_element(By.TAG_NAME, "p").text

            print(f"- Verified: {class_type} - {when}")

        print(f"\n\n--- VERIFICATION RESULT ---")
        print(f"Expected: {summary['classes_processed']} bookings")
        print(f"Found: {len(confirmed_bookings)} bookings\n")
        
        if (len(confirmed_bookings) == summary["classes_processed"]):
            print("SUCCESS: All bookings verified\n\n")
        else:
            print("FAILED: Invalid bookings detected\n\n")
 
        time.sleep(5)
        driver.quit()
        
    # NOTE -> The corse wanted me to create a retry function to use on each selenium call to do retries,
    # i opted to just use the selenium related exeptions and a global retry. This will quit chrome and try again.
    except (NoSuchElementException, TimeoutException, WebDriverException) as err:
        # if a network or selenuim related ishue happens, try again every 10 sec for a limit of 7 tries.
        print("Selenium error detected, restarting...")
        driver.quit()
        retries += 1
        time.sleep(10)

    except Exception as err:
        # if an actual program error, quit selenium and stop the program
        print("Something went wrong :(")
        print(f"ERROR -> {err}")
        driver.quit()
        break
