from abc import ABC, abstractmethod
import asyncio
import sys
from flask import json, jsonify
sys.path.append('..')
from DB_Interfaces.assignmentInterface import *


class AssignmentHandlerInterface(ABC):
    @abstractmethod
    async def handleGET(self, args: dict):
        pass
    @abstractmethod
    async def handlePOST(self, data: json):
        pass
    @abstractmethod
    async def handlePUT(self, args:dict, data: json):
        pass
    @abstractmethod
    async def handleDELETE(self, args: dict):
        pass

class AssignmentHandlerImpl(AssignmentHandlerInterface):
    def __init__ (self, interface: AssignmentInterface):
        self.interface = interface
    async def handleGET(self, args: dict): #In the real handler, the json would be read and processed to call the function
        arg = None
        #Read in the ids
        if (args.get('ids') != None):
            arg = args.get('ids')
            arg = arg.replace('[', '')
            arg = arg.replace(']', '')
            arg = arg.split(',')
        try:
            result = await self.interface.readAssignments(arg)
            if result == None:
                return jsonify(), 200
            #convert the results in a dictionary that can be put into a json
            assigns = []
            
            for assignment in result:
                newDict = {
                    'id': assignment.id,
                    'name': assignment.name,
                    'dueDate': assignment.duedate,
                    'description': assignment.description,
                    'numberOfPoints': assignment.numberOfPoints,
                    'instructorUsername': assignment.instructorUsername,
                    'inputs': assignment.inputs, #an array of strings
                    'outputs': assignment.outputs #an array of strings
                }
                assigns.insert(len(assigns), newDict)
            ret = {'assignments': assigns}
            return jsonify(ret), 200
        except Exception as e:
            return jsonify({'error': e.args}), 500
        

    async def handlePOST(self, data: json):
        #read in the data to a DTO object

        try:
            dto = AssignmentDTO(data['name'], data['dueDate'], data['description'], data['numberOfPoints'], data['instructorUsername'], data['inputs'], data['outputs'])
        except Exception as e:
            return jsonify({'error': e.args}), 400 #bad request
        
        try:
            ret = await self.interface.createAssignment(dto)
            
            return jsonify({'id': ret}), 200
        except Exception as e:
            return jsonify({'error': e.args}), 500
        

    async def handlePUT(self, args: dict, data: json):
        #read in the data to a DTO object

        try:
            dto = AssignmentDTO(data['name'], data['dueDate'], data['description'], data['numberOfPoints'], data['instructorUsername'], data['inputs'], data['outputs'], args['id'])
        except Exception as e:
            return jsonify({'error': e.args}), 400 #bad request
        
        try:
            await self.interface.updateAssignment(dto)
            
            return jsonify(), 200
        except Exception as e:
            return jsonify({'error': e.args}), 500
        
    async def handleDELETE(self, args: dict):
        arg = None
        #Read in the ids
        if (args.get('ids') != None):
            arg = args.get('ids')
            arg = arg.replace('[', '')
            arg = arg.replace(']', '')
            arg = arg.split(',')
        try:
            await self.interface.deleteAssignment(arg)
            return jsonify(), 200
        except Exception as e:
            return jsonify({'error': e.args}), 500