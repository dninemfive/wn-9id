from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
import warno_mfw.utils.ndf.ensure as ensure
import warno_mfw.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("A-7E CORSAIR II [SEAD]", "US", "Mirage_5_F_clu_FR") as a7e_sead:
        a7e_sead.modules.ui.UpgradeFromUnit='d9_A7E_CORSAIR_II_NPLM_US'
        a7e_sead.unit.set_country('US')
        a7e_sead.modules.ui.main_specialty = 'sead'
        return a7e_sead