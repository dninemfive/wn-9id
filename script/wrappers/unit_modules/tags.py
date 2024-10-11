from typing import Self

import utils.ndf.edit as edit
import utils.ndf.ensure as ensure
from ndf_parse.model import List, Object
from wrappers.str_list import StrListWrapper

from ._abc import UnitModuleWrapper
from ._decorator import unit_module


@unit_module('TTagsModuleDescriptor')
class TagsModuleWrapper(UnitModuleWrapper):
    def __iter__(self: Self):
        yield from self.TagSet

    @property
    def TagSet(self: Self) -> StrListWrapper:
        if self._tag_set is None:
            self._tag_set = StrListWrapper(self.object.by_member('TagSet').value)
        return self._tag_set
    
    @TagSet.setter
    def TagSet(self: Self, value: list[str] | List) -> None:
        if self._tag_set is not None:
            self._tag_set = None
        edit.member(self.object, 'TagSet', ensure.all(value, lambda x: ensure.quoted(x, '"')))

    def add(self: Self, *values: str) -> None:
        for value in values:
            self.TagSet.add(ensure.quoted(value, '"'))

    def remove(self: Self, *values: str) -> None:
        for value in values:
            self.TagSet.remove(value)