import json
import requests

class pet_api:
    def __init__(self, url_path="https://petstore3.swagger.io/api/v3"):
        self._url_path_pet = url_path
        self.headrs = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headrs)

    # update an exiting pet.
    def put_update_existing_pet(self, existing_pet: dict) -> dict:
        res = self.session.put(url=f"{self._url_path_pet}/pet", data=existing_pet)
        pet_updated = res.json()
        if res.status_code == 200:
            return pet_updated
        else:
            return res.status_code

    # add new pet to the store.
    def post_new_pet(self, new_pet) -> dict:
        res = self.session.post(url=f"{self._url_path_pet}/pet", data=new_pet)
        if res.status_code == 200:
            return res.json()
        else:
            return res.status_code

    # find pet by status.
    def get_pet_by_status(self, status: str) -> list:
        # Available values : available, pending, sold
        res = self.session.get(url=f"{self._url_path_pet}/pet/findByStatus?status={status}")
        pets = res.json()
        res_pets = []

        if res.status_code == 200:
            for pet in pets:
                res_pets.append(pet)
        else:
            return res.status_code
        return res_pets

    # find by tag.
    def get_pet_by_tags(self, tags):
        dict2 = [{'id': 1, 'name': 'tag3'}, {'id': 2, 'name': 'tag4'}]
        res = self.session.get(url=f"{self._url_path_pet}/pet/findByTags?tags={tags}")
        return res.content

    # get pet by integer id.
    def get_pet_by_id(self, pet_id: int) -> dict:
        """

        :param pet_id:
        :return:
        """
        res = self.session.get(url=f"{self._url_path_pet}/pet/{pet_id}")
        err_msg_404 = "pet not found"
        err_msg_405 = "invalid id supplied"
        pet = res.json()
        if res.status_code == 200:
            return pet
        elif res.status_code == 404:
            return err_msg_404
        elif res.status_code == 405:
            return err_msg_405

    # update pet in the store by id.
    def post_pet_by_id(self, pet_id: int, pet_name: str) -> dict or int:
        res = self.session.post(url=f"{self._url_path_pet}/pet/{pet_id}/?name={pet_name}")
        if res.status_code == 200:
            return res.json()
        else:
            return res.status_code

    # delete pet by id.
    def delete_pet_by_id(self, pet_id):
        res = self.session.delete(url=f"{self._url_path_pet}/pet/{pet_id}")

        if res.status_code == 200:
            return f"Pet number {pet_id} deleted"
        else:
            return res.status_code

    # upload an image.
    def upload_img_by_id(self):
        pass


def main():
    pet_josn = """
    {
  "id": 2,
  "name": "My_doggie",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 10,
      "name": "string"
    }
  ],
  "status": "available"
}
    """
    pet_josn = json.loads(pet_josn)
    pet2 = pet_api()
    pet3 = pet2.get_pet_by_id(5)
    # print(pet2.post_new_pet())
    # print(type(pet2.get_pet_by_id(5)))
    # update_name = pet2.get_pet_by_id(5)
    # print(type(pet2.put_update_existing_pet(pet3)))
    # print(pet3)
    # print(pet2.post_pet_by_id())
    # print(pet2.get_pet_by_status("sold"))
    # print(pet2.delete_pet_by_id(5))
    # print(pet2.get_pet_by_tags("name"))
if __name__ == "__main__":
    main()