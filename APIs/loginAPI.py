from flask import Blueprint, request, jsonify
from markupsafe import escape

import sys
sys.path.append("..")
from RequestHandlers.loginHandler import LoginHandlerInterface


def constructLoginBlueprint(interface: LoginHandlerInterface):
    loginBlueprint = Blueprint('login_page', __name__)

    @loginBlueprint.route('/login',methods=['POST'])
    def login():
        data = request.get_json()
        if not data or 'username' not in data or 'password' not in data:
            return 400
        
        res = interface.handleLogin(data['username'],data['password'])

        return jsonify(res)
    
    return (loginBlueprint)