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
time.sleep(4)
elem = driver.find_element(By.ID, "langSelect-PL")
print(elem)
elem.click()
time.sleep(2)

elem = driver.find_element(By.ID, "bigCookie")
i = 0
prodValue = driver.find_element(By.ID, "productOwned0")
prod = driver.find_element(By.ID, "product0")
upgrade = driver.find_element(By.ID, "upgrade0")
upgradeValue = driver.find_element(By.ID, "upgrade0")
while(True):
    
    elem = driver.find_element(By.ID, "bigCookie")
    elem2 = driver.find_element(By.ID, "bigCookie")
    
   
    # elem.send_keys(Keys.RETURN)
    elem.click()
    
    
    if(prod.get_attribute("class") == "product unlocked enabled"):
            prod.click()
            if(prodValue.text == ""):
                 prod.click()
            else:
                if(int(prodValue.text) == 14 ):
                    
                    i+=1
                    prod = driver.find_element(By.ID, "product"+str(i))
                    prodValue = driver.find_element(By.ID, "productOwned"+str(i))
                    prod.click()
                # driver.find_element(By.ID, "product0").click()

            
            

            
    
    # i = 0;  
    # elem2 = driver.find_element(By.CLASS_NAME, "")
        
        
    # print(elem2.get_attribute("innerHTML")[0])
    # elem =
    # if elem.
assert "No results found." not in driver.page_source
# driver.close()

