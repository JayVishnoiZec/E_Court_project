# import json
# from flask import Flask, jsonify
# import requests
# # from E_Court_Scrap import dict__

# from E_Court_Scrap import main_

# app = Flask(__name__)

# token = "CBE0102A675F4A94B06D0F35BCC14D2B"


# @app.route('/')
# def info():
#     result = main_()
#     return jsonify(result)
#     rec_count += 1


# if __name__ == "__main__":
#     app.run(debug=True)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import base64
import requests









driver = webdriver.Chrome(executable_path='/home/zec/Desktop/chromedriver')
driver.maximize_window()
driver.get("https://services.ecourts.gov.in/ecourtindia_v4_bilingual/cases/c_index.php?state=D&state_cd=17&dist_cd=14#")
sleep(3)
src = driver.find_element(By.ID, "captcha_image").get_attribute("src")
print(src)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

image_b64 = base64.b64encode(requests.get(src).content)
print(requests.get(src).content)
print("<<<<<<<<<<<<<<<<<<<<<<<")
print("image_b64", image_b64)
print("<<<<<<<<<<<<<<<<<<<<<<<")


Balance = requests.get(
    f"https://bcsapi.xyz/api/user/balance?access_token={ACCESS_TOKEN}")
print(Balance.json())
print("==========================")


tokan_dict_ = {
    "b64image": str(image_b64),
    "access_token": ACCESS_TOKEN
}

response_imz_id = requests.post(
    f"https://bcsapi.xyz/api/captcha/image", params=tokan_dict_)

img_id_json = response_imz_id.json()
print(response_imz_id.json())
print(img_id_json['id'])
print("==========================")

solved_captcha_ = requests.get(
    f"https://bcsapi.xyz/api/captcha/{img_id_json['id']}?access_token={ACCESS_TOKEN}")
print(solved_captcha_.json())
print(solved_captcha_.json()["text"])


#################################################################################
