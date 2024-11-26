from abc import ABC, abstractmethod #abstract base class

class AssignmentDTO():
    def __init__(self, name: str, duedate, #what type should due date be?
                         description: str, numberOfPoints: int, instructorUsername: str,
                         inputs: list, outputs: list, id: str = None):
        self.id = id
        self.name = name
        self.duedate = duedate
        self.description = description
        self.numberOfPoints = numberOfPoints
        self.instructorUsername = instructorUsername
        self.inputs = inputs
        self.outputs = outputs

class AssignmentInterface(ABC):
    @abstractmethod
    def createAssignment(self, assignment: AssignmentDTO) -> str: #returns assignment ID
        pass
    @abstractmethod
    def updateAssignment(self, assignment: AssignmentDTO):
        pass
    @abstractmethod
    def readAssignments(self, assignmentIDs: list[str] = None) -> list[AssignmentDTO]:
        pass
    @abstractmethod
    def deleteAssignment(self, assignmentIDs: list[str]):
        pass
