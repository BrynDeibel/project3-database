'''
API Documentation:

GET /users - Gets all users or specific users
Expects
/users?usernames=username1&usernames=username2&usernames=username3
(A list of usernames)
Returns the following body:
{
  "users": [                              #An array of users
    {                                           #A particular user object
      "username:"",
      "role":""
    }
    .......
  ]
}
On Error Returns
{
    "error":""
}


POST /users - Creates an user
Expects the following payload: 
{
    "username":"",
    "password":"",
    "role":""
}
Returns the following body:
{
    "status": "success", "message":"User Successfully Created"                                  
} with 200 code
Returns the following body on fail:
{
    "status": "failure", 'message':""
} with bad request code





DELETE /users?usernames=username1&usernames=username2&usernames=username3......
(a object with list of users)
On Failure returns 
{
    "error": "No usernames provided"
} with bad request code
On Success returns
{
    "status": "success", "message": "User(s) deleted successfully"
} with code 200

'''


from flask import Blueprint, request, jsonify
import sys
sys.path.append("..")
from RequestHandlers.UserHandler import UserHandlerInterface


def constructUserBlueprint(interface: UserHandlerInterface):
    userBlueprint = Blueprint('user_page', __name__)

    @userBlueprint.route('/users', methods=['GET', 'POST', 'PATCH', 'DELETE'])
    def handleUsers():
        if request.method == 'GET':
            res = interface.handleGET(request.args.to_dict())
            return jsonify(res)
        
        if request.method == 'POST':
            data = request.get_json()
            if not data or 'username' not in data or 'password' not in data or 'role' not in data:
                return jsonify({'error': 'Invalid request payload'}), 400
            
            res = interface.handlePOST(data)
            return jsonify(res)
        
        if request.method == 'PATCH':
            data = request.get_json()
            if not data or 'name' not in data or 'role' not in data:
                return jsonify({'error': 'Invalid request payload'}), 400
            res = interface.handlePATCH(request.args.to_dict(), data)
            return jsonify(res)
        
        if request.method == 'DELETE':
            res = interface.handleDELETE(request.args.to_dict())
            return jsonify(res)
    
    return userBlueprint
