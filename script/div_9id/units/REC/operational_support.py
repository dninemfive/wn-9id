from mw2.context.mod_creation import ModCreationContext
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair

from ..infantry_weapons import M16A2, M249, M82, SATCHEL_CHARGE


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # OPERATIONAL SUPPORT
    # TODO: change weapon loadout, maybe including M82?
    with ctx.create_infantry_unit("#RECO1 OPERATIONAL SUPPORT", "US", "Scout_US", [(M16A2, 8), (M249, 2), (M82, 2), (SATCHEL_CHARGE, 2)]) as osd:
        # TODO: increase menace
        # TODO: reduce vision
        return osd