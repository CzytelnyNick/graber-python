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
    elem2 = driver.find_element(By.ID, "bigCookie")
    prod = driver.find_element(By.ID, "product0")
   
    elem.send_keys(Keys.RETURN)
    prodValue = driver.find_element(By.ID, "productOwned0")
    
    if(prod.get_attribute("class") == "product unlocked enabled"):
            # print()
            driver.find_element(By.ID, "product0").click()
            
            if int(prodValue.text) == 10:
                time.sleep(10)
                prod = driver.find_element(By.ID, "product1")
                prodValue = driver.find_element(By.ID, "productOwned1")

            
    
    # i = 0;  
    # elem2 = driver.find_element(By.CLASS_NAME, "")
        
        
    # print(elem2.get_attribute("innerHTML")[0])
    # elem =
    # if elem.
assert "No results found." not in driver.page_source
# driver.close()

