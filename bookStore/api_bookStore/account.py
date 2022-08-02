import requests
from requests.auth import HTTPBasicAuth

class book_store_api:
    def __init__(self,  url='https://bookstore.toolsqa.com/Account/v1'):
        self._url_path_pet = url
        self.headrs = {'accept': 'application/json'}
        self._authreization = HTTPBasicAuth('selaUser', 'Aa123456@')
        self._user = '860189b4-4a95-4e96-8079-4a4f69ea3a0b'

    def post_Authorized(self, user: dict) -> bool or str:
        res = requests.post(url=f"{self._url_path_pet}/Authorized", headers=self.headrs, data=user)
        if res.status_code == 200:
            return True
        else:
            return res.json()

    def post_GenerateToken(self, user: dict) -> dict:
        res = requests.post(url=f"{self._url_path_pet}/GenerateToken", headers=self.headrs, data=user)
        if res.status_code == 200:
            return res.json()
        else:
            return res.json()

    def post_User(self, user: dict) -> dict or str:
        res = requests.post(url=f"{self._url_path_pet}/User", headers=self.headrs, data=user)
        if res.status_code == 200:
            return res.json()
        else:

            return res.json()

    def delete_uuid(self,  user: dict, uuid: str):
        new_token = requests.post(url=f"{self._url_path_pet}/GenerateToken", data=user, headers=self.headrs)
        user_token = new_token.json()["token"]
        user_headers = {'Authorization': f'Bearer {user_token}', 'accept': 'application/json'}

        res = requests.delete(url=f"{self._url_path_pet}/User/{uuid}", headers=user_headers)
        if res.status_code == 200:
            return res.status_code
        else:
            return res.json()

    def get_uuid(self, user: dict, uuid: str) -> dict:
        new_token = requests.post(url=f"{self._url_path_pet}/GenerateToken", data=user, headers=self.headrs)
        user_token = new_token.json()["token"]
        user_headers = {'Authorization': f'Bearer {user_token}', 'accept': 'application/json'}

        res = requests.get(url=f"{self._url_path_pet}/User/{uuid}", headers=user_headers)
        if res.status_code == 200:
            return res.json()
        else:
            return res.json()

    def _Bearer_token(self):
        selaUser = {"userName": "selaUser",
                    "password": "Aa123456@"}
        sela_user_id = '860189b4-4a95-4e96-8079-4a4f69ea3a0b'
        new_token = requests.post(url=f"{self._url_path_pet}/GenerateToken", data=selaUser, headers=self.headrs)
        sela_token = new_token.json()["token"]
        my_headers = {'Authorization': f'Bearer {sela_token}', 'accept': 'application/json'}
        res = requests.get(url=f"{self._url_path_pet}/User/{self._user}", headers=my_headers)
        return res.json()







