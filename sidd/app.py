#!flask/bin/python
from flask import Flask
from flask import render_template
import csv
import json
app = Flask(__name__, static_url_path='')

@app.route('/')
def index():

    return render_template('map.html')

@app.route('/complains')
def complains():
	csvfile = open("complaint.csv", "r")
	fieldnames = ("category","lat", "long", "image", "caption")
	reader = csv.DictReader(csvfile, fieldnames)
	out = json.dumps([row for row in reader])
	return out

if __name__ == '__main__':
    app.run(debug=True)
