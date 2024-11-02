from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
from warno_mfw.context.mod_creation import ModCreationContext


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # Mk.19 40mm
    with ctx.create_unit("Mk.19 40mm", "US", "HMGteam_Mk19_AB_US") as mk19:
        mk19.modules.ui.SpecialtiesList.remove('_para')
        mk19.modules.ui.UpgradeFromUnit='HMGteam_M2HB_US'
        mk19.modules.remove('TDeploymentShiftModuleDescriptor')
        return mk19
        