from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # M1075 PLS
    # copy of: HEMTT
    with ctx.create_unit("M1075 PLS", "US", "HEMTT_US", button_texture_src_path='img/units/m1075_pls/icon.png') as m1075_pls:
        m1075_pls.modules.ui.UpgradeFromUnit="HEMTT_US"
        return m1075_pls