from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
import warno_mfw.utils.ndf.ensure as ensure
import warno_mfw.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("A-6E INTRUDER SWIP", "US", "F4F_Phantom_II_AT_RFA") as a6e_swip:
        a6e_swip.modules.ui.UpgradeFromUnit='d9_A6E_INTRUDER_LGB_US'
        a6e_swip.unit.set_country('US')
        return a6e_swip