from mw2.context.mod_creation import ModCreationContext
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair

from ..infantry_weapons import M16A2, M240


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # CMD MOT. RIFLES LDR.
    with ctx.create_infantry_unit("#CMD MOT. RIFLES LDR.", "US", "Rifles_CMD_US", [(M16A2, 5), (M240, 1)]) as mot_rifles_ldr:
        return mot_rifles_ldr
        