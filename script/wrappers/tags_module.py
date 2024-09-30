from typing import Self

from ndf_parse.model import List, Object
import utils.ndf.ensure as ensure

class TagsModuleWrapper(object):
    def __init__(self: Self, ctx, obj: Object):
        self.ctx = ctx
        self.object = obj

    def __iter__(self: Self):
        yield from [x.value for x in self.TagSet]

    @property
    def TagSet(self: Self) -> List:
        return self.object.by_member('TagSet').value
    
    @TagSet.setter
    def TagSet(self: Self, value: List) -> None:
        self.object.by_member('TagSet').value = value

    def add(self: Self, value: str) -> None:
        self.TagSet.add(ensure.quoted(value))

    def remove(self: Self, value: str) -> None:
        index = self.TagSet.find_by_cond(lambda x: x.value == value)
        self.TagSet.remove(index)