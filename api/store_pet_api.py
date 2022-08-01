from api.pet_api import pet_api
import json, requests


class store_pet_api:
    def __init__(self, url_path="https://petstore3.swagger.io/api/v3"):
        self._url_path_pet = url_path
        self.headrs = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headrs)

    # return pet inventory by status.
    def get_pet_inventory(self) -> dict or str:
        res = self.session.get(url=f"{self._url_path_pet}/store/inventory")
        if res.status_code == 200:
            return res.json()
        else:
            return res.json()["message"]

    # place an order for a pet.
    def post_new_order(self, order_details: dict) -> dict or int:
        res = self.session.post(url=f"{self._url_path_pet}/store/order", data=order_details)
        if res.status_code == 200:
            return res.json()
        else:
            return res.json()["message"]

    # find purchase orders by order id.
    def get_purchase_by_order_id(self, order_id: int):
        res = self.session.get(url=f"{self._url_path_pet}/store/order/{order_id}")
        if res.status_code == 200:
            return res.json()
        else:
            return res.json()["message"]


    # delete purchase order by id.
    def delete_purchase_order_by_id(self, order_id):
        res = self.session.delete(url=f"{self._url_path_pet}/store/order/{order_id}")
        if res.status_code == 200:
            return 'purchase is deleted'
        else:
            return res.json()["message"]

store = store_pet_api()


