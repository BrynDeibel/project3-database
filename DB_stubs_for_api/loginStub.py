import sys
sys.path.append("..")
from DB_Interfaces.loginInterface import *

class loginImplStub(LoginInterface):
    def login(self, username,password):
        return "Admin"