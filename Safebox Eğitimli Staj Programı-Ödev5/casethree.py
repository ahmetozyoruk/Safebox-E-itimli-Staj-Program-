from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskmongodb"]
users_collection = db["users"]

@app.route('/adduser', methods=['POST'])
def add_user():
    name = request.json.get('name')
    age = request.json.get('age')
    job = request.json.get('job')
    description = request.json.get('description', 1)

    user_data = {
        'Name': name,
        'Age': age,
        'Job': job,
        'Description': description
    }

    users_collection.insert_one(user_data)

    return jsonify({'message': 'User added successfully'}), 200

@app.route('/25', methods=['GET'])
def get_users_over_25():
    users_over_25 = users_collection.find({'Age': {'$gt': 25}})
    users_list = list(users_over_25)
    
    return json_util.dumps(users_list), 200

@app.route('/age/<int:age>', methods=['GET'])
def get_users_by_age(age):
    users_by_age = users_collection.find({'Age': {'$gt': age}})
    users_list = list(users_by_age)
    
    return json_util.dumps(users_list), 200

@app.route('/', methods=['GET'])
def get_all_users():
    all_users = users_collection.find()
    users_list = list(all_users)
    
    return json_util.dumps(users_list), 200

@app.route('/deleteuser', methods=['POST', 'DELETE'])
def delete_user():
    user_id = request.json.get('id')

    result = users_collection.delete_one({'_id': user_id})
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
