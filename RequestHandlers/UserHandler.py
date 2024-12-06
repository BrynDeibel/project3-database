from abc import ABC, abstractmethod
import sys
sys.path.append('..')
from DB_Interfaces.userInterface import UserDTO, UserInterface
from Enums.RoleEnum import UserRole


class UserHandlerInterface(ABC):
    @abstractmethod
    def handleGET(self, args: dict):
        pass

    @abstractmethod
    def handlePOST(self, data: dict):
        pass

    @abstractmethod
    def handlePATCH(self, args: dict, data: dict):
        pass

    @abstractmethod
    def handleDELETE(self, args: dict):
        pass


class UserHandler(UserHandlerInterface):
    def __init__(self, interface: UserInterface):
        self.interface = interface

    def handleGET(self, args: dict):
        try:
            arg = None
            #Read in the usernames
            if (args.get('usernames') != None):
                arg = args.get('usernames')
                arg = arg.replace('[', '')
                arg = arg.replace(']', '')
                arg = arg.split(',')
            users = self.interface.getUsers(arg)
            result = [{'username': user.username, 'role': user.role.name, 'name': user.name} for user in users]
            return {'users': result}
        except Exception as e:
            return {'error': str(e)}

    def handlePOST(self, data: dict):
        try:
            userDTO = UserDTO(data['username'], data['password'], UserRole[data['role'].upper()], data['name'])
            self.interface.createUser(userDTO)
            return {'status': 'success', 'message': 'User created successfully'}
        except KeyError:
            return {'status': 'failure', 'message': 'Invalid role provided'}
        except Exception as e:
            return {'status': 'failure', 'message': str(e)}

    def handlePATCH(self, args: dict, data: dict):
        try:
            userDTO = UserDTO(args['username'], None, UserRole[data['role'].upper()], data['name'])
            self.interface.updateUser(userDTO)
            return {'status': 'success', 'message': 'User patched successfully'}
        except KeyError:
            return {'status': 'failure', 'message': 'Invalid role provided'}
        except Exception as e:
            return {'status': 'failure', 'message': str(e)}
        
    def handleDELETE(self, args: dict):
        try:
            arg = None
            #Read in the usernames
            if (args.get('usernames') != None):
                arg = args.get('usernames')
                arg = arg.replace('[', '')
                arg = arg.replace(']', '')
                arg = arg.split(',')
            self.interface.deleteUser(arg)
            return {'status': 'success', 'message': 'User(s) deleted successfully'}
        except Exception as e:
            return {'status': 'failure', 'message': str(e)}
