from mw2.context.mod_creation import ModCreationContext
from mw2.context.unit_module import UnitModuleContext
from mw2.metadata.unit import UnitMetadata
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair
import mw2.utils.ndf.ensure as ensure
import mw2.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("EA-6B PROWLER [EW]", "US", "F4_Wild_Weasel_US") as ea6b_ew:
        ea6b_ew.modules.ui.UpgradeFromUnit='d9_EA6B_PROWLER_EW_US'
        ea6b_ew.unit.set_country('US')
        return ea6b_ew