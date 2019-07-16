# -*- coding: cp936 -*-
def sendImage(image_path):
    import requests
    url = "http://ss.ss.ss.ss:80/bot6ssssssssssss:ssssssssssss/sendPhoto";
    files = {'photo': open(image_path, 'rb')}
    data = {'chat_id' : "-ssssssssssss"}
    r= requests.post(url, files=files, data=data)
    return
def parse_captcha(image_path):
    # Load image into memory
    from io import BytesIO
    import base64
    import requests
    import time
    buffer = BytesIO()
    image = Image.open(image_path)
    image.save(buffer, format="PNG")
    # Use base64 to encode image buffer
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    # Anti-captcha API structure
    data = {
        "clientKey":"ssssssssssss",
        "task": {
            "type": "ImageToTextTask",
            "body": img_str,
            "phrase":False,
            "case": True,
            "numeric": 2,
            "math": 0,
            "minLength": 4,
            "maxLength": 4
        }
    }
    # Create a ImageToTextTask and retrieve taskId from response
    r = requests.post("https://api.anti-captcha.com/createTask", json=data)
    r.raise_for_status()
    task_id = r.json()['taskId']
    # Polling for task finish.
    ret = ""
    while True:
        data = {
            "clientKey":"ssssssssssss",
            'taskId': task_id
        }
        r = requests.post("https://api.anti-captcha.com/getTaskResult", json=data)
        r.raise_for_status()
        if r.json()['status'] == 'ready':
            ret = r.json()['solution']['text']
            break
        time.sleep(5)
    return ret
import time
from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome()
driver.get("https://console.bce.baidu.com/cdn/#/cdn/package/list")
time.sleep(10)
inloop = 1
while (inloop > 0):
    driver.find_element_by_id("choose-uc-login").click()
    driver.save_screenshot('test.png')
    element = driver.find_element_by_id("token-img")
    left = element.location['x']
    right = element.location['x']+element.size['width']
    top = element.location['y']
    bottom = element.location['y']+element.size['height']
    img = Image.open('test.png')
    img = img.crop((left, top, right, bottom))
    img.save('caputa.png')
    img = img.convert('L')
    img.save('temp.png')
    driver.find_element_by_id("uc-common-account").send_keys("ssssssssssss")
    driver.find_element_by_id("ucsl-password-edit").send_keys("ssssssssssss")
    data = parse_captcha("temp.png")
    driver.find_element_by_id("uc-common-token").send_keys(data)
    driver.save_screenshot('output.png')
    driver.find_element_by_id("submit-form").click()
    time.sleep(5)
    driver.refresh()
    driver.save_screenshot('output1.png')
    time.sleep(5)
    driver.get("https://console.bce.baidu.com/cdn/#/cdn/overview")
    driver.save_screenshot('output2.png')
    time.sleep(5)
    driver.get("https://console.bce.baidu.com/cdn/#/cdn/package/list")
    time.sleep(5)
    js5 = "window.scrollTo(document.body.scrollWidth,0)"
    driver.execute_script(js5)
    time.sleep(5)
    driver.save_screenshot('output3.png')
    time.sleep(5)
    driver.get("https://console.bce.baidu.com/cdn/#/cdn/overview")
    time.sleep(5)
    js5 = "window.scrollTo(document.body.scrollWidth,0)"
    driver.execute_script(js5)
    driver.implicitly_wait(3)
    time.sleep(5)
    driver.save_screenshot('output4.png')
    if (driver.current_url.find("login.bce.baidu.com") > 0):
        inloop = 1
    else:
        inloop = 0
driver.quit()
sendImage('output3.png')
sendImage('output4.png')
