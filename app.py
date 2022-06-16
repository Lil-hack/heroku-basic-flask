from flask import Flask
from datetime import datetime
from threading import Thread, Lock
import time
import requests


app = Flask(__name__)

def pinger():
    while True:
        res = requests.get('https://binancer.farm/')
        if res.find('200')!=-1:
            print('good')
        else:
            print('bad')

        time.sleep(100)




@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    Thread(target=pinger, args=()).start()
    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':

    app.run(debug=True, use_reloader=True)

