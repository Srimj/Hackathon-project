from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os


driver = webdriver.Firefox()

driver.get("https://github.com/login")
time.sleep(5)
a = driver.find_element_by_xpath('//*[@id="login_field"]')
time.sleep(2)
a.click()
a.send_keys("Srimj")
a = driver.find_element_by_xpath('//*[@id="password"]')
time.sleep(2)
a.click()
a.send_keys("srishailmj26")
a.send_keys(Keys.ENTER)
time.sleep(5)
a = driver.find_element_by_xpath('//*[@id="user-links"]/li[2]/details/summary')
time.sleep(2)
a.click()
a = driver.find_element_by_xpath('//*[@id="user-links"]/li[2]/details/ul/a[1]')
time.sleep(2)
a.click()
time.sleep(5)
a = driver.find_element_by_xpath('//*[@id="repository_name"]')
repo_name = input("Enter repo name: ")
a.send_keys(repo_name)
repo_name = repo_name.replace(' ', '-')
time.sleep(2)
a.send_keys(Keys.ENTER)
time.sleep(5)
os.system('git init')
os.system('git add .')
os.system('git commit -m "random"')
os.system('git remote add origin https://github.com/Srimj/'+repo_name+'.git')
os.system('git push -u origin master')