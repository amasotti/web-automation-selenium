def accept_cookies(driver) -> bool:
    """
    Accept cookies on the webpage (based on the Bikeleasing Implementation of cookieFirst)

    :param driver: Selenium webdriver

    :return: True if cookies were accepted, False if not

    """

    # See if we need to accept cookies
    cookie_banner = driver.find_element_by_id("cookiefirst-root")
    if not cookie_banner:
        print("No cookie banner found")
        return True

    # Accept cookies
    cookie_banner.find_element_by_xpath("//button[@data-cookiefirst-action='accept']").click()

    print("Cookies accepted")
    return True
