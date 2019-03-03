from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:/Users/your computer address/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://students.iitmandi.ac.in/webmail/")
username = driver.find_element_by_id("rcmloginuser")
password = driver.find_element_by_id("rcmloginpwd")
username.send_keys("your_rollno")
password.send_keys("********")
driver.find_element_by_id("rcmloginsubmit").click()
time.sleep(1)
for i in range(1,11):
    x='//table/tbody/tr['+str(i)+']'
    elem = driver.find_element_by_xpath(x)
    if(elem.get_attribute("class")=="message unread"):
        elem.click()
        elem.click()
    