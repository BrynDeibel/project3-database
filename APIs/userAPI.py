from flask import Blueprint, request, jsonify
import sys
sys.path.append("..")
from RequestHandlers.UserHandler import UserHandlerInterface


def constructUserBlueprint(interface: UserHandlerInterface):
    userBlueprint = Blueprint('user_page', __name__)

    @userBlueprint.route('/users', methods=['GET', 'POST', 'DELETE'])
    def handleUsers():
        if request.method == 'GET':
            usernames = request.args.getlist('usernames')
            res = interface.handleGET(usernames)
            return jsonify(res)
        
        if request.method == 'POST':
            data = request.get_json()
            if not data or 'username' not in data or 'password' not in data or 'role' not in data:
                return jsonify({'error': 'Invalid request payload'}), 400
            
            res = interface.handlePOST(data)
            return jsonify(res)
        
        if request.method == 'DELETE':
            usernames = request.args.getlist('usernames')
            if not usernames:
                return jsonify({'error': 'No usernames provided'}), 400
            
            res = interface.handleDELETE(usernames)
            return jsonify(res)
    
    return userBlueprint
