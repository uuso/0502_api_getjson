import os
from bottle import route, run, view, static_file
from datetime import datetime as dt
from random import random

@route("/")
@view("predictions-in-divs-css")
def index():
	now = dt.now()
	x = random()
	return {
		"date": f"{now.year}-{now.month}-{now.day}",
    	"special_date": x > 0.5,
    	"x": x,
	}
	
@route("/css/<filename:path>")
def send_static(filename):
	return static_file(filename, root = 'css')


	
if os.environ.get('APP_LOCATION') == 'heroku':
	run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
	run(host='localhost', port=80, debug=True)
# run(
#   host="localhost",
#   port=80,
#   autoreload=True
# )