from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")
# assert "Python" in driver.title
elem = driver.find_element(By.CLASS_NAME, "fc-button")
# elem.clear()
# elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(2)
elem = driver.find_element(By.ID, "langSelect-PL")
print(elem)
elem.click()
time.sleep(2)

elem = driver.find_element(By.ID, "bigCookie")
while(True):
    elem = driver.find_element(By.ID, "bigCookie")

    elem.send_keys(Keys.RETURN)
    elem2 = driver.find_element(By.XPATH, "//*[@id='cookies']")
    print(elem2.get_property("value"))
    # elem =
    # if elem.
assert "No results found." not in driver.page_source
# driver.close()

