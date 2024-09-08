from dataclasses import dataclass
from typing import Self

@dataclass
class UnitMetadata(object):
    name: str
    
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
    def showroom_descriptor_path(self: Self) -> str:
        return f'$/GFX/Unit/Descriptor_ShowRoomUnit_{self.name}'
    
    @property
    def deck_pack_descriptor_name(self: Self) -> str:
        return f"Descriptor_Deck_Pack_{self.name}"
    
    @property
    def deck_pack_descriptor_path(self: Self) -> str:
        return f"~/{self.deck_pack_descriptor_name}"
    
    @property
    def tag(self: Self) -> str:
        return f'"UNITE_{self.name}"'
    
    @staticmethod
    def from_localized_name(localized_name: str, country: str) -> Self:
        return UnitMetadata(f"{UnitMetadata.delocalize(localized_name)}_{country}")
    
    @staticmethod
    def delocalize(localized_name: str) -> str:
        result: str = "_".join(localized_name.split())
        for c in [".", "(", ")", "-"]:
            result = result.replace(c, "")
        return result