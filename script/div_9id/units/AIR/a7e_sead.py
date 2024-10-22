from mw2.context.mod_creation import ModCreationContext
from mw2.context.unit_module import UnitModuleContext
from mw2.metadata.unit import UnitMetadata
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair
import mw2.utils.ndf.ensure as ensure
import mw2.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("A-7E CORSAIR II [SEAD]", "US", "Mirage_5_F_clu_FR") as a7e_sead:
        a7e_sead.modules.ui.UpgradeFromUnit='d9_A7E_CORSAIR_II_NPLM_US'
        a7e_sead.unit.set_country('US')
        return a7e_sead