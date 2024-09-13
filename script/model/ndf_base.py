from ndf_parse.model import Object
from typing import Self

class NdfBase(object):
    def __init__(self: Self, **kwargs):
        pass

    def to_ndf(self: Self) -> Object:
        pass

    @staticmethod
    def from_ndf(object: Object) -> Self:
        result = Self()
        for row in object:
            setattr(result, row.member, row.value)