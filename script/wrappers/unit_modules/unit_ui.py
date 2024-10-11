from typing import Self
from script.creators.unit.abc import UnitCreator
from script.metadata.unit import UnitMetadata
from script.wrappers.unit import UnitWrapper
from utils.ndf import ensure
from wrappers.str_list import StrListWrapper
from wrappers.unit_modules._abc import UnitModuleWrapper, unit_module
from ndf_parse.model import List, Object
from constants.primitive_types import UnitRole
import utils.ndf.edit as edit

@unit_module('TUnitUIModuleDescriptor')
class UnitUiModuleWrapper(UnitModuleWrapper):
    def __init__(self: Self, ctx, obj: Object):
        self.ctx = ctx
        self.object = obj

    @property
    def ButtonTexture(self: Self) -> str:
        return self.object.by_member('ButtonTexture').value

    @ButtonTexture.setter
    def ButtonTexture(self: Self, value: str) -> None:
        edit.member(self.object, 'ButtonTexture', ensure.quoted(ensure.prefix('Texture_Button_Unit_')))

    @property
    def CountryTexture(self: Self) -> str:
        return self.object.by_member('CountryTexture').value

    @CountryTexture.setter
    def CountryTexture(self: Self, value: str) -> None:
        edit.member(self.object, 'CountryTexture', ensure.quoted(ensure.prefix(value, 'CommonTexture_MotherCountryFlag_')))

    @property
    def DisplayRoadSpeedInKmph(self: Self) -> float:
        return self.object.by_member('DisplayRoadSpeedInKmph').value

    @DisplayRoadSpeedInKmph.setter
    def DisplayRoadSpeedInKmph(self: Self, value: float) -> None:
        edit.member(self.object, 'DisplayRoadSpeedInKmph', value)

    @property
    def GenerateName(self: Self) -> bool:
        return self.object.by_member('GenerateName').value

    @GenerateName.setter
    def GenerateName(self: Self, value: bool) -> None:
        edit.member(self.object, 'GenerateName', value)

    @property
    def InfoPanelConfigurationToken(self: Self) -> str:
        return self.object.by_member('InfoPanelConfigurationToken').value

    @InfoPanelConfigurationToken.setter
    def InfoPanelConfigurationToken(self: Self, value: str) -> None:
        edit.member(self.object, 'InfoPanelConfigurationToken', ensure.quoted(value))

    @property
    def MenuIconTexture(self: Self) -> str:
        return self.object.by_member('MenuIconTexture').value

    @MenuIconTexture.setter
    def MenuIconTexture(self: Self, value: str) -> None:
        edit.member(self.object, 'MenuIconTexture', ensure.quoted(ensure.prefix(value, 'Texture_RTS_H_')))

    @property
    def NameToken(self: Self) -> str:
        return self.object.by_member('NameToken').value

    @NameToken.setter
    def NameToken(self: Self, value: str) -> None:
        edit.member(self.object, 'NameToken', value)

    @property
    def SpecialtiesList(self: Self) -> StrListWrapper:
        if self._specialties_list is None:
            self._specialties_list = StrListWrapper(self.object.by_member('SpecialtiesList').value,
                                                    (ensure.quoted, ensure.unquoted))
        return self._specialties_list

    @SpecialtiesList.setter
    def SpecialtiesList(self: Self, value: list[str] | List) -> None:
        if self._specialties_list is not None:
            self._specialties_list = None
        edit.member(self.object, 'SpecialtiesList', ensure.all(value, ensure.quoted))

    @property
    def TypeStrategicCount(self: Self) -> str:
        return self.object.by_member('TypeStrategicCount').value

    @TypeStrategicCount.setter
    def TypeStrategicCount(self: Self, value: str) -> None:
        edit.member(self.object, 'TypeStrategicCount', ensure.prefix(value, 'ETypeStrategicDetailedCount/'))

    @property
    def UnitRole(self: Self) -> str:
        return self.object.by_member('UnitRole').value

    @UnitRole.setter
    def UnitRole(self: Self, value: str) -> None:
        edit.member(self.object, 'UnitRole', value)

    @property
    def UpgradeFromUnit(self: Self) -> str | None:
        try:
            return self.object.by_member('UpgradeFromUnit').value
        except:
            return None

    @UpgradeFromUnit.setter
    def UpgradeFromUnit(self: Self, value: str | UnitMetadata | UnitCreator | None) -> None:
        if isinstance(value, UnitCreator):
            value = value.new_unit.descriptor_name
        elif isinstance(value, UnitMetadata):
            value = value.descriptor_name
        edit.member(self.object, 'UpgradeFromUnit', ensure.prefix(value, 'Descriptor_Unit_'))

    @property
    def localized_name(self: Self) -> str:
        """ This is expensive and won't always work. Mostly included so i can make a setter for it. """
        return self.ctx.localization.reverse_lookup(self.NameToken)
    
    @localized_name.setter
    def localized_name(self: Self, value: str) -> None:
        return self.ctx.localization.register(value)