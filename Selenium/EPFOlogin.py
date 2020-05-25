from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome("C:\\Users\\Devdutt\\.wdm\\drivers\\chromedriver\\83.0.4103.39\\win32\\chromedriver.exe")
# driver = webdriver.chrome(ChromeDriverManager().install())
driver.get("https://unifiedportal-mem.epfindia.gov.in/memberinterface/")
driver.find_element_by_id("userName").send_keys("100133927190")
driver.find_element_by_id("password").send_keys("Dev@may2015")
# driver.find_element_by_id("loginbutton").click()