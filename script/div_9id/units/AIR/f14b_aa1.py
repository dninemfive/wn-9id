from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
import warno_mfw.utils.ndf.ensure as ensure
import warno_mfw.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("F-14B TOMCAT [AA1]", "US", "F15C_Eagle_AA_US") as f14b_aa1:
        f14b_aa1.modules.ui.UpgradeFromUnit=None
        f14b_aa1.unit.set_country('US')
        return f14b_aa1