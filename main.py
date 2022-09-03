# Imports
import os
from selenium import webdriver

# Own modules
from utils.cookies_handling import accept_cookies
from utils.leasing_calculator import calculate_leasing

# Add path to the chrome driver (Linux specific)
os.environ['PATH'] += ":" + os.getcwd() + r"/.drivers/"


def run_first_test(broswer):

    # Start web browser
    if broswer.lower() == "chrome":
        driver = webdriver.Chrome()
    elif broswer.lower() == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    # Visit webpage
    driver.get("http://bikeleasing.de")
    # Wait 1 second to load the page
    driver.implicitly_wait(2)
    # Accept cookies
    accept_cookies(driver)
    driver.implicitly_wait(2)
    # Calculate Leasing for 1000€
    calculate_leasing(driver)


#run_first_test("Firefox")
run_first_test("Chrome")

