# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(3)
gift_ideas = driver.find_element("xpath","/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[5]")
gift_ideas.click()

time.sleep(5)

gift_men = driver.find_element("xpath","/html/body/div[1]/div[1]/div/div/div[2]/div/a[3]")
gift_men.click()

time.sleep(5)

category = driver.find_element("xpath","/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/ul/li[2]/button")
category.click()

time.sleep(5)

gift_list = driver.find_element("xpath","/html/body/div[1]/header/div/div[6]/div/a[3]")
gift_list.click()

time.sleep(5)

search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("gifts for men")

search_bar.send_keys(Keys.RETURN)

time.sleep(5)

assert "gifts for men" in driver.title

driver.close()
