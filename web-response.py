from flask import Flask
import requests
import time
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/response/<website>')
def w_response(website):

    url = 'http://' + website

    start = time.time()
    r = requests.get(url, timeout=3)
    r.raw.read()
    end = time.time()
    t = int(round((end -start) * 1000))
    response_time = {}
    response_time['time'] = t

    return '%s' % json.dumps(response_time)

if __name__ == '__main__':
    app.run()
