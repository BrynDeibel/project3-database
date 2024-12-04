import sys
from firebase import firebase
import hashlib
sys.path.append("..")
from DB_Interfaces.loginInterface import LoginInterface
from Enums.RoleEnum import UserRole


firebase = firebase.FirebaseApplication('https://database-team-project3-default-rtdb.firebaseio.com', None)


class LoginInterfaceFirebase(LoginInterface):
    def login(self, username: str, password: str):
        try:
            # hash for comparison
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            user_data = firebase.get('/Users', username)
            if not user_data:
                return "login failed"

            if user_data['password'] == hashed_password:
                return {'role':user_data['role'], 'name':user_data['name']}  # return the role as success response

            return "login failed"
        except Exception as e:
            raise Exception(f"Error during login: {str(e)}")
