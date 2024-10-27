from mw2.metadata.unit import UnitMetadata
from mw2.utils.ndf import edit
from ndf_parse.model import List, ListRow, Object


def untransportify_m1038_gfx(generated_depiction_vehicles: List, unit: UnitMetadata) -> str:
    obj: Object = generated_depiction_vehicles.by_name(UnitMetadata('M1038_Humvee_US').gfx_autogen.name).value.copy()
    # subdepictions: List = obj.by_member('SubDepictions').value
    # subdepictions.remove(0)
    obj.by_member('SubDepictions').value = '[] + HumanSubDepictions_M1038_Humvee_US'
    edit.members(obj,
                 SubDepictionGenerators=[])
    generated_depiction_vehicles.add(ListRow(obj, namespace=unit.gfx_autogen.name))
    return unit.gfx_autogen.path