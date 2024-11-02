from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
import warno_mfw.utils.ndf.ensure as ensure
import warno_mfw.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("F-14B TOMCAT [AA2]", "US", "F15C_Eagle_AA2_US") as f14b_aa2:
        f14b_aa2.modules.ui.UpgradeFromUnit='d9_F14B_TOMCAT_AA1_US'
        f14b_aa2.unit.set_country('US')
        return f14b_aa2