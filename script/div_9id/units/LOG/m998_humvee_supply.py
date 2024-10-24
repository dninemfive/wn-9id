from mw2.constants.ndf_paths import UNITE_DESCRIPTOR
from mw2.context.mod_creation import ModCreationContext
from mw2.context.unit_module import UnitModuleContext
from mw2.creators.unit.basic import BasicUnitCreator
from mw2.metadata.unit import UnitMetadata
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair
from mw2.wrappers.unit import UnitWrapper
from ndf_parse.model import List, Object

MODULES_DESCRIPTORS = "ModulesDescriptors"

M1038, ROVER = 'M1038_Humvee_US', 'Rover_101FC_supply_UK'

# todo: put most of this structure in an @annotation
def create(ctx: ModCreationContext) -> NewSrcUnitPair | None:
    # M998 HUMVEE SUPPLY
    #   copy of: M35 Supply
    with ctx.create_unit("M998 HUMVEE SUPPLY", "US", ROVER, M1038) as m998_humvee_supply:
        # need to have a way to just do (unit).MakeSupply, (unit).MakeNotTransport, &c
        edit_with_m1038(m998_humvee_supply, ctx.get_unit(M1038))
        # edit_with_rover101fc(m998_humvee_supply, ctx.get_unit(ROVER))
        m998_humvee_supply.modules.type.MotherCountry = 'US'
        m998_humvee_supply.modules.type.Nationalite = 'NATO'
        m998_humvee_supply.modules.ui.edit_members(
            # upgrade from M561 SUPPLY GOAT
            UpgradeFromUnit='Gama_Goat_supply_US',
            # TODO: automate this as part of copying the appearance of another unit?
            ButtonTexture='M1038_Humvee_US',

        )
        m998_humvee_supply.modules.ui.CountryTexture = 'US'
        # make M35 upgrade from this instead
        ctx.get_unit('M35_supply_US').modules.ui.UpgradeFromUnit = m998_humvee_supply
        return (m998_humvee_supply, ROVER)

def edit_with_m1038(m998_humvee_supply: BasicUnitCreator, m1038_humvee: UnitWrapper) -> None:
    m998_humvee_supply.modules.replace_from(m1038_humvee, 'ApparenceModel', by_name=True)
    m998_humvee_supply.modules.replace_from(m1038_humvee, 'GenericMovement', by_name=True)
    m998_humvee_supply.modules.replace_from(m1038_humvee, 'LandMovement', by_name=True)
    m998_humvee_supply.modules.replace_from(m1038_humvee, 'TBaseDamageModuleDescriptor')

def edit_with_rover101fc(m998_humvee_supply: BasicUnitCreator, rover_101fc_supply: UnitWrapper) -> None:
    m998_humvee_supply.modules.replace_from(rover_101fc_supply, 'TSupplyModuleDescriptor')
    m998_humvee_supply.modules.production.command_point_cost\
         = rover_101fc_supply.modules.production.command_point_cost