from dataclasses import dataclass
from typing import Self

from utils.localization import delocalize


@dataclass
class UnitMetadata(object):
    name: str
    country: str

    @property
    def quoted_name(self: Self) -> str:
        return f"'{self.name}'"
    
    @property
    def class_name_for_debug(self: Self) -> str:
        return f"'Unit_{self.name}'"

    @property
    def descriptor_name(self: Self) -> str:
        return f'Descriptor_Unit_{self.name}'
    
    @property
    def descriptor_path(self: Self) -> str:
        return f'$/GFX/Unit/{self.descriptor_name}'
    
    @property
    def showroom_descriptor_name(self: Self) -> str:
        return f'Descriptor_ShowRoomUnit_{self.name}'

    @property
    def showroom_descriptor_path(self: Self) -> str:
        return f'$/GFX/Unit/{self.showroom_descriptor_name}'
    
    @property
    def deck_pack_descriptor_name(self: Self) -> str:
        return f"Descriptor_Deck_Pack_{self.name}"
    
    @property
    def deck_pack_descriptor_path(self: Self) -> str:
        return f"~/{self.deck_pack_descriptor_name}"
    
    @property
    def tag(self: Self) -> str:
        return f'"UNITE_{self.name}"'
    
    @property
    def button_texture_name(self: Self) -> str:
        return f'Texture_Button_Unit_{self.name}'
    
    @property
    def weapon_descriptor_name(self: Self) -> str:
        return f'WeaponDescriptor_{self.name}'
    
    @property
    def weapon_descriptor_path(self: Self) -> str:
        return f'$/GFX/Weapon/{self.weapon_descriptor_name}'
    
    @staticmethod
    def from_localized_name(prefix: str, localized_name: str, country: str) -> Self:
        return UnitMetadata(f"{prefix}_{delocalize(localized_name)}", country)
    
    @staticmethod
    def resolve(unit_reference: str | Self | None, backup_reference: str | Self | None = None) -> Self:
        if isinstance(unit_reference, UnitMetadata):
            return unit_reference
        if isinstance(unit_reference, str):
            split = unit_reference.split('_')
            return UnitMetadata('_'.join(split[:-1]), split[-1])
        if unit_reference is None:
            if backup_reference is None:
                raise ValueError(f'Backup reference cannot be None if unit_reference is None!')
            return UnitMetadata.resolve(backup_reference)
        