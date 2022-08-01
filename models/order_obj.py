
class order:
    def __int__(self, Id, pet_id, quantity, shipDate, status, complete):
        self._id = Id
        self._pet_id = pet_id
        self._quantity = quantity
        self._ship_date = shipDate
        self._status = status
        self._complete = complete

    @property
    def Id(self) -> int:
        return self._id

    @Id.setter
    def Id(self, new_id: int):
        self._id = new_id

    @property
    def pet_id(self) -> int:
        return self._pet_id

    @pet_id.setter
    def pet_id(self, new_pet_id: int):
        self._pet_id = new_pet_id

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int):
        self._quantity = new_quantity

    @property
    def shipDate(self) -> str:
        return self._ship_date

    @shipDate.setter
    def shipDate(self, new_shipDate: str):
        self._ship_date = new_shipDate

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_status) -> str:
        self._status = new_status

    @property
    def complete(self) -> bool:
        return self._complete

    @complete.setter
    def complete(self, new_complete: bool):
        self._complete = new_complete
