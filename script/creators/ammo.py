# right, python is stupid so i can't use type hints for this
# from context.unit_creation_context import UnitCreationContext
from typing import Self

import utils.ndf.edit as edit
import utils.ndf.ensure as ensure
from constants.ndf_paths import AMMUNITION
from context.module_context import ModuleContext
from metadata.unit import UnitMetadata
from ndf_parse import Mod
from ndf_parse.model import List, ListRow, Map, MapRow, MemberRow, Object
from ndf_parse.model.abc import CellValue
from utils.ndf.decorators import ndf_path
from utils.ndf.unit_module import get, remove
from utils.types.message import Message


class AmmoCreator(object):
    def __init__(self: Self, ndf: dict[str, List], name: str, copy_of: str, ammo_guid: str, hit_roll_guid: str):
        self.ndf = ndf
        self.name = ensure.prefix(name, 'Ammo_')
        self.copy_of = ensure.prefix(copy_of, 'Ammo_')
        self.ammo_guid = ammo_guid
        self.hit_roll_guid = hit_roll_guid

    def __enter__(self: Self) -> Self:
        self.root_msg = self.ctx.root_msg.nest(f"Making {self.name}")
        self.root_msg.__enter__()
        with self.root_msg.nest(f"Copying {self.copy_of}") as _:
            self.object = self.make_copy(self.ctx.ndf[AMMUNITION])
        return self
    
    def __exit__(self: Self, exc_type, exc_value, traceback):
        self.apply(self.ctx.ndf, self.root_msg)
        self.root_msg.__exit__(exc_type, exc_value, traceback)

    def apply(self: Self, ndf: dict[str, List], msg: Message):
        with msg.nest(f"Saving {self.new.name}") as msg2:
            self.edit_ammunition(ndf, msg2)

    def make_copy(self: Self, ndf: List) -> Object:
        copy: Object = ndf.by_name(self.copy_of).value.copy()
        edit.members(copy,
                     DescriptorId=self.ammo_guid)
        # TODO: generic "copy descriptor" method which automatically checks for and sets any member named DescriptorId?
        copy.by_member('HitRollRuleDescriptor').value.by_member('DescriptorId').value = self.hit_roll_guid
        return copy

    # TODO: copy of this but for the missile file?
    @ndf_path(AMMUNITION)
    def edit_ammunition(self: Self, ndf: List):
        ndf.add(ListRow(self.object, namespace=self.name))

    def edit_members(self: Self, **kwargs: CellValue):
        edit.members(self.object, **kwargs)