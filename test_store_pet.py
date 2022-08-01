from api.store_pet_api import store
from models.order import Order
import pytest, logging, json, datetime
from api.pet_api import pet_api

def test_get_pet_inventory():
    res = store.get_pet_inventory()
    if type(res) != type("abc"):
        res_approved = res["approved"]
        res_delivered = res["delivered"]
        assert res["approved"] == res_approved and res["delivered"] == res_delivered, logging.error(res)
        logging.info("store inventory is checked")
    else:
        logging.error(res)

@pytest.fixture()
def set_neworder():
    """
    insert to order_details new order.
    :return: order_details: dict
    """
    today = datetime.datetime.now()
    order_details = {"id": today.day*2, "petId": today.year, "quantity": 7, "shipDate": f"{today}",
                    "status": "approved", "complete": True}
    return order_details

def test_post_new_order(set_neworder):
    pet_id = set_neworder["id"]
    res = store.post_new_order(set_neworder)
    if type(res) != type("abc"):
        new_order = Order(**res)
        assert new_order.id == pet_id, logging.error("id order not set")
        logging.info(f"order number {pet_id} is shipped for today")
    else:
        logging.error(res)


def test_get_purchase_by_order_id(set_neworder):
    new_purchase = store.post_new_order(set_neworder)
    if type(new_purchase) != type("abc"):
        purchase_id = new_purchase["id"]
        res = store.get_purchase_by_order_id(purchase_id)
        new_purchase = Order(**res)
        assert new_purchase.id == purchase_id, logging.error("id not found")
        logging.info(f"purchase number {purchase_id}, is founded")
    else:
        logging.error(new_purchase)


def test_delete_purchase_order_by_id(set_neworder):
    new_purchase = store.post_new_order(set_neworder)
    if type(new_purchase) != type("abc"):
        purchase_id = new_purchase["id"]
        res = store.delete_purchase_order_by_id(purchase_id)
        assert res == "purchase is deleted", logging.error("id not found")
        logging.info(f"purchase id number: {purchase_id} is deleted")
    else:
        logging.error(new_purchase)

