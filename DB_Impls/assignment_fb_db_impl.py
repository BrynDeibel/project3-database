import asyncio
from DB_Interfaces.assignmentInterface import AssignmentDTO, AssignmentInterface
from firebase import firebase


firebase = firebase.FirebaseApplication('https://database-team-project3-default-rtdb.firebaseio.com', None)

class AssignmentInterfaceFirebase(AssignmentInterface):
    async def createAssignment(self, assignment: AssignmentDTO) -> str:
        try:
            result = await asyncio.to_thread(
                firebase.post,
                '/TestFolder2',
                {'name': assignment.name,
                 'duedate': assignment.duedate,
                 'description': assignment.description,
                 'numberOfPoints': assignment.numberOfPoints,
                 'instructorUsername': assignment.instructorUsername,
                 'inputs': assignment.inputs,
                 'outputs': assignment.outputs}
            )
            return result['name']
        except Exception as e:
            print(f"Error creating assignment: {e}")
            return False

    async def updateAssignment(self, assignment: AssignmentDTO) -> str:
        try:
            result = await asyncio.to_thread(
                firebase.put,
                '/TestFolder2',
                assignment.id,
                {'name': assignment.name,
                 'duedate': assignment.duedate,
                 'description': assignment.description,
                 'numberOfPoints': assignment.numberOfPoints,
                 'instructorUsername': assignment.instructorUsername,
                 'inputs': assignment.inputs,
                 'outputs': assignment.outputs}
            )
            return result['name']
        except Exception as e:
            print(f"Error updating assignment: {e}")
            return False

    async def readAssignments(self, assignmentIDs: list[str] = None) -> list[AssignmentDTO]:
        try:
            if assignmentIDs is None:
                result = await asyncio.to_thread(firebase.get, "/TestFolder2", "")
                return result
            else:
                assignments = []
                for id in assignmentIDs:
                    result = await asyncio.to_thread(firebase.get, "/TestFolder2", id)
                    if result:
                        assignments.append(AssignmentDTO(**result))
                return assignments
        except Exception as e:
            print(f"Error reading assignments: {e}")
            return False

    async def deleteAssignment(self, assignmentIDs: list[str]) -> str:
        try:
            for id in assignmentIDs:
                await asyncio.to_thread(firebase.delete, '/TestFolder2', id)
            return "Deleted successfully"
        except Exception as e:
            print(f"Error deleting assignments: {e}")
            return False
