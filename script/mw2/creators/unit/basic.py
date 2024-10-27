from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Self

import mw2.constants.ndf_paths as ndf_paths
from mw2.creators.unit.abc import UnitCreator
from mw2.metadata.unit import UnitMetadata
from mw2.utils.ndf.decorators import ndf_path
from mw2.utils.types.message import Message
from mw2.wrappers.unit import UnitWrapper
from ndf_parse.model import List, ListRow, Map, MemberRow, Object

if TYPE_CHECKING:
    from context.mod_creation import ModCreationContext

MODULES_DESCRIPTORS = "ModulesDescriptors"
UNIT_UI = "TUnitUIModuleDescriptor"
TAGS = "TTagsModuleDescriptor"

class BasicUnitCreator(UnitCreator):
    def __init__(self: Self,
                 ctx: ModCreationContext,
                 localized_name: str,
                 new_unit: str | UnitMetadata,
                 src_unit: str | UnitMetadata,
                 gfx_unit: str | UnitMetadata | None = None,
                 button_texture: str | None = None,
                 msg: Message | None = None):
        super().__init__(ctx, localized_name, new_unit, src_unit, button_texture, msg)
        self.gfx_unit = UnitMetadata.resolve(gfx_unit) if gfx_unit is not None else self.src_unit

    def post_enter(self: Self, msg: Message) -> None:
        self.unit.modules.replace_from_many(
            self.gfx_unit.descriptor.name,
            ('ApparenceModel', True),
            'TCadavreGeneratorModuleDescriptor')

    def post_apply(self: Self, msg: Message) -> None:
        self.edit_showroom_units(self.ndf, msg)
        self.edit_showroom_equivalence(self.ndf, msg)

    @ndf_path(ndf_paths.SHOWROOM_UNITS)
    def edit_showroom_units(self: Self, ndf: List):
        showroom_unit: Object
        if hasattr(self, '_showroom_unit'):
            showroom_unit = self._showroom_unit
        else:
            copy: UnitWrapper = self.ctx.get_unit(self.gfx_unit.name, showroom=True).copy()
            copy.DescriptorId = self.ctx.guids.generate(self.new_unit.descriptor.showroom.name)
            copy.modules.type.copy(self.unit.modules.type.object)
            showroom_unit = copy.object
        # try:
        #     copy.modules.remove_where(lambda x: isinstance(x.value, str) and x.value.startswith('$/GFX/Weapon/WeaponDescriptor_'))
        #     copy.modules.append(self.new_unit.weapon_descriptor_path)
        # except:
        #     pass
        ndf.add(ListRow(showroom_unit, visibility='export', namespace=self.new_unit.descriptor.showroom.name))

    @ndf_path(ndf_paths.SHOWROOM_EQUIVALENCE)
    def edit_showroom_equivalence(self: Self, ndf: List):
        unit_to_showroom_equivalent: Map = ndf.by_name("ShowRoomEquivalenceManager").value.by_member("UnitToShowRoomEquivalent").value
        unit_to_showroom_equivalent.add(k=self.new_unit.descriptor.path, v=self.new_unit.descriptor.showroom.path)