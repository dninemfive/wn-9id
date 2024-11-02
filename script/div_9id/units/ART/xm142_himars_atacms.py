import warno_mfw.utils.ndf.edit as edit
from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.creators.ammo import AmmoCreator
from warno_mfw.creators.unit.basic import UNIT_UI
from warno_mfw.creators.weapon import WeaponCreator
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
from ndf_parse.model import List, ListRow


def create(ctx: ModCreationContext) -> NewSrcUnitPair | None:
    with ctx.create_unit("XM142 HIMARS [ATACMS]", "US", "BM21_Grad_SOV") as xm142_himars_atacms:
        # weapon
        # update speed, fuel capacity
        xm142_himars_atacms.unit.set_country('US')
        # change unit dangerousness
        # change unit attack/defense value
        # change unit cost
        xm142_himars_atacms.modules.ui.UpgradeFromUnit = 'd9_XM142_HIMARS_CLU_US'
        return xm142_himars_atacms
        