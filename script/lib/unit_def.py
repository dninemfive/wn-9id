from abc import ABC, abstractmethod
from typing import Self

from lib.context.mod_creation_context import ModCreationContext
from lib.creators.unit import UnitCreator

class UnitDef(ABC):
    def __init__(self: Self,
                 ctx: ModCreationContext,
                 name: str,
                 country: str,
                 copy_of: str,
                 showroom_src: str | None = None,
                 button_texture_src_path: str | None = None):
        self.ctx = ctx
        self.name = name
        self.country = country
        self.copy_of = copy_of
        self.showroom_src = showroom_src
        self.button_texture_src_path = button_texture_src_path

    def _unit_creator(self: Self) -> UnitCreator:
        return self.ctx.create_unit(self.name, self.country, self.copy_of, self.showroom_src, self.button_texture_src_path)

    @abstractmethod
    def adjust(self: Self, unit_creator: UnitCreator) -> str:
        ...

