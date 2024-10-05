from typing import Generic, Self, TypeVar
from ndf_parse.model import List, ListRow, Map, MapRow, MemberRow, Object

T = TypeVar('T')
NdfItemReference = List | Map | Object
NdfFieldReference = ListRow | MapRow | MemberRow

class NdfFieldWrapper(Generic[T]):
    def __init__(self: Self, ndf: NdfItemReference, name: str):
        if isinstance(ndf, List):
            self.ref: ListRow = ndf.by_name(name)
        elif isinstance(ndf, Map):
            self.ref: MapRow = ndf.by_key(name)
        elif isinstance(ndf, Object):
            self.ref: MemberRow = ndf.by_member(name)

    def __set__(field: NdfFieldReference, value: T) -> None:
        pass

    def __get__(field: NdfFieldReference) -> T:
        pass

class IntWrapper(NdfFieldWrapper[int]):
    def set(field: NdfFieldReference, value: int) -> None:
        field.value = str(value)

    def get(field: NdfFieldReference) -> int:
        return int(field.value)