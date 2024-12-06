from abc import ABC, abstractmethod #abstract base class
from Enums.RoleEnum import UserRole

class UserDTO():
    def __init__(self, username: str, password: str, role: UserRole, name: str):
        self.username = username
        self.password = password
        self.role = role
        self.name = name

class UserInterface(ABC):
    @abstractmethod
    def createUser(self, userDTO: UserDTO):
        pass
    @abstractmethod
    def updateUser(self, userDTO: UserDTO):
        pass
    @abstractmethod
    def getUsers(self, usernames: list[str] = None) -> list[UserDTO]:
        pass
    @abstractmethod
    def deleteUser(self, username):
        pass