import json
import requests
import os
class pet_api:
    def __init__(self, url_path="https://petstore3.swagger.io/api/v3"):
        self._url_path_pet = url_path
        self.headrs = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headrs)

    # update an exiting pet.
    def put_update_existing_pet(self, existing_pet: dict) -> dict or int:
        res = self.session.put(url=f"{self._url_path_pet}/pet", data=existing_pet)
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 400:
            return "Invalid id supplied"
        elif res.status_code == 404:
            return "Pet not found"
        elif res.status_code == 405:
            return "Validation exception"
        else:
            "There was an error processing your request"

    # add new pet to the store.
    def post_new_pet(self, new_pet: dict) -> dict or str:
        res = self.session.post(url=f"{self._url_path_pet}/pet", data=new_pet)
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 405:
            return "invalid input"
        else:
            return "There was an error processing your request"

    # find pet by status.
    def get_pet_by_status(self, status: str) -> list or str:
        res = self.session.get(url=f"{self._url_path_pet}/pet/findByStatus?status={status}")
        if res.status_code == 200:
            if len(res.json()) > 0:
                return res.json()
            else:
                return "list is empty ! try other options pending/sold/available"
        elif res.status_code == 400:
            return "Invalid status value"
        elif res.status_code == 500:
            return "There was an error processing your request"

    # find by tag.
    def get_pet_by_tags(self, tag_id: int, tag_name: str) -> dict or str:
        res = self.session.get(url=f"{self._url_path_pet}/pet/findByTags?tags={tag_id}&tags={tag_name}")
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 400:
            return "invalid tag values"
        elif res.status_code == 500:
            return "There was an error processing your request"

    # get pet by integer id.
    def get_pet_by_id(self, pet_id: str) -> dict or str:
        res = self.session.get(url=f"{self._url_path_pet}/pet/{pet_id}")
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 404:
            return "pet not found"
        elif res.status_code == 405:
            return "invalid id supplied"
        else:
            return "There was an error processing your request"

    # update pet in the store by id.
    def post_pet_by_id(self, pet_id: int, pet_name: str, pet_status: str) -> dict or int:
        res = self.session.post(url=f"{self._url_path_pet}/pet/{pet_id}?name={pet_name}&status={pet_status}")
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 405:
            return "Invalid input"
        elif res.status_code == 500:
            return "There was an error processing your request"

    # delete pet by id.
    def delete_pet_by_id(self, pet_id: int) -> str:
        res = self.session.delete(url=f"{self._url_path_pet}/pet/{pet_id}")
        if res.status_code == 200:
            return f"Pet number {pet_id} deleted"
        elif res.status_code == 400:
            return "Invalid pet value"
        elif res.status_code == 500:
            return "There was an error processing your request"

    # upload an image.
    def post_upload_img_by_id(self, pet_id: str, meta_data: str,peth_image: dict,):
        res = self.session.post(url=f"{self._url_path_pet}/{pet_id}/uploadImage?additionalMetadata={meta_data}", data=peth_image)
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 404:
            return "HTTP 404 Not Found"
        elif res.status_code == 500:
            return "There was an error processing your request"


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
    # pet3 = pet2.get_pet_by_id(5)
    # print(pet2.post_new_pet())
    # print(type(pet2.get_pet_by_id(10)))
    # update_name = pet2.get_pet_by_id(5)
    # print(type(pet2.put_update_existing_pet(pet3)))
    # print(pet3)
    # print(pet2.post_pet_by_id())
    print(pet2.get_pet_by_status("available"))
    # print(pet2.delete_pet_by_id(5))
    # print(pet2.get_pet_by_tags(20, "string"))
    print(pet2.upload_img_by_id())
if __name__ == "__main__":
    main()
