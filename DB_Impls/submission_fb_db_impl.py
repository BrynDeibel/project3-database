from DB_Interfaces.submissionInterface import SubmissionDTO, SubmissionInterface
from firebase import firebase

SubmissionDTO
firebase = firebase.FirebaseApplication('https://database-team-project3-default-rtdb.firebaseio.com', None)

class SubmissionInterfaceFirebase(SubmissionInterface):
    async def createSubmission(self, submission: SubmissionDTO) -> str:
        try:
            result = firebase.post('SubmissionsFolder', 
                            {'id': submission.id,
                             'assignmentID': submission.assignmentID,
                             'studentUsername': submission.studentUsername,
                             'submissionTime': submission.submissionTime,
                             'score': submission.score})
            return result['name']
        except Exception as e:
            print(f"Error creating assignment: {e}")
            return False

    async def updateSubmission(self, submission: SubmissionDTO) -> str:
        try:
            result = firebase.put('SubmissionsFolder', submission.id, 
                            {'assignmentID': submission.assignmentID,
                             'studentUsername': submission.studentUsername,
                             'submissionTime': submission.submissionTime,
                             'score': submission.score})
            return result['name']
        except Exception as e:
            print(f"Error creating assignment: {e}")
            return False

    async def readSubmissions(self, submissionIDs: list[str] = None, usernames: list[str] = None, assignmentIDs: list[str] = None) -> list[SubmissionDTO]:
        if submissionIDs is None and usernames is None and assignmentIDs is None:
            result = firebase.get("/SubmissionsFolder", "")
            submissions = []
            if result:
                for r in result:
                    if result[r]:
                        dto = SubmissionDTO(**result[r])
                        dto.id = r
                        submissions.append(dto)
            return submissions
        
        # Fetch all data first
        all_submissions = firebase.get("/SubmissionsFolder", "")

        if not all_submissions:
            return []  # Return an empty list if no data exists

        # Filter results based on provided criteria
        filtered_submissions = []
        for submission in all_submissions:
            # Check if submission matches any of the provided criteria
            if (submissionIDs and submission not in submissionIDs):
                continue  # Skip if submissionID doesn't match
            if (usernames and all_submissions[submission].get('studentUsername') not in usernames):
                continue  # Skip if username doesn't match
            if (assignmentIDs and all_submissions[submission].get('assignmentID') not in assignmentIDs):
                continue  # Skip if assignmentID doesn't match


            dto = SubmissionDTO(**all_submissions[submission])
            dto.id = submission
            filtered_submissions.append(dto)

        return filtered_submissions

    async def deleteSubmission(self, submissionIDs: list[str]):
        try:
            for id in submissionIDs:
                result = firebase.delete('/SubmissionsFolder', id)
            return True
        except Exception as e:
            return False