from DB_Interfaces.submissionInterface import SubmissionDTO, SubmissionInterface
from firebase import firebase

SubmissionDTO
firebase = firebase.FirebaseApplication('https://database-team-project3-default-rtdb.firebaseio.com', None)

class SubmissionInterfaceFirebase(SubmissionInterface):
    def createSubmission(self, submission: SubmissionDTO) -> str:
        try:
            result = firebase.post('/TestFolder2', 
                            {'id': submission.id,
                             'assignmentID': submission.assignmentID,
                             'studentUsername': submission.studentUsername,
                             'submissionTime': submission.submissionTime,
                             'score': submission.score})
            return result['name']
        except Exception as e:
            print(f"Error creating assignment: {e}")
            return False

    def updateSubmission(self, submission: SubmissionDTO) -> str:
        try:
            result = firebase.put('/TestFolder2', submission.id, 
                            {'assignmentID': submission.assignmentID,
                             'studentUsername': submission.studentUsername,
                             'submissionTime': submission.submissionTime,
                             'score': submission.score})
            return result['name']
        except Exception as e:
            print(f"Error creating assignment: {e}")
            return False

    def readSubmissions(self, submissionIDs: list[str] = None, usernames: list[str] = None, assignmentIDs: list[str] = None) -> list[SubmissionDTO]:
        try:
            if submissionIDs is None and usernames is None and assignmentIDs is None:
                result = firebase.get("/TestFolder3", "")
                return result
            
            # Fetch all data first
            all_submissions = firebase.get("/TestFolder3", "")

            if not all_submissions:
                return []  # Return an empty list if no data exists

            # Filter results based on provided criteria
            filtered_submissions = []
            for submission in all_submissions:
                # Check if submission matches any of the provided criteria
                if (submissionIDs and submission.get('submissionID') not in submissionIDs):
                    continue  # Skip if submissionID doesn't match
                if (usernames and submission.get('username') not in usernames):
                    continue  # Skip if username doesn't match
                if (assignmentIDs and submission.get('assignmentID') not in assignmentIDs):
                    continue  # Skip if assignmentID doesn't match

                filtered_submissions.append(submission)

            return filtered_submissions
        except Exception as e:
            print(f"Error reading assignments: {e}")
            return False

    def deleteSubmission(self, submissionIDs: list[str]):
        try:
            for id in submissionIDs:
                result = firebase.delete('/TestFolder2', id)
            return True
        except Exception as e:
            return False