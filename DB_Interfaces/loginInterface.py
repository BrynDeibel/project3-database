from abc import ABC, abstractmethod #abstract base class
from ..Enums.RoleEnum import UserRole

class LoginInterface(ABC):
    @abstractmethod
    def login(username: str, password: str):
        pass