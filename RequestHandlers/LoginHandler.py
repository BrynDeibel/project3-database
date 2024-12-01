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
        try:

            user = self.interface.login(username,password)

            if user == "login failed":
                return {"status":"failure","message":"Invalid Creds"}, 401 #good request, lack of auth
            if user:
                return {"status":"success","role":user}, 200 # successful login
            
            #No content just in case
            return {"status":"failure","message":"No content"},204
        except ValueError as ve:
            return {"status":"error","message":"Bad Request"}, 400 #bad input, bad request
        
        except Exception as e:
            return {"status":"error","message":"Server error"}, 500 # Server side error