from api.pet_api import pet_api
from models.pet import Pet
import pytest, logging, json

pet = pet_api()
@pytest.fixture()
def get_available_pet():
    # choose value : available, pending, sold
    status_options = ["available", "pending", "sold"]
    available_pets = pet.get_pet_by_status(status_options[0])
    if available_pets == 400:
        return "invalid status value"
    return available_pets[0]

def test_update_exsiting_pet(get_available_pet):
    # validate if pet.
    if type(get_available_pet) != type("abc"):
        # set to pet new name.
        get_available_pet["name"] = "Roxy"
        # update the pet.
        res = pet.put_update_existing_pet(get_available_pet)
        if type(res) != type("abc"):
            updated_pet = Pet(**res)
            assert updated_pet.name == "Roxy", logging.error("roxy name not match")
            logging.info("pet name is updated")
        else:
            logging.info(res)
    else:
        logging.error(get_available_pet)


def test_get_by_id(get_available_pet):
    if type(get_available_pet) != type("abc"):
        pet_id = get_available_pet["id"]
        res = pet.get_pet_by_id(pet_id)
        if type(res) != type("abc"):
            my_pet = Pet(**res)
            assert my_pet._id == pet_id, logging.error("pet id number {} is not found".format(pet_id))
            logging.info("found the pet by id number {}".format(pet_id))
        else:
            logging.error(res)
    else:
        logging.error(get_available_pet)


def test_post_new_pet():
    new_pet = {"id": "20", "name": "bimbo", "category": {"id": 1, "name": "Dogs"}, "status": "available"}
    # delete the pet if exits.
    pet_id = int(new_pet["id"])
    # delete pet if exist.
    delete_pet = pet.delete_pet_by_id(pet_id)
    if delete_pet == f"Pet number {pet_id} deleted":
        # post new object pet.
        res = pet.post_new_pet(new_pet)
        if type(res) != type("abc"):
            # validate the new pet.
            res_pet = Pet(**res)
            assert res_pet._id == pet_id, logging.error("pet not found")
            logging.info("bimbo is added to the store")
        else:
            logging.error(res)
    else:
        logging.error(delete_pet)


def test_find_by_status():
    # choose value : available, pending, sold
    status_options = ["available", "pending", "sold"]
    chose_status = status_options[0]

    # request the pet list.
    res = pet.get_pet_by_status(chose_status)
    # validate request response list or error.
    if type(res) != type("abc"):
        # new objects pets list.
        lst_pets = []
        for pets in res:
            add_pet = Pet(**pets)
            lst_pets.append(add_pet)
        # validate the status of the objects list.
        for i in range(len(lst_pets)):
            assert lst_pets[i].status == chose_status, logging.error("pet id {}, is status: {}".format(lst_pets[i].name, lst_pets[i].status))
        logging.info("all the pets in the list have a statu: {}".format(chose_status))
    else:
        logging.error(res)
def test_post_pet_by_id(get_available_pet):
    if type(get_available_pet) != type("abc"):
        pet_id = int(get_available_pet["id"])
        pet_name = "Bimbo"
        pet_status = get_available_pet["status"]
        res = pet.post_pet_by_id(pet_id, pet_name, pet_status)
        if type(res) != type("abc"):
            updated_pet = Pet(**res)
            assert updated_pet._name == pet_name and updated_pet._id == pet_id and updated_pet._status == pet_status, logging.error("name is not updated")
            logging.info(f"pet name is updated to {updated_pet.name}")
        else:
            logging.error(res)


def test_delete_pet_by_id():
    dummy_pet = {"id": 55345435, "name": "bimbo", "category":  {"id": 13322444, "name": "Dogs"}, "status": "available"}
    # post new pet to be deleted.
    post_dummy = pet.post_new_pet(dummy_pet)
    if type(post_dummy) != type("abc"):
        dummy_id = post_dummy["id"]
        res = pet.delete_pet_by_id(dummy_id)
        assert res == 'Pet number {} deleted'.format(dummy_pet["id"]), logging.error(res)
        logging.info(res)
    else:
        logging.error(post_dummy)

def test_get_pet_by_tags(get_available_pet):
    # get tag name and tage id from available pet.
    # tag_id = get_available_pet["tags"][0]["id"]
    # tag_name = get_available_pet["tags"][0]["name"]
    print(get_available_pet["tags"])
    """
        res = pet.get_pet_by_tags(tag_id, tag_name)
    if type(res) != type("abc"):
        pet_with_tags = Pet(**res)
        assert pet_with_tags._tags[0]["id"] == tag_id and pet_with_tags._tags[0]["name"] == tag_name, logging.error("pet with not tags")
        logging.info("pet with tags")
    else:
        logging.error(res)
    """


def test_post_upload_img_by_id(get_available_pet):
    pet_id = get_available_pet["id"]
    meta_data = "cute dog"
    # image path from models/images.
    peth_img = 'models/images/couteDog.jpg'
    file = {}
    # red the file.
    with open(peth_img, 'rb') as img:
        img_file = img.read()
        file["file"] = img_file
    res = pet.post_upload_img_by_id(pet_id, meta_data, file)
    if type(res) != type("abc"):
        pet_with_img = Pet(**res)
        assert file["file"] not in pet_with_img, logging.error("pet not include image")
        logging.info("pet include image")
    else:
        logging.info(res)
