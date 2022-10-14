import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# target
target = input("Who we gonna search today? ")
time.sleep(1)

# browsing
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5)

# logging in
username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
username.clear()
password.clear()
username.send_keys("insert_your_username_here")
password.send_keys("insert_your_password_here")
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(10)

# save login pop-up
notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
time.sleep(10)

# turn on notifications
notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
time.sleep(7)

# searchbox
searchbox = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
searchbox.clear()
time.sleep(4)
searchbox.send_keys(target)
time.sleep(7)
searchbox.send_keys(Keys.ENTER)
time.sleep(10)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)

# aggregated data
data = []

dt = str(datetime.datetime.today())
data.append(dt)
account_name = driver.find_element(By.TAG_NAME, 'h2')
data.append(account_name.text)
time.sleep(1)
posts_count = driver.find_elements(By.XPATH, './/span[@class = "_ac2a"]')
for post in posts_count:
    data.append(post.text)

print('updated_at: ' + data[0])
print('account_name: ' + data[1])
print('posts: ' + data[2])
print('followers: ' + data[3])
print('following: ' + data[4])
