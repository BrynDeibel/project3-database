'''
API Documentation:

GET /submissions - Gets all submission 
Returns the following body:
{
  "submissions": [                              #An array of submission objects
    {                                           #A particular submission object
      {
        "assignmentID": "",                     
        "score": "",
        "submissionId": "",
        "studentUsername": "",
        "submissionTime": ""       
    }                       
  ]
}
Returns HTTP code 500 in the event of an error, else returns 200

GET /submissions?submissionIds=[id1,id2,...]&assignmentIds=[id1,id2,...]&usernames=[name1, name2, ...]
        -Each of these optional arguments can be put in any order or not included to filter results
Returns the same body as the above GET
Returns HTTP code 500 in the event of an error, else returns 200

POST /submissions - Creates a submission
Expects the following payload: (Note it's a json so order doesn't matter)
{
    "assignmentID": "",                     
    "studentUsername": "",
    "submissionTime": "",
    "score": ""
}
Returns the following body:
{
    "id": ""                                   
}
Returns HTTP code 400 for a bad request, 500 in the event of an error, else returns 200

PUT /submissions?id=id - Updates the submission with the given id
Expects the exact same payload as the POST
Returns an empty body
Returns HTTP code 400 for a bad request, 500 in the event of an error, else returns 200


DELETE /submissions?ids=[id1,id2,...] - Deletes the submissions with the particular ids in the query
Reeturns an empty body
Returns HTTP code 500 in the event of an error, else returns 200
'''


from flask import Blueprint, request

import sys
sys.path.append("..")
from RequestHandlers.submissionHandler import SubmissionHandlerInterface


def constructSubmissionBlueprint(interface: SubmissionHandlerInterface):
    submissionBlueprint = Blueprint('submission_page', __name__)

    @submissionBlueprint.route('/submissions', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def doSubmissionsThing():
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

    return(submissionBlueprint)