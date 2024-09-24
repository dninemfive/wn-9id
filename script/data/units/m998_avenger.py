from lib.context.mod_creation_context import ModCreationContext
from lib.context.module_context import ModuleContext
from lib.creators.unit import UNIT_UI
from lib.metadata.division_unit_registry import UnitRules
from lib.metadata.unit import UnitMetadata
from ndf_parse.model import List, ListRow
import lib.utils.ndf.ensure as ensure


def create(ctx: ModCreationContext) -> UnitRules | None:
    # M998 AVENGER
    # copy AB M998 AVENGER
    with ctx.create_unit("M998 Avenger", "US", "M998_Avenger_US") as m998_avenger:
        # remove forward deploy
        m998_avenger.remove_module("TDeploymentShiftModuleDescriptor")
        # remove para trait
        m998_avenger.edit_ui_module(SpecialtiesList=ensure._list("'AA'"))
        # make AB M998 AVENGER upgrade from M998 AVENGER
        # TODO: maybe allow deployment via CH-47D?
        return UnitRules(m998_avenger, 2, [0, 4, 3, 0])
        