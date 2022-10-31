import csv
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image
from selenium import webdriver
from PIL import Image, ImageFilter
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"/home/zec/Downloads"
driver = webdriver.Chrome(executable_path='/home/zec/Desktop/chromedriver')
driver.maximize_window()
driver.get("http://sistemas.cvm.gov.br/?fundosreg")

# change frame
driver.switch_to.frame("Main")


def get_captcha(driver, element, path):
    # now that we have the preliminary stuff out of the way time to get that image :D
    location = element.location
    size = element.size
    # saves screenshot of entire page
    driver.save_screenshot(path)

    # uses PIL library to open image in memory
    image = Image.open(path)

    left = location['x']
    top = location['y'] + 140
    right = location['x'] + size['width']
    bottom = location['y'] + size['height'] + 140

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, 'png')  # saves new cropped image

    captcha = pytesseract.image_to_string(image)
    captcha = captcha.replace(" ", "").strip()
    print(captcha)
# download image/captcha
img = driver.find_element_by_xpath(".//*[@id='trRandom3']/td[2]/img")
get_captcha(driver, img, "captcha.png")