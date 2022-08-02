import logging, json, pytest, requests
from api_bookStore.account import book_store_api
from models.user_account import UserAccount
from requests.auth import HTTPBasicAuth

user_accout = book_store_api()
def register_username_password() -> dict:
    """
    dict contain username and password.
    param: sela_user: dict
    return: userName: str, password: str.
    """
    demo_user = {"userName": "selaUser", "password": "Aa123456@"}
    uuid = '860189b4-4a95-4e96-8079-4a4f69ea3a0b'
    return demo_user

@pytest.mark.contain_user_details
def test_post_Authorized():
    # request authorized user.
    demo_user = {"userName": "selaUser", "password": "Aa123456@"}
    uuid = '860189b4-4a95-4e96-8079-4a4f69ea3a0b'
    authorized = user_accout.post_Authorized(demo_user)
    if type(authorized) == type(True):
            assert authorized, logging.error("user not authorized")
            logging.info("{} is Authorized".format(demo_user["userName"]))
    else:
        logging.error(authorized)


@pytest.mark.secure_token
def test_post_GenerateToken():
    demo_user = {"userName": "selaUser", "password": "Aa123456@"}
    res = user_accout.post_GenerateToken(demo_user)
    # validate response.
    if type(res) != type("abc"):
        if res["status"] == "Success":
            user_generated = UserAccount(**demo_user)
            assert res["status"] == "Success" and user_generated.userName == demo_user["userName"], logging.error("users details not authorized")
            logging.info("{}, {}".format(demo_user["userName"], res["result"]))
        elif res["status"] == "Failed":
            logging.error("users details not authorized")
    else:
        logging.error(res)


@pytest.mark.username_userID
def test_post_User():
    demo_user = {"userName": "BimBambooobbbvvvvvbooodddd", "password": "bbbb@@@@BD###DDbbbbb3bbb3@@ss"}
    res = user_accout.post_User(demo_user)
    # reload response is 200.
    if len(res) == 3 and len(res) != 2:
        assert res["username"] == demo_user["userName"], logging.error("user not created")
        logging.info("user registered successfully! userID: {}".format(res["userID"]))
        uuid = res["userID"]
        user_accout.delete_uuid(demo_user, uuid)
    else:
        logging.error(res["message"])


@pytest.mark.warning
def test_delete_uuid():
    demo_user = {"userName": "BimBamboooboo", "password": "bbbbBDDDbbbbb3bbb3@@ss"}
    uuid = "78ceac91-2467-4228-b383-ee558ef65510"
    res = user_accout.delete_uuid(demo_user, uuid)
    if res == 200:
        valide_the_user = user_accout.get_uuid(demo_user, uuid)
        if type(valide_the_user) == type({}):
            assert valide_the_user["message"] == "User not found!", logging.error("user exsit")
            logging.info("user not found")
        else:
            logging.error(valide_the_user)
    else:
        logging.error(res)


def test_get_uuid():
    demo_user = {"userName": "selaUser", "password": "Aa123456@"}
    uuid = '860189b4-4a95-4e96-8079-4a4f69ea3a0b'
    res = user_accout.get_uuid(demo_user, uuid)
    if len(res) != 2:
        assert res["userId"] == uuid and res["username"] == demo_user["userName"], logging.error("user not found")
        logging.info("user found")
    else:
        logging.error(res)