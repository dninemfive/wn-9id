from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.creators.unit.basic import UNIT_UI
from warno_mfw.metadata.unit import UnitMetadata
from ndf_parse.model import List, ListRow
import warno_mfw.utils.ndf.edit as edit
import warno_mfw.utils.ndf.ensure as ensure
import warno_mfw.utils.ndf.unit_module as module
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # XM119 IMCS
    # copy VLRA mortar
    with ctx.create_unit("XM119 IMCS 105mm", "US", "VLRA_Mortier81_FR") as xm119_imcs:
        # add tag Artillerie_Longue_Portee
        xm119_imcs.tags.remove('Artillerie_Courte_Portee')
        xm119_imcs.tags.add('Artillerie_Longue_Portee')
        edit.members(xm119_imcs.modules.get('TTacticalLabelModuleDescriptor').by_member('IdentifiedTexture').value,
                        Values=['"Texture_RTS_H_howitzer"', '"Texture_howitzer"'])
        xm119_imcs.modules.ui.edit_members(SpecialtiesList=['howitzer'],
                                           TypeStrategicCount='Howitzer',
                                           UnitRole='tank_C',
                                           UpgradeFromUnit='Howz_M102_105mm_US')
        # change main weapon to a somewhat improved version of the M102 (a bit better fire rate + RAP projectiles, probably)
        ctx.get_unit('Howz_M198_155mm_US').modules.ui.UpgradeFromUnit = None
        # change country (+flag) to US
        xm119_imcs.modules.type.MotherCountry = 'US'
        xm119_imcs.modules.remove('TDeploymentShiftModuleDescriptor')
        xm119_imcs.modules.weapon_manager.Default = 'Howz_L118_105mm_UK'
        return xm119_imcs
        