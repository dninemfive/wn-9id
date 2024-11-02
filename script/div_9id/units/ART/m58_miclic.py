from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
import warno_mfw.utils.ndf.ensure as ensure
import warno_mfw.utils.ndf.edit as edit


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("M58 MICLIC", "US", "Mortier_2B9_Vasilek_SOV") as m58_miclic:
        # set ammo to Ammo_RocketArt_PW_MICLICS
        m58_miclic.modules.ui.UpgradeFromUnit=None
        m58_miclic.unit.set_country('US')
        return m58_miclic