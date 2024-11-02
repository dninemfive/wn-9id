
from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
from ndf_parse.model import List, ListRow, Object


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("XM4 SLAMMER", "US", "Marder_1A3_RFA") as xm4_slammer:
        xm4_slammer.modules.ui.UpgradeFromUnit=None
        return xm4_slammer