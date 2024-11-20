from abc import ABC, abstractmethod

import sys
sys.path.append('..')
from DB_Interfaces.assignmentInterface import *


class AssignmentHandlerInterface(ABC):
    @abstractmethod
    def handleReadAssignment(self, json):
        pass

class AssignmentHandlerStub(AssignmentHandlerInterface):
    def __init__ (self, interface: AssignmentInterface):
        self.interface = interface
    def handleReadAssignment(self, json): #In the real handler, the json would be read and processed to call the function
        ret = self.interface.readAssignments()
        return ret