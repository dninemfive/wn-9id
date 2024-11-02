from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
import warno_mfw.utils.ndf.ensure as ensure
import warno_mfw.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("A-7E CORSAIR II [HE]", "US", "Mirage_5_F_FR") as a7e_he:
        a7e_he.modules.ui.UpgradeFromUnit=None
        a7e_he.unit.set_country('US')
        return a7e_he