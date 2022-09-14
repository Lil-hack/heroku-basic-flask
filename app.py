from flask import Flask
from datetime import datetime
from threading import Thread, Lock
import time
import requests
import paramiko

app = Flask(__name__)

metka=0

def pinger():
    while True:
        res = requests.get('https://binancer.farm/')
        if str(res).find('200')!=-1:
            print('good')
        else:
            host = '194.87.146.137'
            user = 'root'
            pps = 'dVXG4B83sE'
            port = 22

            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=user, password=pps, port=port)
            client.exec_command('sudo reboot')
            client.close()
            time.sleep(300)

        res = requests.get('https://bin.farm/')
        if str(res).find('200') != -1:
            print('good')
        else:
            host = '195.133.49.227'
            user = 'root'
            pps = 'vLTYi1mjTl'
            port = 22

            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=user, password=pps, port=port)
            client.exec_command('sudo reboot')
            client.close()
            time.sleep(300)

        time.sleep(100)




@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    global metka
    print(metka)
    if metka==0:
        Thread(target=pinger, args=()).start()
        metka=1
    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':

    app.run(debug=True, use_reloader=True)

