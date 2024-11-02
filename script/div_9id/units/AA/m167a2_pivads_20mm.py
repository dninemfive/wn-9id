from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.creators.unit.basic import UNIT_UI
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
from ndf_parse.model import List, ListRow


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # M167A2 PIVADS 20mm
    # copy AB version
    with ctx.create_unit("M167A2 PIVADS 20mm", "US", "DCA_M167A2_Vulcan_20mm_Aero_US") as m167a2_pivads:
        # add air-transportable trait
        m167a2_pivads.modules.ui.edit_members(SpecialtiesList=['AA', '_canBeAirlifted'],
                                              UpgradeFromUnit='DCA_M167A2_Vulcan_20mm_US')
        # ensure air-transportable with transportation module
        # add "CanBeAirlifted" to tags
        m167a2_pivads.tags.add('CanBeAirlifted')
        
        # advanced: replace soldiers manning it with normal instead of airborne models
        # advanced: insert before AERO-M167A2 PIVADS 20mm
        ctx.get_unit('DCA_M167A2_Vulcan_20mm_Aero_US').modules.ui.UpgradeFromUnit = m167a2_pivads
        return m167a2_pivads