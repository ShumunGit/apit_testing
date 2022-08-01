
class Order:
    def __init__(self, id: int, petId: int, quantity: int, shipDate: str, status: str, complete: bool):
        self._id = id
        self._pet_id = petId
        self._quantity = quantity
        self._shipDate = shipDate
        self._status = status
        self._complete = complete


    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, Id: int):
        self._id = Id

    @property
    def pet_id(self) -> int:
        return self._pet_id

    @pet_id.setter
    def pet_id(self, Id):
        self._pet_id = Id

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity

    @property
    def shipDate(self) -> str:
        return self._shipDate

    @shipDate.setter
    def shipDate(self, shipDate: str):
        self._shipDate = shipDate

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status

    @property
    def complete(self) -> bool:
        return self._complete

    @complete.setter
    def complete(self, complete: bool):
        self._complete = complete


