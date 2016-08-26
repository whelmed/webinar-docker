import logging
import os
import redis

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from data import DATA
app = Flask(__name__)
application = app

HOST = os.environ.get('WEBINAR_SERVICE_SERVICE_HOST','db')


@app.route('/')
def index():
    return render_template('index.html', context=DATA)

@app.route('/env')
def env():
    return str(os.environ)

@app.route('/redis/<key>/<value>')
def from_redis(key, value):
    try:
        r = redis.StrictRedis(host=HOST, port=6379, db=0)
    except:
        return "Could not connect to redis server", 500

    r.set(key, value)
    return 'You set the {0} value to {1}'.format(key, r.get(key))

@app.route('/redis/get/all')
def redis_all():
    try:
        r = redis.StrictRedis(host=HOST, port=6379, db=0)
        return str([(key, r.get(key)) for key in r.keys()])
    except:
        return "Could not connect to redis server", 500


@app.errorhandler(500)
def server_error(e):
    return 'An error has occurred on the server', 500




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
