from api.store_pet_api import store
import pytest, logging, json
import datetime
from api.pet_api import pet_api


def test_get_pet_inventory():
    res = store.get_pet_inventory()
    res_approved = res["approved"]
    res_delivered = res["delivered"]
    assert res["approved"] == res_approved and res["delivered"] == res_delivered, logging.warning(res)
    logging.info("store inventory is checked")


@pytest.fixture()
def set_neworder():
    today = datetime.datetime.now()
    pet = pet_api()
    first_pet = pet.get_pet_by_status("available")
    pet_id = first_pet[0]["id"]
    order_details = {"id": pet_id, "petId": {pet_id*2}, "quantity": 7, "shipDate": f"{today}",
                    "status": "approved", "complete": True}

    return order_details


def test_post_new_order(set_neworder):
    pet_id = set_neworder["id"]
    res = store.post_new_order(set_neworder)
    assert res["id"] == set_neworder["id"], logging.warning(res)
    logging.info(f"order number {pet_id} is shipped for today")


def test_get_purchase_by_order_id(set_neworder):
    new_purchase = store.post_new_order(set_neworder)
    purchase_id = new_purchase["id"]
    res = store.get_purchase_by_order_id(purchase_id)
    assert res["id"] == purchase_id, logging.warning("id not found")
    logging.info(f"purchase number {purchase_id}, is founded")


def test_delete_purchase_order_by_id(set_neworder):
    new_purchase = store.post_new_order(set_neworder)
    purchase_id = new_purchase["id"]
    res = store.delete_purchase_order_by_id(purchase_id)
    assert res == "purchase is deleted", logging.warning("id not found")
    logging.info(f"purchase id number: {purchase_id} is deleted")

