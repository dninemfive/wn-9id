from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair

from ..infantry_weapons import M16A2, M249, TOW_SCAT


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # SCOUT/AT TEAM
    with ctx.create_infantry_unit("#RECO2 SCOUT/AT TEAM", "US", "Scout_US", [(M16A2, 5), (M249, 1), (TOW_SCAT, 1)]) as scout_at_team:
        scout_at_team.modules.ui.UpgradeFromUnit='d9_RECO2_IEW_TEAM_US'
        scout_at_team.modules.production.command_point_cost = 100
        return scout_at_team