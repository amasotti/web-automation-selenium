
def calculate_leasing(driver):
    # Go to the subpage /leasingrechnert/arbeitnehmer
    driver.get("https://www.bikeleasing.de/leasingrechner/arbeitnehmer")
    bike_price = driver.find_element_by_id("bikeleasing_totalPrice-0")
    bike_price.clear()
    bike_price.send_keys("1000")
    driver.find_element_by_id("calculateLeasing-0").click()
    print("Leasing calculated with 1000€ bike price")
    net_costs = driver.find_element_by_xpath("//span[@data-result='netCost']")
    # scroll to net_costs
    driver.execute_script("window.scrollBy(0, 600);")

    if net_costs.text == "17,73":
        print("Test passed: Für 1000€ Kaufpreis mit default Bedienung ergibt sich ein Netto-Leasingpreis von 17,73€")
    else:
        print("Test failed")
        raise Exception("Test failed: Für 1000€ Kaufpreis mit default Bedienung ergibt sich ein Netto-Leasingpreis von 17,75€ -- Erwartet: 17,73€")





