from typing import Self

import utils.ndf.ensure as ensure
from constants.primitive_types import MotherCountry
from ndf_parse.model import List, Object

from ._abc import UnitModuleKey, UnitModuleWrapper


class TypeUnitModuleWrapper(UnitModuleWrapper):
    _module_key = UnitModuleKey('TTypeUnitModuleDescriptor')
    def __init__(self: Self, ctx, obj: Object):
        self.ctx = ctx
        self.object = obj
        
    @property
    def Nationalite(self: Self) -> str:
        return self.object.by_member('Nationalite').value
    
    @Nationalite.setter
    def Nationalite(self: Self, value: str) -> None:
        if value == 'NATO':
            value = 'Allies'
        if value == 'PACT':
            value = 'Axis'
        self.object.by_member('Nationalite').value = ensure.prefix(value, 'ENationalite/')

    @property
    def MotherCountry(self: Self) -> str:
        return self.object.by_member('MotherCountry').value
    
    @MotherCountry.setter
    def MotherCountry(self: Self, val: str) -> None:
        self.object.by_member('MotherCountry').value = ensure.quoted(val)

    @property
    def AcknowUnitType(self: Self) -> str:
        return self.object.by_member('AcknowUnitType').value
    
    @AcknowUnitType.setter
    def AcknowUnitType(self: Self, val: str) -> None:
        self.object.by_member('AcknowUnitType').value = ensure.prefix(val, '~/TAcknowUnitType_')

    @property
    def TypeUnitFormation(self: Self) -> str:
        return self.object.by_member('TypeUnitFormation').value
    
    @TypeUnitFormation.setter
    def TypeUnitFormation(self: Self, val: str) -> None:
        self.object.by_member('TypeUnitFormation').value = ensure.quoted(val)