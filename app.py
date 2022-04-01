from flask import Flask
from datetime import datetime
from selenium import webdriver
app = Flask(__name__)
import os
import random
from threading import Thread, Lock
from flask import send_file
import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# path = os.getcwd()
# list_cockie=[]
# with os.scandir(path+"/cockiestwitch") as listOfEntries:
#     for entry in listOfEntries:
#         # печать всех записей, являющихся файлами
#         if entry.is_file():
#            list_cockie.append(entry.name)
        
def new(url):
    print(url)
    url=f'https://www.twitch.tv/{url}'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("http://check.torproject.org")
    driver.save_screenshot(f'ip.png')
    driver.get(url)
    for i in range(0, 100):
        time.sleep(5)
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div[7]/div/div[3]/button').click()
        except Exception as e:
            pass
        driver.save_screenshot(f'photo.png')
        print('lox2')
        time.sleep(500)
        driver.get(url)
        
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

@app.route('/youtube/<url>')
def homepage_youtube(url):
    print(url)
    Thread(target=new_youtube,args=([url])).start()
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)
@app.route('/<url>')
def homepage(url):
    print(url)
    Thread(target=new,args=([url])).start()
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

