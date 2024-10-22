from mw2.context.mod_creation import ModCreationContext
from mw2.context.unit_module import UnitModuleContext
from mw2.metadata.unit import UnitMetadata
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair
import mw2.utils.ndf.ensure as ensure
import mw2.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("F-14B TOMCAT [AA2]", "US", "F15C_Eagle_AA2_US") as f14b_aa2:
        f14b_aa2.modules.ui.UpgradeFromUnit='d9_F14B_TOMCAT_AA1'
        f14b_aa2.unit.set_country('US')
        return f14b_aa2