from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
import warno_mfw.utils.ndf.ensure as ensure
import warno_mfw.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("A-7E CORSAIR II [NPLM]", "US", "Mirage_5_F_nplm_FR") as a7e_nplm:
        a7e_nplm.modules.ui.UpgradeFromUnit='d9_A7E_CORSAIR_II_HE_US'
        a7e_nplm.unit.set_country('US')
        return a7e_nplm