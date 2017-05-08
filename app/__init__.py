from flask import Flask, render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps


app = Flask(__name__)


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'world_bank'
COLLECTION_NAME = 'banks'
FIELDS = {'project_name': True, 'countryname': True, 'countrycode': True, 'lendprojectcost': True, '_id': False}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/json')
def banks():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS)
    json_data = []
    for project in projects:
        json_data.append(project)
    json_data = json.dumps(json_data, default=json_util.default)
    connection.close()
    return json_data

if __name__ == '__main__':
    app.run(debug=True)