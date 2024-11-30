from abc import ABC, abstractmethod
import sys
sys.path.append('..')
from DB_Interfaces.userInterface import UserDTO, UserInterface
from Enums.RoleEnum import UserRole


class UserHandlerInterface(ABC):
    @abstractmethod
    def handleGET(self, usernames: list[str]):
        pass

    @abstractmethod
    def handlePOST(self, data: dict):
        pass

    @abstractmethod
    def handleDELETE(self, usernames: list[str]):
        pass


class UserHandler(UserHandlerInterface):
    def __init__(self, interface: UserInterface):
        self.interface = interface

    def handleGET(self, usernames: list[str]):
        try:
            users = self.interface.getUsers(usernames)
            result = [{'username': user.username, 'role': user.role.name} for user in users]
            return {'users': result}
        except Exception as e:
            return {'error': str(e)}

    def handlePOST(self, data: dict):
        try:
            userDTO = UserDTO(data['username'], data['password'], UserRole[data['role'].upper()])
            self.interface.createUser(userDTO)
            return {'status': 'success', 'message': 'User created successfully'}
        except KeyError:
            return {'status': 'failure', 'message': 'Invalid role provided'}
        except Exception as e:
            return {'status': 'failure', 'message': str(e)}

    def handleDELETE(self, usernames: list[str]):
        try:
            self.interface.deleteUser(usernames)
            return {'status': 'success', 'message': 'User(s) deleted successfully'}
        except Exception as e:
            return {'status': 'failure', 'message': str(e)}
