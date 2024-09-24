
from lib.context.mod_creation_context import ModCreationContext
from lib.context.module_context import ModuleContext
from lib.creators.unit import UNIT_UI
from lib.metadata.division_unit_registry import UnitRules
from lib.metadata.unit import UnitMetadata
from ndf_parse.model import List, ListRow, Object
import lib.utils.ndf.edit as edit
import lib.utils.ndf.ensure as ensure
from lib.constants.ndf_paths import WEAPON_DESCRIPTOR


def create(ctx: ModCreationContext) -> UnitRules | None:
    # M998 HUMVEE GLH-L
    with ctx.create_unit("M998 HUMVEE GLH-L", "US", "M1025_Humvee_TOW_US") as m998_humvee_glhl:
        with m998_humvee_glhl.edit_weapons('M1025_Humvee_TOW_US') as weapons:
            weapons.edit_members(Salves=[4,])
            weapons.get_turret_weapon(0).by_member('Ammunition').value = 'Ammo_AGM_AGM114A_x2_sol'
        m998_humvee_glhl.edit_ui_module(UpgradeFromUnit='Descriptor_Unit_M1025_Humvee_TOW_para_US')
        return UnitRules(m998_humvee_glhl, 3, [0, 4, 3, 0])