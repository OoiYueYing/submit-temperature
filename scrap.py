from bs4 import BeautifulSoup
import urllib.request
import time
from selenium import webdriver
import yaml

conf = yaml.load(open('./credentials.yml'))
username = conf['ntu']['userName']
pwd = conf['ntu']['password']

url = "https://sso.wis.ntu.edu.sg/webexe88/owa/sso_login1.asp?t=1&p2=https://wis.ntu.edu.sg/pls/webexe/str_stud.BRANCH_STUD"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
# print(soup)

# google chrome session
driver = webdriver.Chrome('../chromDriver/chromedriver.exe')
driver.get(url)
time.sleep(2)

# fill in userName
userName  = driver.find_element_by_name('UserName')
userName.send_keys(username)
okButton = driver.find_element_by_name('bOption')
okButton.click()

# fill in password
userName  = driver.find_element_by_name('PIN')
userName.send_keys(pwd)
okButton = driver.find_element_by_name('bOption')
okButton.click()

# click on confirm button
CONFIRM_BUTTON_XPATH = '//input[@type="submit" and @value="Confirm"]'
driver.find_element_by_xpath(CONFIRM_BUTTON_XPATH).click()