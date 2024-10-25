from mw2.context.mod_creation import ModCreationContext
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # 👓 FAV
    with ctx.create_unit("#RECO1 FAV", "US", "Iltis_trans_RFA") as fav:
        fav.modules.type.edit_members(
            AcknowUnitType='Reco',
            TypeUnitFormation='Reconnaissance'
        )
        fav.unit.set_country('US')
        fav.modules.production.Factory = 'Recons'
        fav.tags.add('Vehicule_Reco')
        fav.modules.ui.edit_members(
            SpecialtiesList=['reco', '_transport1', 'air_transportable'],
            MenuIconTexture='RECO_veh',
            TypeStrategicCount='Reco_Veh'
        )
        # stealth, vision: M151A2 M2HB
        m151a2_scout = ctx.get_unit('M151A2_scout_US')
        fav.modules.replace_from(m151a2_scout, 'TVisibilityModuleDescriptor')
        fav.modules.replace_from(m151a2_scout, 'TScannerConfigurationDescriptor')
        fav.modules.replace_from(m151a2_scout, 'TReverseScannerWithIdentificationDescriptor')
        fav.modules.replace_from(m151a2_scout, 'TTacticalLabelModuleDescriptor')
        fav.modules.append_from( m151a2_scout, 'TDeploymentShiftModuleDescriptor')
        # add a little bit of ECM to represent being a very small target?
        return fav