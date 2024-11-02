from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
import warno_mfw.utils.ndf.ensure as ensure
import warno_mfw.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("EA-6B PROWLER [SEAD]", "US", "F4_Wild_Weasel_US") as ea6b_sead:
        ea6b_sead.modules.ui.UpgradeFromUnit=None
        ea6b_sead.unit.set_country('US')
        ea6b_sead.modules.ui.main_specialty = 'sead'
        return ea6b_sead