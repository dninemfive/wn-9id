from typing import Self

from lib.context.mod_creation_context import ModCreationContext

class UnitDef(object):
    def __init__(self: Self,
                 ctx: ModCreationContext,
                 name: str,
                 country: str,
                 copy_of: str,
                 showroom_src: str | None = None,
                 button_texture_src_path: str | None = None):
        self.ctx = ctx

