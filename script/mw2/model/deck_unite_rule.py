from __future__ import annotations

from dataclasses import dataclass
from typing import Self

from mw2.creators.unit.basic import BasicUnitCreator
from mw2.metadata.unit import UnitMetadata
from mw2.unit_registration._types import UnitsPerXp
from mw2.utils.ndf import ensure
from ndf_parse.model import List, MemberRow, Object

UNITE_RULE = 'TDeckUniteRule'
KEY_AVAILABLE_TRANSPORT_LIST = 'AvailableTransportList'
KEY_UNIT_DESCRIPTOR = 'UnitDescriptor'
KEY_AVAILABLE_WITHOUT_TRANSPORT = 'AvailableWithoutTransport'
KEY_NUMBER_OF_UNIT_IN_PACK = 'NumberOfUnitInPack'
KEY_NUMBER_OF_UNIT_IN_PACK_XP_MULTIPLIER = 'NumberOfUnitInPackXPMultiplier'

@dataclass
class TDeckUniteRule(object):
    UnitDescriptor: str
    AvailableWithoutTransport: bool
    AvailableTransportList: list[str] | None
    NumberOfUnitInPack: int
    NumberOfUnitInPackXPMultiplier: tuple[float, float, float, float]

    @staticmethod
    def from_ndf(ndf: Object) -> Self:
        return TDeckUniteRule(
            ndf.by_member(KEY_UNIT_DESCRIPTOR).value,
            ndf.by_member(KEY_AVAILABLE_WITHOUT_TRANSPORT).value,
            [x.value for x in ndf.by_member(KEY_AVAILABLE_TRANSPORT_LIST).value],
            ndf.by_member(KEY_NUMBER_OF_UNIT_IN_PACK).value,
            [float(x) for x in ndf.by_member(KEY_NUMBER_OF_UNIT_IN_PACK_XP_MULTIPLIER).value]
        )

    def to_ndf(self: Self) -> Object:
        return ensure._object(UNITE_RULE,
        {
            KEY_UNIT_DESCRIPTOR:                        self.UnitDescriptor,
            KEY_AVAILABLE_WITHOUT_TRANSPORT:            self.AvailableWithoutTransport,
            KEY_AVAILABLE_TRANSPORT_LIST:               self.AvailableTransportList,
            KEY_NUMBER_OF_UNIT_IN_PACK:                 self.NumberOfUnitInPack,
            KEY_NUMBER_OF_UNIT_IN_PACK_XP_MULTIPLIER:   self.NumberOfUnitInPackXPMultiplier
        })
    
    @staticmethod
    def make(metadata: UnitMetadata | BasicUnitCreator,
             num_per_xp: tuple[int, int, int, int],
             transports: list[str] | None = None,
             force_awt: bool | None = None) -> Self:
        if isinstance(metadata, BasicUnitCreator):
            metadata = metadata.new
        num_per_pack = max(num_per_xp)
        xp_multipliers = [x / num_per_pack for x in num_per_xp]
        available_without_transport = force_awt if force_awt is not None else (transports is None)
        return TDeckUniteRule(
            metadata.descriptor.path,
            available_without_transport,
            transports,
            num_per_pack,
            xp_multipliers
        )
    
    @property
    def units_per_xp(self: Self) -> UnitsPerXp:
        return (int(x * self.NumberOfUnitInPack) for x in self.NumberOfUnitInPackXPMultiplier)