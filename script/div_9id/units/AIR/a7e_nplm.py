from mw2.context.mod_creation import ModCreationContext
from mw2.context.unit_module import UnitModuleContext
from mw2.metadata.unit import UnitMetadata
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair
import mw2.utils.ndf.ensure as ensure
import mw2.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("A-7E CORSAIR II [NPLM]", "US", "Mirage_5_F_nplm_FR") as a7e_nplm:
        a7e_nplm.modules.ui.UpgradeFromUnit='d9_A7E_CORSAIR_II_HE'
        a7e_nplm.unit.set_country('US')
        return a7e_nplm