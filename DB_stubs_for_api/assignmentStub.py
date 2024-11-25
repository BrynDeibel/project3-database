import sys
sys.path.append("..")
from DB_Interfaces.assignmentInterface import *

class AssignmentImplStub(AssignmentInterface):
    def createAssignment(self, assignment: AssignmentDTO) -> str: #returns assignment ID
        return assignment.name;
    def updateAssignment(self, assignment: AssignmentDTO):
        return
    def readAssignments(self, assignmentIDs: list[str] = None) -> list[AssignmentDTO]:
        l = []
        if assignmentIDs != None:
            for a in assignmentIDs :
                dto = AssignmentDTO(a, "date", "desc", 10, "instructor", ["input 1", "input2"], ["output 1", "output2"])
                l.append(dto)
        
        return l
    def deleteAssignment(self, assignmentIDs: list[str]):
        return