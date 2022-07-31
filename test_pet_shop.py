from api.pet_api import pet_api
import pytest, logging, json

pet = pet_api()


def test_update_exsiting_pet():
    available_pets = pet.get_pet_by_status("available")
    first_pet = available_pets[0]
    first_pet["name"] = "Roxy"
    res = pet.put_update_existing_pet(first_pet)
    assert res["name"] == "Roxy", logging.warning("roxy name not match")
    logging.info("pet name is updated")


def test_get_by_id():
    res = pet.get_pet_by_id(8)
    assert res["id"] == 8, logging.warning("pet is not found")
    logging.info("Rocky is a pet")


def test_post_new_pet():
    pet_category = {"id": 1, "name": "Dogs"}
    new_obj = {"id": 5, "name": "bimbo", "category": pet_category, "status": "available"}

    res = pet.post_new_pet(new_obj)
    get_new_obj = pet.get_pet_by_id(5)
    assert res["id"] == get_new_obj["id"], logging.warning("pet not found")
    logging.info("bimbo is added to the store")


def test_find_by_status():
    # Available values : available, pending, sold
    status_options = ["available", "pending", "sold"]

    res = pet.get_pet_by_status(status_options[0])

    if len(res) > 0:
        for pet_status in res:
            assert pet_status["status"] == status_options[0], logging.warning("list is empty")
            logging.info("pet index 0 is available")
    else:
        return res


def test_post_pet_by_id():
    available_pets = pet.get_pet_by_status("sold")
    first_pet_id = available_pets[0]["id"]
    res = pet.post_pet_by_id(first_pet_id, "Bimbo")
    assert res["name"] == "Bimbo", logging.warning(f"pet id number: {first_pet_id}, is not updated")
    logging.info(f"pet id number:{first_pet_id} updated")


def test_delete_pet_by_id():
    pet_category = {"id": 13322444, "name": "Dogs"}
    new_obj = {"id": 55345435, "name": "bimbo", "category": pet_category, "status": "available"}
    insert_pet = pet.post_new_pet(new_obj)
    pet_id = insert_pet["id"]
    res = pet.delete_pet_by_id(pet_id)

    assert res == f"Pet number {pet_id} deleted", logging.warning(res)
    logging.info(res)