from typing import Self

import utils.ndf.edit as edit
import utils.ndf.ensure as ensure
from ndf_parse.model import List, Object
from wrappers.str_list import StrListWrapper

from ._abc import UnitModuleKey, UnitModuleWrapper

class TagsModuleWrapper(UnitModuleWrapper):
    _module_key = UnitModuleKey('TTagsModuleDescriptor')

    def __iter__(self: Self):
        yield from self.TagSet

    @property
    def TagSet(self: Self) -> StrListWrapper:
        if not hasattr(self, '_tag_set'):
            self._tag_set = StrListWrapper(self.object.by_member('TagSet').value)
        return self._tag_set
    
    @TagSet.setter
    def TagSet(self: Self, value: list[str] | List) -> None:
        if hasattr(self, '_tag_set'):
            delattr(self, '_tag_set')
        edit.member(self.object, 'TagSet', ensure.all(value, lambda x: ensure.quoted(x, '"')))

    def add(self: Self, *values: str) -> None:
        for value in values:
            self.TagSet.add(ensure.quoted(value, '"'))

    def remove(self: Self, *values: str) -> None:
        for value in values:
            self.TagSet.remove(value)

    def replace(self: Self, to_replace: str, to_replace_with: str) -> None:
        self.remove(to_replace)
        self.add(to_replace_with)