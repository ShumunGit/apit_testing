import requests, json


class user_api:
    def __init__(self, url_path="https://petstore3.swagger.io/api/v3"):
        self._url_path = url_path
        self.headrs = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headrs)

    def post_create_new_user(self, new_user) -> dict or str:

        res = self.session.post(url=f"{self._url_path}/user", data=new_user)
        if res.status_code == 200:
            return res.json()
        else:
            return res.json()["message"]

    def post_list_of_users(self, new_user: list) -> list or str:
        res = self.session.post(url=f"{self._url_path}/user/createWithList", data=f"{new_user}")
        if res.status_code == 200:
            return res.json()
        else:
            return res.json()["message"]

    def get_login_user_into_system(self, user, passWord):
        res = self.session.get(url=f"{self._url_path}/user/login?username={user}&password={passWord}")
        if res.status_code == 200:
            return res.content
        else:
            return res.json()["message"]

    def get_user_logged_out(self, user: str, passWord: str) -> str:
        res = self.session.get(url=f"{self._url_path}/user/logout?username={user}&password={passWord}")
        if res.status_code == 200:
            return res.content
        else:
            return res.json()["message"]

    def get_user_by_username(self, username: str) -> dict or str:
        res = self.session.get(url=f"{self._url_path}/user/{username}")
        if res.status_code == 200:
            return res.content
        else:
            return res.json()["message"]

    # 500 code
    def put_update_exsit_user(self, user_name, updated_user: dict):
        res = self.session.put(url=f"{self._url_path}/user/{user_name}", data=updated_user)

        if res.status_code == 200:
            return res.content
        else:
            return res.json()["message"]

    def delete_user_by_username(self, user: str) -> str:
        res = self.session.delete(url=f"{self._url_path}/user/{user}")
        if res.status_code == 200:
            return res.content
        else:
            return res.json()["message"]





