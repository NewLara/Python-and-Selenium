# Selenium Tutorial
# https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver
# access to enter, esc keys
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print("Title = " + driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

# find element by id
# main = driver.find_element_by_id("main")

# explicit waits - driver waits for 10sec until id=main is present (until renders false until element is present)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # for every article found in the main element, loop through them and find any className 'entry-title' inside
    # articles and print them
    articles = main.find_elements_bytag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
    time.sleep(5)

finally:
    driver.quit()


# scrapes webpage for all source code !!!!!
# print(driver.page_source)
# driver.close()
