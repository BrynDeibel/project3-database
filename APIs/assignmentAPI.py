from flask import Blueprint
from markupsafe import escape

import sys
sys.path.append("..")
from DB_Interfaces.assignmentInterface import AssignmentInterface


def constructAssignmentBlueprint(interface: AssignmentInterface):
    assignmentBlueprint = Blueprint('assignment_page', __name__)

    @assignmentBlueprint.route('/assignment', methods=['GET'])
    def readAssignment():
        read = interface.readAssignments(interface)
        ret = ""
        for dto in read:
            ret += dto.name + " "
        return ret;
    return(assignmentBlueprint)
