from flask import Flask
from datetime import datetime
from threading import Thread, Lock
import time
app = Flask(__name__)

def pinger():
    while True:
        print('lox')
        time.sleep(5)




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

