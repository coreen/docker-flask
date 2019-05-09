from flask import Flask, request, Response
from flask.json import jsonify

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = Flask(__name__)
# NOTE: use 'localhost' for local dev and 'mongo' for docker-to-docker communication
connection = MongoClient('mongo', 27017)

# default only allow GET method
@app.route('/health')
def healthcheck():
	try:
		db = connection.test
		table = db.names
		item = table.find_one()
		# http://flask.pocoo.org/docs/1.0/api/#flask.json.jsonify
		if item is None:
			return jsonify(status='ok')
	except ConnectionFailure:
		return jsonify(status='unhealthy', mongo_connection='not connected')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
