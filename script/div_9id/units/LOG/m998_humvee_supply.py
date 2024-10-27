from mw2.constants.ndf_paths import UNITE_DESCRIPTOR
from mw2.context.mod_creation import ModCreationContext
from mw2.context.unit_module import UnitModuleContext
from mw2.creators.unit.basic import BasicUnitCreator
from mw2.metadata.unit import UnitMetadata
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair
from mw2.wrappers.unit import UnitWrapper
from ndf_parse.model import List, Object

from ._utils import untransportify_m1038_gfx
from mw2.constants import ndf_paths

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
                                                Depiction=untransportify_m1038_gfx(ctx.ndf[ndf_paths.GENERATED_DEPICTION_VEHICLES], m998_humvee_supply.new_unit))
        return (m998_humvee_supply, ROVER)

def edit_with_m1038(m998_humvee_supply: BasicUnitCreator, m1038_humvee: UnitWrapper) -> None:
    m998_humvee_supply.modules.replace_from(m1038_humvee, 'GenericMovement', by_name=True)
    m998_humvee_supply.modules.replace_from(m1038_humvee, 'LandMovement', by_name=True)
    m998_humvee_supply.modules.replace_from(m1038_humvee, 'TBaseDamageModuleDescriptor')