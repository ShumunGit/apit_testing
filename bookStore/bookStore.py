import requests
from requests.auth import HTTPBasicAuth

"""
  data = {
              "userName": "tamir",
              "password": "Aa123456@"
            }
    tamir_userid = "9f320d3b-c5f3-4fbe-960f-f5ff087acb2d"
"""


class book_store_api:
    def __init__(self,  url='https://bookstore.toolsqa.com/Account/v1'):
        self._url_path_pet = url
        self.headrs = {'accept': 'application/json'}
        self._authreization = HTTPBasicAuth('selaUser', 'Aa123456@')
        self._user = '860189b4-4a95-4e96-8079-4a4f69ea3a0b'

    def _Bearer_token(self):
        selaUser = {"userName": "selaUser",
                    "password": "Aa123456@"}
        sela_user_id = '860189b4-4a95-4e96-8079-4a4f69ea3a0b'
        new_token = requests.post(url=f"{self._url_path_pet}/GenerateToken", data=selaUser, headers=self.headrs)
        sela_token = new_token.json()["token"]
        my_headers = {'Authorization': f'Bearer {sela_token}', 'accept': 'application/json'}
        res = requests.get(url=f"{self._url_path_pet}/User/{self._user}", headers=my_headers)
        return my_headers

    def get_request(self):
        res = requests.get(url=f"{self._url_path_pet}/User/{self._user}", auth=self._authreization, headers=self.headrs)
        if res.status_code == 200:
            return res.json()
        else:
            res.json()

    def get_account(self):
        res = requests.get(url=f"{self._url_path_pet}/User/{self._user}", headers=self.headrs, auth=self._authreization)
        if res.status_code == 200:
            return res.json()
        else:
            return res.content

    def post_Authorized(self):
        sela_user = {"userName": "selaUser", "password": "Aa123456@"}
        res = requests.post(url=f"{self._url_path_pet}/Authorized", headers=self.headrs, data=sela_user)

        if res.status_code == 200:
            return res.json()
        else:
            return res.json()["message"]

    def post_GenerateToken(self):
        sela_user = {"userName": "selaUser", "password": "Aa123456@"}
        res = requests.post(url=f"{self._url_path_pet}/GenerateToken", headers=self.headrs, data=sela_user)
        if res.status_code == 200:
            return res.json()
        else:
            return res.json()["message"]

    def post_User(self):
        sela_user = {"userName": "shumun", "password": "Aa123456@"}
        res = requests.post(url=f"{self._url_path_pet}/User", headers=self.headrs, data=sela_user)

        if res.status_code == 200:
            return res.json()
        else:
            return res.json()["message"]

    def delete_uuid(self,  uuid='1301254e-d055-4756-9de0-5476bf7397ab'):
        res = requests.delete(url=f"{self._url_path_pet}/User/{uuid}", headers=self.headrs)

        if res.status_code == 200:
            return res.json()
        else:
            return res.json()["message"]

    def get_uuid(self,  uuid='1301254e-d055-4756-9de0-5476bf7397ab'):
        res = requests.get(url=f"{self._url_path_pet}/User/{uuid}", headers=self.headrs)

        if res.status_code == 200:
            return res.json()
        else:
            return res.json()["message"]


user = book_store_api()
print(user.get_uuid())