from api.pet_api import pet_api
import pytest, logging


def test_get_by_id():
    pet = pet_api()
    res = pet.get_pet_by_id(8)

    assert res["id"] == 8, logging.warning("pet is not found")
    logging.info("Rocky is a pet")


def test_post_new_pet():
    pet_category = {"id": 1, "name": "Dogs"}
    new_obj = {"id": 5, "name": "bimbo", "category": pet_category, "status": "available"}
    pet = pet_api()
    res = pet.post_new_pet(new_obj)
    get_new_obj = pet.get_pet_by_id(5)
    assert res["id"] == get_new_obj["id"], logging.warning("pet not found")
    logging.info("bimbo is added to the store")