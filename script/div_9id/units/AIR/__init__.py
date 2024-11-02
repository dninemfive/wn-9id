from warno_mfw.unit_registration.division_unit_registry import DivisionUnitRegistry
from warno_mfw.unit_registration.unit_group import UnitGroup
from warno_mfw.unit_registration.unit_registration_info import \
    UnitRegistrationInfo as u
from warno_mfw.utils.types.message import Message

from .a6e_he        import create as intruder_he
from .a6e_clu       import create as intruder_clu
from .a6e_lgb       import create as intruder_lgb
from .a6e_swip      import create as intruder_swip
from .a7e_he        import create as corsair_he
from .a7e_nplm      import create as corsair_nplm
from .a7e_sead      import create as corsair_sead
from .ea6b_sead     import create as prowler_sead
from .ea6b_ew       import create as prowler_ew
from .f14b_aa1      import create as tomcat_aa1
from .f14b_aa2      import create as tomcat_aa2
from .f14b_lgb      import create as tomcat_lgb

def group(registry: DivisionUnitRegistry, parent_msg: Message | None = None) -> UnitGroup:
    return UnitGroup(
        'AIR',
        registry,
        parent_msg,
        (
            'A-6 Intruder',
            [
                u(intruder_he,      1),
                u(intruder_clu,     1),
                u(intruder_lgb,     1),
                u(intruder_swip,    1)
            ]
        ),
        (
            'EA-6 Prowler',
            [
                u(prowler_sead,     1),
                u(prowler_ew,       1)
            ]
        ),
        (
            'A-7 Corsair II',
            [
                u(corsair_he,   1),
                u(corsair_nplm, 1),
                u(corsair_sead, 1)
            ]
        ),
        (
            'F-14 Tomcat',
            [
                u(tomcat_aa1,   1),
                u(tomcat_aa2,   1),
                u(tomcat_lgb,   1)
            ]
        )
    )