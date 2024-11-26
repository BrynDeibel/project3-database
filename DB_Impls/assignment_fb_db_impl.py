import asyncio
import sys
from DB_Interfaces.assignmentInterface import AssignmentDTO, AssignmentInterface
from firebase import firebase
sys.path.append('..')
from DB_Interfaces.assignmentInterface import *


firebase = firebase.FirebaseApplication('https://database-team-project3-default-rtdb.firebaseio.com', None)

class AssignmentInterfaceFirebase(AssignmentInterface):
    async def createAssignment(self, assignment: AssignmentDTO) -> str:
        result = await asyncio.to_thread(
            firebase.post,
            '/AssignmentsFolder',
            {'name': assignment.name,
                'duedate': assignment.duedate,
                'description': assignment.description,
                'numberOfPoints': assignment.numberOfPoints,
                'instructorUsername': assignment.instructorUsername,
                'inputs': assignment.inputs,
                'outputs': assignment.outputs}
        )
        return result['name']

    async def updateAssignment(self, assignment: AssignmentDTO) -> str:
            result = await asyncio.to_thread(
                firebase.put,
                '/AssignmentsFolder',
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
    
    async def readAssignments(self, assignmentIDs: list[str] = None) -> list[AssignmentDTO]:
        if assignmentIDs is None:
            result = await asyncio.to_thread(firebase.get, "/AssignmentsFolder", "")
            assignments = []
            if result:
                for r in result:
                    if result[r]:
                        dto = AssignmentDTO(**result[r])
                        dto.id = r
                        assignments.append(dto)
            return assignments
        else:
            assignments = []
            for id in assignmentIDs:
                result = await asyncio.to_thread(firebase.get, "/AssignmentsFolder", id)
                if result:
                    dto = AssignmentDTO(**result)
                    dto.id = id
                    assignments.append(dto)
            return assignments

    async def deleteAssignment(self, assignmentIDs: list[str]) -> str:
        for id in assignmentIDs:
            await asyncio.to_thread(firebase.delete, '/AssignmentsFolder', id)
        return "Deleted successfully"
