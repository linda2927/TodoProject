from app.crud.base import CRUDBase
from app.models.address import Address
from app.schemas.address_schema import AddressCreate, AddressUpdate


class CRUDAddress(CRUDBase[Address, AddressCreate, AddressUpdate]):
    pass


address = CRUDAddress(Address)
