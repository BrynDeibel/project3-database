from abc import ABC, abstractmethod #abstract base class

class SubmissionDTO():
    def __init__(self, assignmentID: str, studentUsername: str, submissionTime, #what type should submission type be?
                         score: float, id: str = None):
        self.id = id
        self.assignmentID = assignmentID
        self.studentUsername = studentUsername
        self.submissionTime = submissionTime
        self.score = score
        
class SubmissionInterface(ABC):
    @abstractmethod
    async def createSubmission(self, submission: SubmissionDTO) -> str: #returns submission ID
        pass
    @abstractmethod
    async def updateSubmission(self, submission: SubmissionDTO):
        pass
    @abstractmethod
    async def readSubmissions(self, submissionIDs: list[str] = None, usernames: list[str] = None, assignmentIDs: list[str] = None) -> list[SubmissionDTO]:
        pass
    @abstractmethod
    async def deleteSubmission(self, submissionIDs: list[str]):
        pass