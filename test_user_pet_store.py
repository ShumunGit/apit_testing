import pytest, logging, json
from api.user_pet_shop import user_api
user = user_api()
@pytest.fixture
def get_new_user():
    new_user = {"id": 1001, "username": "The_mooon", "firstName": "Alexxxx", "lastName": "Jaaames",
                "email": "Alexxx@gmail.com",
                "password": "12345", "phone": "12345", "userStatus": 1}
    return new_user
def test_post_create_new_user():
    new_user = {"id": 1001, "username": "The_mooon", "firstName": "Alexxxx", "lastName": "Jaaames",
                "email": "Alexxx@gmail.com",
                "password": "12345", "phone": "12345", "userStatus": 1}
    res = user.post_create_new_user(new_user)
    if type(res) != type("abc"):
        assert res["id"] == get_new_user["id"], logging.error("user not been created")
        logging.info("user is created in the DB")
    else:
        logging.error(res)

def test_post_list_of_users(get_new_user):
    lst_users = [get_new_user]
    res = user.post_list_of_users(lst_users)
    if type(res) != type("abc"):
        assert len(res) == len(lst_users), logging.error("list is not created")
        logging.info("list of users created")
    else:
        logging.error(res)

def test_get_login_user_into_system():
    user_name = "The_moon"
    passWord = "12345"
    res = user.get_login_user_into_system(user_name, passWord)
    assert len(res[24:]) == 19, logging.error("user not logged in")
    logging.info("Logged in user")

def test_get_user_logged_out():
    user_name = "The_moon"
    passWord = "12345"
    login_user = user.get_login_user_into_system(user_name, passWord)
    if len(login_user[24:]) == 19:
        res = user.get_user_logged_out(user_name, passWord)
        assert len(res[12:]) == 3, logging.error("user not log out")
        logging.info("user logged out")
    else:
        logging.info(login_user)

def test_get_user_by_username():
    user_name = "theUser"
    res = user.get_user_by_username(user_name)
    if type(res) != type("abc"):
        res = json.loads(res)
        assert res["username"] == user_name, logging.error("user not founded")
        logging.info("user founded")
    else:
        logging.error(res)


def test_put_update_exsit_user():
    updated_user = {"id": 100001, "username": "The_moon", "firstName": "Alexx", "lastname": "James",
                    "email": "Alex@gmail.com",
                    "password": "12345", "phone": "12345", "userStatus": 1}
    res = user.put_update_exsit_user(updated_user["username"], updated_user)
    if type(res) != type("abc"):
        res = json.loads(res)
        assert res["username"] == updated_user["username"], logging.error("user not updated")
        logging.info("user is updated")
    else:
        logging.error(res)

def test_delete_user_by_username():
    user_name = "TheUser"
    res = user.delete_user_by_username(user_name)
    if type(res) != type("abc"):
        assert res == "", logging.error("user name not founded")
        logging.info("user is deleted")
    else:
        logging.error(res)