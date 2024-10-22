from mw2.context.mod_creation import ModCreationContext
from mw2.context.unit_module import UnitModuleContext
from mw2.metadata.unit import UnitMetadata
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair
import mw2.utils.ndf.ensure as ensure
import mw2.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("F-14B TOMCAT [LGB]", "US", "F15E_StrikeEagle_US") as f14b_lgb:
        f14b_lgb.modules.ui.UpgradeFromUnit='d9_F14B_TOMCAT_AA2_US'
        f14b_lgb.unit.set_country('US')
        return f14b_lgb