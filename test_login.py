import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

with open("results.txt", "w") as log:

    with open("test_data.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:

            username = row["username"]
            password = row["password"]

            driver.get("https://practicetestautomation.com/practice-test-login/")

            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "submit").click()

            time.sleep(2)

            if "Logged In Successfully" in driver.page_source:
                result = f"{username} : PASS"
            else:
                result = f"{username} : FAIL"

            print(result)
            log.write(result + "\n")

driver.quit()

print("Testing Completed")
