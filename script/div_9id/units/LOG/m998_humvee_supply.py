from ndf_parse.model import List, Object
from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.creators.unit.basic import BasicUnitCreator
from warno_mfw.hints.paths.GameData.Generated.Gameplay import Gfx as ndf_paths
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
from warno_mfw.wrappers.unit import UnitWrapper

from ._utils import m1038ify_m1025_gfx

MODULES_DESCRIPTORS = "ModulesDescriptors"

M1038, ROVER = 'M1038_Humvee_US', 'Rover_101FC_supply_UK'

def create(ctx: ModCreationContext) -> NewSrcUnitPair | None:
    with ctx.create_unit("M998 HUMVEE SUPPLY", "US", ROVER, M1038) as m998_humvee_supply:
        edit_with_m1038(m998_humvee_supply, ctx.get_unit(M1038))
        m998_humvee_supply.modules.type.MotherCountry = 'US'
        m998_humvee_supply.modules.type.Nationalite = 'NATO'
        m998_humvee_supply.modules.ui.edit_members(
            # upgrade from M561 SUPPLY GOAT
            UpgradeFromUnit='Gama_Goat_supply_US',
            ButtonTexture='M1038_Humvee_US',

        )
        m998_humvee_supply.modules.ui.CountryTexture = 'US'
        # make M35 upgrade from this instead
        ctx.get_unit('M35_supply_US').modules.ui.UpgradeFromUnit = m998_humvee_supply
        m998_humvee_supply.modules.edit_members('ApparenceModel',
                                                by_name=True,
                                                Depiction=m1038ify_m1025_gfx(ctx.ndf[ndf_paths.Depictions.GeneratedDepictionVehicles], m998_humvee_supply.new_unit))
        return (m998_humvee_supply, ROVER)

def edit_with_m1038(m998_humvee_supply: BasicUnitCreator, m1038_humvee: UnitWrapper) -> None:
    m998_humvee_supply.modules.replace_from(m1038_humvee, 'GenericMovement', by_name=True)
    m998_humvee_supply.modules.replace_from(m1038_humvee, 'LandMovement', by_name=True)
    m998_humvee_supply.modules.replace_from(m1038_humvee, 'TBaseDamageModuleDescriptor')