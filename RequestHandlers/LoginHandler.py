from abc import ABC, abstractmethod


import sys
sys.path.append('..')
from DB_Interfaces.loginInterface import *

class LoginHandlerInterface(ABC):
    @abstractmethod
    def handleLogin(self,username,password):
        pass

class LoginHandler(LoginHandlerInterface):
    def __init__(self,interface: LoginInterface):
        self.interface = interface
    def handleLogin(self,username,password):
        user = self.interface.login(username,password)

        if user == "login failed":
            return {"status":"failure","message":"Invalid Creds"}
        else:
            return {"status":"success"}
