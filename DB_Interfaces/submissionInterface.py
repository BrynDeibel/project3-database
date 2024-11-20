from abc import ABC, abstractmethod #abstract base class

class SubmissionDTO():
    def __init__(self, assignmentID: str, studentUsername: str, submissionTime, #what type should submission type be?
                         score: float, ID: str = None):
        self.id = id
        self.assignmentID = assignmentID
        self.studentUsername = studentUsername
        self.submissionTime = submissionTime
        self.score = score
        
class SubmissionInterface(ABC):
    @abstractmethod
    def createSubmission(self, submission: SubmissionDTO) -> str: #returns submission ID
        pass
    @abstractmethod
    def updateSubmission(self, submission: SubmissionDTO):
        pass
    @abstractmethod
    def readSubmissionsByID(self, submissionIDs: list[str] = None) -> list[SubmissionDTO]:
        pass
    #this should probably be overloading the above function, but idk how to do that cleanly in python
    @abstractmethod
    def readSubmissions(self, usernames: list[str] = None, assignmentIDs: list[str] = None) -> list[SubmissionDTO]:
        pass
    @abstractmethod
    def deleteSubmission(self, submissionIDs: list[str]):
        pass