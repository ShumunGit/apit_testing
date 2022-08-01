from models.baseObject import baseObj
class User(baseObj):
    def __init__(self, id: int, username: str, firstName: str, lastName: str, email: str, password: str, phone: str, userStatus: int):
        self._id = id
        self._username = username
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._password = password
        self._phone = phone
        self._userStatus= userStatus


    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, Id: int):
        self._id = Id

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, username: str):
        self._username = username

    @property
    def firstName(self) -> str:
        return self._firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self._firstName = firstName

    @property
    def lastName(self) -> str:
        return self._lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self._lastName = lastName

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        self._phone = phone

    @property
    def userStatus(self) -> int:
        return self._userStatus

    @userStatus.setter
    def userStatus(self, userStatus: str):
        self._userStatus = userStatus










