import sys
sys.path.append("..")
from DB_Interfaces.submissionInterface import *

class SubmissionImplStub(SubmissionInterface):
    def createSubmission(self, submission: SubmissionDTO) -> str: #returns submission ID
        return submission.assignmentID
    def updateSubmission(self, submission: SubmissionDTO):
        pass
    def readSubmissions(self, submissionIDs: list[str] = None, usernames: list[str] = None, assignmentIDs: list[str] = None) -> list[SubmissionDTO]:
        ret = []
        if submissionIDs != None:
            for s in submissionIDs:
                ret.append(SubmissionDTO("assignmentID", "username", "time", 98.76, s))
        if usernames != None:
            for u in usernames:
                ret.append(SubmissionDTO("assignmentID", u, "time", 97.76))
        if assignmentIDs != None:
            for a in assignmentIDs:
                ret.append(SubmissionDTO(a, "username", "time", 96.76))
        ret.append(SubmissionDTO("assignmentID", "username", "time", 95.76))
        return ret
    def deleteSubmission(self, submissionIDs: list[str]):
        pass