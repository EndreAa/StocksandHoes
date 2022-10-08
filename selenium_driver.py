
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
PATH = "C:\Program Files (x86)\chromedriver.exe" # Path to chromedriver.exe
driver = webdriver.Chrome(PATH) # Open Chrome, you can use Firefox, Edge, etc.'

driver.get("https://aksjelive.e24.no/") # Opens the website for the stocknews

print(driver.title)
# id, tag_name, class_name, name, link_text, partial_link_text, xpath, css_selector

search = driver.find_elements(By.name(("q")).click) # Im trying to find the search bar, but
# for some reason the argument by wont work

search.send_keys("Equinor") # Types in the search bar
search.send_keys(Keys.RETURN) # Press enter (nøkkelord = RETURN)

time.sleep(5)  
"""
For improved reliability, you should consider using WebDriverWait in combination with element_to_be_clickable.
"""



driver.quit() 