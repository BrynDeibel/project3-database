from flask import Blueprint
from markupsafe import escape

import sys
sys.path.append("..")
from RequestHandlers.AssignmentHandler import AssignmentHandlerInterface


def constructAssignmentBlueprint(interface: AssignmentHandlerInterface):
    assignmentBlueprint = Blueprint('assignment_page', __name__)

    @assignmentBlueprint.route('/assignment', methods=['GET'])
    def readAssignment():
        read = interface.handleReadAssignment(None)
        ret = ""
        for dto in read:
            ret += dto.name + " "
        return ret;

    return(assignmentBlueprint)