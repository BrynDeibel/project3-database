
'''
API Documentation:

POST /login - Login User 

Expects this body in JSON
{
    "username":"",
    "password":""
}

Returns the following body on success:
{
    "status":"success",
    "role":"<user_role>"
    "name":""
}
Returns the following body on failure
{
    "status":"failure",
    "message":"<Fail Message>"
}

Returns HTTP error code in the event of an error, else returns 200
'''

from flask import Blueprint, request, jsonify
from markupsafe import escape

import sys
sys.path.append("..")
from RequestHandlers.LoginHandler import LoginHandlerInterface


def constructLoginBlueprint(interface: LoginHandlerInterface):
    loginBlueprint = Blueprint('login_page', __name__)

    @loginBlueprint.route('/login',methods=['POST'])
    def login():
        data = request.get_json()
        if not data:
            return jsonify({"status":"error","message":"No data provided"})
        if "username" not in data or "password" not in data:
            return jsonify({"status":"error","message":"Need both username and password"})
        
        res = interface.handleLogin(data['username'],data['password'])

        return res
    
    return (loginBlueprint)
