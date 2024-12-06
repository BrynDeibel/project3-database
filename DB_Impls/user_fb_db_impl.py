import sys
from firebase import firebase
import hashlib
sys.path.append("..")
from DB_Interfaces.userInterface import UserDTO, UserInterface
from Enums.RoleEnum import UserRole


firebase = firebase.FirebaseApplication('https://database-team-project3-default-rtdb.firebaseio.com', None)


class UserInterfaceFirebase(UserInterface):
    def createUser(self, userDTO: UserDTO):
        try:
            # hash password before storing
            hashed_password = hashlib.sha256(userDTO.password.encode()).hexdigest()

            user_data = {
                'password': hashed_password,
                'role': userDTO.role.name,
                'name': userDTO.name
            }
            firebase.put('/Users', userDTO.username, user_data)
        except Exception as e:
            raise Exception(f"Error creating user: {str(e)}")

    def updateUser(self, userDTO: UserDTO):
        try:
            user_data = {
                'name': userDTO.name,
                'role': userDTO.role.name
            }
            get = firebase.get('/Users', userDTO.username)
            if (get):
                firebase.patch(('/Users/' + userDTO.username), user_data)
            else:
                raise Exception(f"User does not exist")
        except Exception as e:
            raise Exception(f"Error patching user: {str(e)}")
    
    def getUsers(self, usernames: list[str] = None) -> list[UserDTO]:
        try:
            users = []
            if usernames is None:
                # retrieve all users
                all_users = firebase.get('/Users', '')
                if all_users:
                    for username, data in all_users.items():
                        user_role = UserRole[data['role'].upper()]
                        users.append(UserDTO(username, None, user_role, data['name']))
            else:
                # retrieve specific users
                for username in usernames:
                    user_data = firebase.get('/Users', username)
                    if user_data:
                        user_role = UserRole[user_data['role'].upper()]
                        users.append(UserDTO(username, None, user_role, user_data['name']))
            return users
        except Exception as e:
            raise Exception(f"Error retrieving users: {str(e)}")

    def deleteUser(self, usernames: list[str]):
        try:
            for username in usernames:
                firebase.delete('/Users', username)
        except Exception as e:
            raise Exception(f"Error deleting user: {str(e)}")
