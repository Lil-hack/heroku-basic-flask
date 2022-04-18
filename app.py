from flask import Flask
from datetime import datetime
from selenium import webdriver
app = Flask(__name__)
import os
import random
from threading import Thread, Lock
from flask import send_file
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = os.getcwd()
list_cockie=[]
with os.scandir(path+"\\!1000") as listOfEntries:
    for entry in listOfEntries:
        # печать всех записей, являющихся файлами
        if entry.is_file():
           list_cockie.append(entry.name)
        
def new_youtube(url):
    print(url)
    url=f'https://www.youtube.com'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url)
    file1 = open(f'!1000/{list_cockie[random.randint(0, len(list_cockie))]}', 'r')
    driver.delete_all_cookies()
    for item in file1:
        data = item.split('	')
        if url.find(data[0]) != -1:
            print(file1)
            value = data[6].replace(' ', '').replace('\r', '').replace('\n', '')
            cookie_dict = {
                'name': data[5],
                'value': value,
                "domain": data[0],  # google chrome
                "expires": data[4],
                'path': data[2],
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False
            }
            driver.add_cookie(cookie_dict)
    driver.get(url)
    stroka='Твое имя наше последнее лето'
    time.sleep(5)
    try:
            driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(stroka)
            driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(Keys.ENTER)
    except Exception as e:
            print(e)
    time.sleep(4)
    try:
            driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/ytd-thumbnail/a/yt-img-shadow/img').click()
            time.sleep(5)
    except Exception as e:
            print(e)
    try:
        driver.find_element_by_xpath(
            '//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]').click()
        time.sleep(2)
    except Exception as e:
        print(e)
        
    for i in range(0, 100):
        driver.save_screenshot(f'photo.png')
        print('lox2')
        time.sleep(500)
          
        
@app.route('/get_image')
def get_image():
    filename = 'ip.png'
    return send_file(filename, mimetype='image/png')

@app.route('/get_image2')
def get_image2():
    filename = 'photo.png'
    return send_file(filename, mimetype='image/png')

    
@app.route('/<url>')
def homepage(url):
    print(url)
    Thread(target=new_youtube,args=([url])).start()
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

