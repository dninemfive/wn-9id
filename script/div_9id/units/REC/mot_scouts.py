from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
from ..infantry_weapons import M16A2, M249
from warno_mfw.context.mod_creation import ModCreationContext


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_infantry_unit("#RECO2 MOT. SCOUTS", "US", "Scout_US", [(M16A2, 3), (M249, 1)]) as mot_scouts:
        mot_scouts.modules.ui.UpgradeFromUnit='Scout_US'
        ctx.get_unit('Airborne_Scout_US').modules.ui.UpgradeFromUnit = mot_scouts
        return mot_scouts