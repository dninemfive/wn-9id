from mw2.metadata.unit import UnitMetadata
from mw2.utils.ndf import edit, ensure
from ndf_parse.model import List, ListRow, Object


def m1038ify_m1025_gfx(generated_depiction_vehicles: List, unit: UnitMetadata) -> str:
    obj: Object = generated_depiction_vehicles.by_name(UnitMetadata('M1025_Humvee_CMD_US').gfx_autogen.name).value.copy()
    edit.members(obj,
                 CoatingName=ensure.quoted('M1038_Humvee_US'),
                 Selector='Selector_M1038_Humvee_US',
                 Alternatives='Alternatives_M1038_Humvee_US',
                 SubDepictions='[] + HumanSubDepictions_M1038_Humvee_US')
    generated_depiction_vehicles.add(ListRow(obj, namespace=unit.gfx_autogen.name))
    return unit.gfx_autogen.path