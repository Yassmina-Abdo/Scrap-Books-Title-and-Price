from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import csv


options = Options()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(
    r"D:\Programs\New folder\chromedriver.exe", options=options)


driver.get('https://www.amazon.in/gp/bestsellers/books/')

titles = driver.find_elements_by_xpath("//div[@class='p13n-sc-truncated']")
prices = driver.find_elements_by_xpath("//span[@class='p13n-sc-price']")

titles_list = []
prices_list = []
for title in titles:
    titles_list.append(title.text)


for price in prices:
    prices_list.append(price.text)

# --------------------------- Save as csv File -----------------------------
df = pd.DataFrame({'Title Name': titles_list, 'Price': prices_list})
df.to_csv('Books.csv', index=False, encoding='utf-8-sig')
