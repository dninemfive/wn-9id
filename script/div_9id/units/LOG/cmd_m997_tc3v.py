import mw2.constants.ndf_paths as ndf_paths
from mw2.context.mod_creation import ModCreationContext
from mw2.context.unit_module import UnitModuleContext
from mw2.creators.unit.abc import UnitCreator
from mw2.creators.unit.basic import BasicUnitCreator
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair
from mw2.utils.ndf import ensure
from ndf_parse.model import List, ListRow, MemberRow, Object

from ._utils import m1038ify_m1025_gfx


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # ✪ M997 TC3V
    with ctx.create_unit("#CMD M997 TC3V", "US", "M1025_Humvee_CMD_US", 'M1038_Humvee_US') as m997_tc3v:
        m997_tc3v.modules.production.command_point_cost += 20
        m997_tc3v.modules.ui.ButtonTexture = 'M1038_Humvee_US'
        m997_tc3v.modules.ui.UpgradeFromUnit = 'M1025_Humvee_CMD_US'
        m997_tc3v.modules.edit_members('ApparenceModel',
                                       by_name=True,
                                       Depiction=m1038ify_m1025_gfx(ctx.ndf[ndf_paths.GENERATED_DEPICTION_VEHICLES], m997_tc3v.new_unit))
        return m997_tc3v