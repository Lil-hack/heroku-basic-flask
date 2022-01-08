from flask import Flask
from datetime import datetime
from selenium import webdriver
app = Flask(__name__)
import os
import random
from threading import Thread, Lock
from flask import send_file


url="https://www.twitch.tv/satomin2007"
def new():
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
            wd.save_screenshot(f'photo.png')
            print('lox2')
            time.sleep(500)
            wd.get(url)
    
@app.route('/get_image')
def get_image():
    filename = 'ip.png'
    return send_file(filename, mimetype='image/png')
@app.route('/get_image2')
def get_image():
    filename = 'photo.png'
    return send_file(filename, mimetype='image/png')
@app.route('/')
def homepage():
    Thread(target=new).start()
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

