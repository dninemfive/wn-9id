from mw2.context.mod_creation import ModCreationContext
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair

from ..infantry_weapons import M16A2, M240, SMOKE_GRENADE


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # CMD MOT. RIFLES LDR.
    with ctx.create_infantry_unit("#CMD MOT. RIFLES LDR.", "US", "Rifles_CMD_US", [(M16A2, 5), (M240, 1), (SMOKE_GRENADE, 1)],
                                  'img/units/mot_rifles/ldr/icon.png') as mot_rifles_ldr:
        mot_rifles_ldr.command_point_cost -= 10
        return mot_rifles_ldr
        