import sys
sys.path.append("..")
from DB_Interfaces.assignmentInterface import *

class AssignmentImplStub(AssignmentInterface):
    def createAssignment(self, assignment: AssignmentDTO) -> str: #returns assignment ID
        return "testID";
    def updateAssignment(self, assignment: AssignmentDTO):
        return
    def readAssignments(self, assignmentIDs: list[str] = None) -> list[AssignmentDTO]:
        a = AssignmentDTO("name", "date", "desc", 10, "instructor", "", "")
        b = AssignmentDTO("name2", "date", "desc", 10, "instructor", "", "")
        return [a, b]
    def deleteAssignment(self, assignmentIDs: list[str]):
        return