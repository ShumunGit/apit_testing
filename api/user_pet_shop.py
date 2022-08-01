import requests, json


class user_api:
    def __init__(self, url_path="https://petstore3.swagger.io/api/v3"):
        self._url_path = url_path
        self.headrs = {'accept': '*/*'}
        self.session = requests.session()
        self.session.headers.update(self.headrs)

    def post_create_new_user(self) -> dict:
        new_user = {"id": 100001, "username": "The_mon", "firstName": "Alexx", "lastname": "James", "email": "Alex@gmail.com",
                    "password": "12345", "phone": "12345", "userStatus": 1}
        res = self.session.post(url=f"{self._url_path}/user", data=new_user)
        if res.status_code == 200:
            return res.json()
        else:
            return res.content

    # Error 500.
    def post_list_of_users(self):
       new_user = {"id": 14, "username": "theUuuuser", "firstName": "Joooohn",
                "lastName": "James", "email": "joooohn@email.com", "password": "12222345",
                "phone": "12345", "userStatus": 1}
       lst_users = json.dumps(list(new_user))
       res = self.session.post(url=f"{self._url_path}/user/createWithList", data=lst_users)
       return res.content

    def get_login_user_into_system(self, user="The_moon", passWord="12345"):
        res = self.session.get(url=f"{self._url_path}/user/login?username={user}&password={passWord}")
        if res.status_code == 200:
            return res.content
        else:
            return res.status_code

    def get_user_logged_out(self, user="The_moon", passWord="12345"):
        res = self.session.get(url=f"{self._url_path}/user/logout?username={user}&password={passWord}")
        if res.status_code == 200:
            return res.content
        else:
            return res.content

    def get_user_by_username(self, username="The_moon"):
        res = self.session.get(url=f"{self._url_path}/user/{username}")
        if res.status_code == 200:
            return res.content
        else:
            return res.status_code

    # 500 code
    def put_update_exsit_user(self, username="The_moon"):
        updated_user = {"id": 100001, "username": "The_moon", "firstName": "Alexx", "lastname": "James", "email": "Alex@gmail.com",
                    "password": "12345", "phone": "12345", "userStatus": 1}
        res = self.session.put(url=f"{self._url_path}/user/The_mon", data=updated_user)
        return res.content

    def delete_user_by_username(self, user="The_moon"):
        res = self.session.delete(url=f"{self._url_path}/user/{user}")
        if res.status_code == 200:
            return res.content
        else:
            return res.status_code

user = user_api()
print(user.post_create_new_user())
print(user.put_update_exsit_user())
