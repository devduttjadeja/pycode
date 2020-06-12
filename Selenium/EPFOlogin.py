from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import pytesseract
import re
import time

def get_captcha_text(location, size):
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    im = Image.open('screenshot.png') # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('screenshot.png')
    croppedImage = Image.open('screenshot.png')
    captcha_text = pytesseract.image_to_string(croppedImage)
    numbers = re.split(r"[^0-9\s]", captcha_text)
    operations = re.sub(r'[0-9]+', '', captcha_text)
    operation = operations[0]

    answer = 0

    if operation is "-":
        answer = int(numbers[0]) - int(numbers[1])
    if operation is "+":
        answer = int(numbers[0]) + int(numbers[1])

    return str(answer)

def startApplication():
    driver = webdriver.Chrome("C:\\Users\\Devdutt\\.wdm\\drivers\\chromedriver\\83.0.4103.39\\win32\\chromedriver.exe")
    # driver = webdriver.chrome(ChromeDriverManager().install())

    # EPFO Website
    # driver.get("https://unifiedportal-mem.epfindia.gov.in/memberinterface/")
    # driver.find_element_by_id("userName").send_keys("100133927190")
    # driver.find_element_by_id("password").send_keys("Dev@may2015")
    # element = driver.find_element_by_xpath("//div[@id='toggleCaptcha']/div/div/img")

    # EPF Passbook website
    driver.get("https://passbook.epfindia.gov.in/MemberPassBook/Login")
    driver.maximize_window()
    driver.find_element_by_id("username").send_keys("100133927190")
    driver.find_element_by_id("password").send_keys("Dev@may2015")
    element = driver.find_element_by_id("captcha_id")

    location = element.location
    size = element.size
    driver.save_screenshot('screenshot.png')
    ans = get_captcha_text(location, size)

    driver.find_element_by_id("captcha").send_keys(ans)
    time.sleep(1)
    driver.find_element_by_id("login").click()
    time.sleep(100)
    # driver.close()

startApplication()