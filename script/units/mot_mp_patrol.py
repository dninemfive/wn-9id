from context.module_context import ModuleContext
from script.context.unit_id_manager import UnitIdManager
from metadata.division_unit_registry import UnitRules
from script.creators.unit import UNIT_UI
from ndf_parse.model import List

def create(ctx: UnitIdManager) -> UnitRules | None:
    # MOT. MP PATROL
    # (just copy AB MP PATROL)
    with ctx.create_unit("MOT. MP PATROL", "US", "Airborne_MP_US") as mp_patrol:
        with mp_patrol.module_context(UNIT_UI) as ui_module:
            specialties: List = ui_module.object.by_member("SpecialtiesList").value
            specialties.remove(specialties.find_by_cond(lambda x: x.value == "'_para'"))
            ui_module.edit_members(SpecialtiesList=specialties)
        mp_patrol.remove_module("TDeploymentShiftModuleDescriptor")
        # update transportable (TODO: automate this)
        with mp_patrol.module_context('TTransportableModuleDescriptor') as transportable_module:
            transportable_module.edit_members(TransportedSoldier='"d9_MOT_MP_PATROL_US"')
        return UnitRules(mp_patrol, 2, [0, 6, 4, 0], ["$/GFX/Unit/Descriptor_Unit_M1025_Humvee_MP_US"])
        