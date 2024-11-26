from abc import ABC, abstractmethod
import asyncio
import sys
from flask import json, jsonify
sys.path.append('..')
from DB_Interfaces.submissionInterface import *


class SubmissionHandlerInterface(ABC):
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

class SubmissionHandlerImpl(SubmissionHandlerInterface):
    def __init__ (self, interface: SubmissionInterface):
        self.interface = interface
    async def handleGET(self, args: dict): #In the real handler, the json would be read and processed to call the function
        sIds = None
        #Read in the ids
        if (args.get('submissionIds') != None):
            sIds = args.get('submissionIds')
            sIds = sIds.replace('[', '')
            sIds = sIds.replace(']', '')
            sIds = sIds.split(',')
        usernames = None
        #Read in the ids
        if (args.get('usernames') != None):
            usernames = args.get('usernames')
            usernames = usernames.replace('[', '')
            usernames = usernames.replace(']', '')
            usernames = usernames.split(',')
        aIds = None
        #Read in the ids
        if (args.get('assignmentIds') != None):
            aIds = args.get('assignmentIds')
            aIds = aIds.replace('[', '')
            aIds = aIds.replace(']', '')
            aIds = aIds.split(',')
        try:
            result = await self.interface.readSubmissions(sIds, usernames, aIds)
            if result == None:
                return jsonify(), 200
            #convert the results in a dictionary that can be put into a json
            subs = []
            for submission in result:
                newDict = {
                    "assignmentID": submission.assignmentID,
                    "score": submission.score,
                    "submissionId": submission.id,
                    "studentUsername": submission.studentUsername,
                    "submissionTime": submission.submissionTime
                }
                subs.insert(len(subs), newDict)
            ret = {'submissions': subs}
            return jsonify(ret), 200
        except Exception as e:
            return jsonify({'error': e.args}), 500
        

    async def handlePOST(self, data: json):
        #read in the data to a DTO object

        try:
            dto = SubmissionDTO(data['assignmentID'], data['studentUsername'], data['submissionTime'], data['score'])
        except Exception as e:
            return jsonify({'error': e.args}), 400 #bad request
        
        try:
            ret = await self.interface.createSubmission(dto)
            
            return jsonify({"id:": ret}), 200
        except Exception as e:
            return jsonify({'error': e.args}), 500
        

    async def handlePUT(self, args: dict, data: json):
        #read in the data to a DTO object

        try:
            dto = SubmissionDTO(data['assignmentID'], data['studentUsername'], data['submissionTime'], data['score'], args['id'])
        except Exception as e:
            return jsonify({'error': e.args}), 400 #bad request
        
        try:
            await self.interface.updateSubmission(dto)
            
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
            await self.interface.deleteSubmission(arg)
            return jsonify(), 200
        except Exception as e:
            return jsonify({'error': e.args}), 500