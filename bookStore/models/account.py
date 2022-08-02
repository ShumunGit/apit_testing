
class UserAccount:
    def __int__(self, username: str):
        self._username = username
    def username(self):
        return self._username

user2 = UserAccount()
print(user2.username())