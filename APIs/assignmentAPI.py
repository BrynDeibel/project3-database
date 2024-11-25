'''
API Documentation:

GET /assignment - Gets all assignments 
Returns the following body:
{
  "assignments": [                              #An array of assignment object
    {                                           #A particular assignment object
      "description": "",                        #type string
      "dueDate": "",                            #type string
      "id": "",                                 #type string
      "inputs": [""],                           #type array of strings
      "instructorUsername": "",                 #type string
      "name": "",                               #type string
      "numberOfPoints": 0,                      #type int
      "outputs": [""]                           #type array of strings
    }                       
  ]
}
Returns HTTP code 500 in the event of an error, else returns 200

GET /assigment?ids=[id1,id2,...] - Gets the assignments with the particular ids in the query
Returns the same body as the above GET
Returns HTTP code 500 in the event of an error, else returns 200

POST /assignment - Creates an assignment
Expects the following payload: (Note it's a json so order doesn't matter)
{
    "name": "",                                  #type string
    "dueDate": "",                               #type string
    "description": "",                           #type string
    "numberOfPoints": "",                        #type string
    "instructorUsername": "",                    #type string
    "inputs":  [""],                             #type array of strings
    "outputs": [""]                              #type array of strings
}
Returns the following body:
{
    "id": ""                                    #type string
}
Returns HTTP code 400 for a bad request, 500 in the event of an error, else returns 200

PUT /assignment?id=id - Updates the assignment with the given id
Expects the exact same payload as the POST
Returns an empty body
Returns HTTP code 400 for a bad request, 500 in the event of an error, else returns 200


DELETE /assignmentids=[id1,id2,...] - Deletes the assignments with the particular ids in the query
Returns HTTP code 500 in the event of an error, else returns 200
'''


from flask import Blueprint, request, jsonify
from markupsafe import escape

import sys
sys.path.append("..")
from RequestHandlers.AssignmentHandler import AssignmentHandlerInterface


def constructAssignmentBlueprint(interface: AssignmentHandlerInterface):
    assignmentBlueprint = Blueprint('assignment_page', __name__)

    @assignmentBlueprint.route('/assignment', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def doAssignmentThing():
        if (request.method == 'GET'):
            res = interface.handleGET(request.args.to_dict())
            return res
        if (request.method == 'POST'):
            res = interface.handlePOST(request.json)
            return res
        if (request.method == 'PUT'):
            res = interface.handlePUT(request.args.to_dict(), request.json)
            return res
        if (request.method == 'DELETE'):
            res = interface.handleDELETE(request.args.to_dict())
            return res

    return(assignmentBlueprint)