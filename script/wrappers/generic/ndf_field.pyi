from typing import Generic, TypeVar
from ndf_parse.model import ListRow, MapRow, MemberRow

T = TypeVar('T')
NdfFieldReference = ListRow | MapRow | MemberRow

class NdfFieldWrapper(Generic[T]):
    def set(field: NdfFieldReference, value: T) -> None:
        pass

    def get(field: NdfFieldReference) -> T:
        pass

class IntWrapper(NdfFieldWrapper[int]):
    def set(field: NdfFieldReference, value: int) -> None:
        field.value = str(value)

    def get(field: NdfFieldReference) -> int:
        return int(field.value)