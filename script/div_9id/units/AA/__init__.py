from div_9id.units.transports import BLACKHAWK, M35, M998_HUMVEE, Transports
from warno_mfw.unit_registration.division_unit_registry import DivisionUnitRegistry
from warno_mfw.unit_registration.unit_group import UnitGroup
from warno_mfw.unit_registration.unit_registration_info import \
    UnitRegistrationInfo as u
from warno_mfw.utils.types.message import Message

from .joh58c             import create as joh58c_
from .m167a2_pivads_20mm import create as m167a2
from .m998_avenger       import create as avenger
from .stinger_tdar       import create as stinger_tdar_
from .xm85_t_chaparral   import create as t_chap
from .excalibur_vwc      import create as excalibur


def group(registry: DivisionUnitRegistry, parent_msg: Message | None = None) -> UnitGroup:
    M998_HUMVEE_AGL     = Transports.singleton.M998_HUMVEE_AGL
    MANPADS_TRANSPORTS = [M998_HUMVEE, M998_HUMVEE_AGL, BLACKHAWK]
    return UnitGroup(
        'AA',
        registry,
        parent_msg,
        (
            'MANPADS',
            [
                u('MANPAD_Stinger_C_US',    1, transports=MANPADS_TRANSPORTS),
                u(stinger_tdar_,             1, transports=MANPADS_TRANSPORTS)
            ]
        ),
        (
            'VSHORAD',
            [
                u(m167a2, 2, transports=M998_HUMVEE),
                u(excalibur, 1, (0, 6, 4, 0))
            ]
        ),
        (
            'SHORAD',
            [
                u(t_chap,   1,    transports=M35),
                u(avenger,  2),
                # u(joh58c,   1)
            ]
        )
    )