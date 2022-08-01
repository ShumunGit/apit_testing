import pytest, logging, json
from api.user_pet_shop import user_api
from models.user import User
user = user_api()
@pytest.fixture
def get_new_user():
    new_user = {"id": 1001, "username": "The_mooon", "firstName": "Alexxxx", "lastName": "Jaaames",
                "email": "Alexxx@gmail.com",
                "password": "12345", "phone": "12345", "userStatus": 1}
    return new_user

def test_post_create_new_user(get_new_user):
    res = user.post_create_new_user(get_new_user)
    if type(res) != type("abc"):
        created_user = User(**res)
        assert created_user.id == get_new_user["id"], logging.error("user not been created")
        logging.info("user is created in the DB")
    else:
        logging.error(res)
def test_post_list_of_users(get_new_user):
    lst_users = [get_new_user]
    res = user.post_list_of_users(lst_users)
    if type(res) != type("abc"):
        first_user = User(**res)
        assert first_user.id == lst_users[0]["id"], logging.error("list is not created")
        logging.info("list of users created")
    else:
        logging.error(res)

def test_get_login_user_into_system():
    dummy_user = {"id": 10,"username": "theUser",
    "firstName": "John",
    "lastName": "James",
    "email": "john@email.com",
    "password": "12345",
    "phone": "12345",
    "userStatus": 1
  }
    res = user.get_login_user_into_system(dummy_user["username"], dummy_user["password"])
    assert len(res[24:]) == 19, logging.error("user not logged in")
    logging.info("Logged in user")

def test_get_user_logged_out():
    dummy_user = {"id": 10, "username": "theUser",
                  "firstName": "John",
                  "lastName": "James",
                  "email": "john@email.com",
                  "password": "12345",
                  "phone": "12345",
                  "userStatus": 1
                  }
    login_user = user.get_login_user_into_system(dummy_user["username"], dummy_user["password"])
    if len(login_user[24:]) == 19:
        logged_user = User(**dummy_user)
        res = user.get_user_logged_out(logged_user.username, logged_user.password)
        assert len(res[12:]) == 3, logging.error("user not log out")
        logging.info("user logged out")
    else:
        logging.info(login_user)

def test_get_user_by_username():
    dummy_user = {"id": 10, "username": "theUser",
                  "firstName": "John",
                  "lastName": "James",
                  "email": "john@email.com",
                  "password": "12345",
                  "phone": "12345",
                  "userStatus": 1
                  }
    res = user.get_user_by_username(dummy_user["username"])
    if type(res) != type("abc"):
        get_user_by_id = User(**json.loads(res))
        assert get_user_by_id.username == dummy_user["username"], logging.error("user not founded")
        logging.info("user founded")
    else:
        logging.error(res)


def test_put_update_exsit_user():
    dummy_user = {"id": 10, "username": "theUser",
                  "firstName": "John",
                  "lastName": "James",
                  "email": "john@email.com",
                  "password": "12345",
                  "phone": "12345",
                  "userStatus": 1
                  }
    res = user.put_update_exsit_user(dummy_user["username"], dummy_user)
    if type(res) != type("abc"):
        updated_user = User(**json.loads(res))
        assert updated_user.username == dummy_user["username"], logging.error("user not updated")
        logging.info("user is updated")
    else:
        logging.error(res)

def test_delete_user_by_username():
    dummy_user = {"id": 10, "username": "theUser",
                  "firstName": "John",
                  "lastName": "James",
                  "email": "john@email.com",
                  "password": "12345",
                  "phone": "12345",
                  "userStatus": 1
                  }
    res = user.delete_user_by_username(dummy_user["username"])
    if type(res) != type("abc"):
        assert res == "", logging.error("user name not founded")
        logging.info("user is deleted")
    else:
        logging.error(res)