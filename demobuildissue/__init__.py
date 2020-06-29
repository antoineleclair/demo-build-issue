import os
from bottle import route, run, template

@route('/')
def index(name):
    return template('<h1>Hi!</h1>')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
