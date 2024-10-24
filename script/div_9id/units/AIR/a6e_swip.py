from mw2.context.mod_creation import ModCreationContext
from mw2.context.unit_module import UnitModuleContext
from mw2.metadata.unit import UnitMetadata
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair
import mw2.utils.ndf.ensure as ensure
import mw2.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("A-6E INTRUDER SWIP", "US", "F4F_Phantom_II_AT_RFA") as a6e_swip:
        a6e_swip.modules.ui.UpgradeFromUnit='d9_A6E_INTRUDER_LGB_US'
        a6e_swip.unit.set_country('US')
        return a6e_swip