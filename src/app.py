# src/app.py

"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException
from datastructure import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member_data(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }
    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def add_member():
    request_data = request.json
    if not request_data or "first_name" not in request_data or "age" not in request_data:
        return jsonify({"error": "Missing required data"}), 400

    member = {
        "first_name": request_data["first_name"],
        "last_name": jackson_family.last_name,
        "age": request_data["age"],
        "lucky_numbers": request_data.get("lucky_numbers", []),
    }
    jackson_family.add_member(member)
    return jsonify({"message": "Member added successfully"}), 201

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if jackson_family.delete_member(member_id):
        return jsonify({"message": "Member deleted successfully"}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route('/member/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    request_data = request.json
    if not request_data:
        return jsonify({"error": "No data provided for update"}), 400

    if jackson_family.update_member(member_id, request_data):
        return jsonify({"message": "Member updated successfully"}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
