import csv
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def main_():
    driver = webdriver.Chrome(executable_path='/home/zec/Desktop/chromedriver')
    driver.maximize_window()
    driver.get("https://services.ecourts.gov.in/ecourtindia_v4_bilingual/cases/c_index.php?state=D&state_cd=17&dist_cd=14#")
    sleep(5)
    # if you want to click Court Establishment than uncommant the below  line

    # click=driver.find_element(By.ID,'radCourtEst').click()
    # sleep(5)
    # and change the  id (court_code)
    select = Select(driver.find_element(By.ID, 'court_complex_code'))
    select.select_by_index(3)
    sleep(5)
    driver.find_element(
    By.XPATH, '/html/body/form/div[8]/div[2]/div[6]/span[3]/input').send_keys('5579')
    
    
    driver.find_element(By.XPATH, '/html/body/form/div[8]/div[2]/div[7]/span[3]/input').send_keys('2020')
    sleep(20)
    driver.find_element(By.XPATH, '/html/body/form/div[8]/div[2]/div[9]/span[3]/input[1]').click()
    sleep(20)
    driver.find_element(By.XPATH, '/html/body/form/div[8]/div[5]/table/tbody/tr[2]/td[4]/a').click()
    sleep(5)
    
    

    Date = driver.find_element( By.XPATH, '//*[@id="secondpage"]/div[2]/div[2]/span[2]/label/strong[2]').text

    if driver.find_element(By.XPATH, '//*[@id="secondpage"]/div[2]/div[2]/span[2]/label/strong[1]').text == "Next Hearing Date":
        print(f"Next Hearing Date :- {Date}")

    elif driver.find_element(By.XPATH, '//*[@id="secondpage"]/div[2]/div[2]/span[2]/label/strong[1]').text == "Decision Date":
        print(f"Decision Date :- {Date}")

    Purpose_of_hearing = driver.find_element(By.XPATH, '//*[@id="secondpage"]/div[2]/table[3]/tbody/tr[2]/td[5]').text
    print(f"Purpose of Hearing :- {Purpose_of_hearing}")

    Case = driver.find_element(By.XPATH, '//*[@id="secondpage"]/div[2]/div[2]/span[3]/label/strong[2]').text

    if driver.find_element(By.XPATH, '//*[@id="secondpage"]/div[2]/div[2]/span[3]/label/strong[1]').text == "Case Stage":
        print(f"Case Stage :- {Case}")

    elif driver.find_element(By.XPATH, '//*[@id="secondpage"]/div[2]/div[2]/span[3]/label/strong[1]').text == "Case Status ":
        print(f"Case Status :- {Case}")

    Judge = driver.find_element(By.XPATH, '//*[@id="secondpage"]/div[2]/table[3]/tbody/tr[2]/td[2]').text
    print(f"Judge :- {Judge}")
    sleep(5)
    business_Date_click = driver.find_element(By.XPATH, '//*[@id="secondpage"]/div[2]/table[3]/tbody/tr[2]/td[3]/a').click()
    sleep(5)
    business = driver.find_element(
        By.XPATH, '//*[@id="thirdpage"]/div/center/center[7]/table/tbody/tr[2]/td[3]').text

    if driver.find_element(By.XPATH, '//*[@id="thirdpage"]/div/center/center[7]/table/tbody/tr[2]/td[1]').text == "Business":
        print(f"Business :- {business}")

    global dict__
    dict__ = {"Date": Date,
              "Purpose_of_hearing": Purpose_of_hearing,
              "Case": Case,
              "Judge": Judge,
              "business": business, }

    print(dict__)

    return dict__

# driver.close()


# main()
