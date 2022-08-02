import json
from bookStore.models.baseObject import baseObj

class UserAccount(baseObj):

    def __init__(self, userName: str, password: str):
        self._userName = userName
        self._password = password

    @property
    def userName(self) -> str:
        return self._userName

    @userName.setter
    def userName(self, userName: str):
        self._userName = userName

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password














