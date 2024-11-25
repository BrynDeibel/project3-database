'''
API Documentation:

GET /assignments - Gets all assignments 
Returns the following body:
{
  "assignments": [                              #An array of assignment objects
    {                                           #A particular assignment object
      "description": "",                        
      "dueDate": "",                            
      "id": "",                                 
      "inputs": [""],                           #array of strings
      "instructorUsername": "",                 
      "name": "",                               
      "numberOfPoints": 0,
      "outputs": [""]                           #array of strings
    }                       
  ]
}
Returns HTTP code 500 in the event of an error, else returns 200

GET /assigments?ids=[id1,id2,...] - Gets the assignments with the particular ids in the query
Returns the same body as the above GET
Returns HTTP code 500 in the event of an error, else returns 200

POST /assignments - Creates an assignment
Expects the following payload: (Note it's a json so order doesn't matter)
{
    "name": "",                                  
    "dueDate": "",                               
    "description": "",                           
    "numberOfPoints": "",                        
    "instructorUsername": "",                    
    "inputs":  [""],                             #array of strings
    "outputs": [""]                              #array of strings
}
Returns the following body:
{
    "id": ""                                    
}
Returns HTTP code 400 for a bad request, 500 in the event of an error, else returns 200

PUT /assignments?id=id - Updates the assignment with the given id
Expects the exact same payload as the POST
Returns an empty body
Returns HTTP code 400 for a bad request, 500 in the event of an error, else returns 200


DELETE /assignments?ids=[id1,id2,...] - Deletes the assignments with the particular ids in the query
Returns and empty body
Returns HTTP code 500 in the event of an error, else returns 200
'''


from flask import Blueprint, request

import sys
sys.path.append("..")
from RequestHandlers.assignmentHandler import AssignmentHandlerInterface


def constructAssignmentBlueprint(interface: AssignmentHandlerInterface):
    assignmentBlueprint = Blueprint('assignment_page', __name__)

    @assignmentBlueprint.route('/assignments', methods=['GET', 'POST', 'PUT', 'DELETE'])
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