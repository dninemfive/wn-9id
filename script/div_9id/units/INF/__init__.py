from div_9id.units.transports import (BLACKHAWK,
                                      M998_HUMVEE,
                                      M1025_HUMVEE_MP,
                                      M1038_HUMVEE,
                                      Transports)
from warno_mfw.unit_registration.division_unit_registry import DivisionUnitRegistry
from warno_mfw.unit_registration.unit_group import UnitGroup
from warno_mfw.unit_registration.unit_registration_info import \
    UnitRegistrationInfo as u
from warno_mfw.utils.types.message import Message

from .cmd_mot_rifles_ldr import create as mot_rifles_ldr
from .m224_60mm          import create as m224
from .mk19_40mm          import create as mk19
from .mot_engineers      import create as mot_engineers_
from .mot_mp_patrol      import create as mot_mp
from .mot_rifles         import create as mot_rifles_
from .mot_rifles_dragon  import create as mot_rifles_dragon_
from .ranger_at_section  import create as rangers_at
from .ranger_gunners     import create as rangers_mg
from .rangers_m203       import create as rangers_m203_
from .m1025_humvee_agl   import create as m1025_agl


def group(registry: DivisionUnitRegistry, parent_msg: Message | None = None) -> UnitGroup:
    M998_HUMVEE_M2HB    = Transports.singleton.M998_HUMVEE_M2HB
    M998_HUMVEE_AGL     = Transports.singleton.M998_HUMVEE_AGL
    return UnitGroup(
        'INF',
        registry,
        parent_msg,
        (
            'Mot. Rifles',
            [
                u(mot_rifles_ldr,           3, transports=[M1038_HUMVEE, M998_HUMVEE_M2HB, M998_HUMVEE_AGL, BLACKHAWK]),
                u(mot_rifles_,              1, transports=[M1038_HUMVEE,                   M998_HUMVEE_AGL, BLACKHAWK]),
                u(mot_rifles_dragon_,       2, transports=[M1038_HUMVEE, M998_HUMVEE_M2HB,                  BLACKHAWK])
            ]
        ),
        (
            'Engineers',
            [
                u('Engineer_CMD_US',        1, transports=[M1038_HUMVEE,                   M998_HUMVEE_AGL]),
                u(mot_engineers_,           2, transports=[M1038_HUMVEE,                   M998_HUMVEE_AGL]),
                u('Engineers_Dragon_US',    1, transports=[M1038_HUMVEE, M998_HUMVEE_M2HB])
            ]
        ),
        (
            'Airborne',
            [
                u('Airborne_CMD_US',        1, transports=[M1038_HUMVEE]),
                u('Airborne_Dragon_US',     1, transports=[M1038_HUMVEE])
            ]
        ),
        (
            'Rangers',
            [
                u(rangers_m203_,            1, transports=[M1038_HUMVEE,                   M998_HUMVEE_AGL, BLACKHAWK]),
                u(rangers_at,               1, transports=[M1038_HUMVEE, M998_HUMVEE_M2HB,                  BLACKHAWK]),
                u(rangers_mg,               1, transports=[M1038_HUMVEE, M998_HUMVEE_M2HB,                  BLACKHAWK])
            ]
        ),
        (
            'Support',
            [
                u(mk19,                     2, transports=[M998_HUMVEE,                    M998_HUMVEE_AGL]),
                u(m224,                     2, (6,4,2,0), [M998_HUMVEE,                                     BLACKHAWK])
            ]
        ),
        (
            'Misc',
            [
                u(mot_mp,                   2, transports=[M998_HUMVEE,  M1025_HUMVEE_MP]),
                u('Rifles_Cavalry_US',      2, transports=[              M998_HUMVEE_M2HB, M998_HUMVEE_AGL, BLACKHAWK]),
                u('Rifles_HMG_US',          1, transports=[M1038_HUMVEE, M998_HUMVEE_M2HB,                  BLACKHAWK]),
                u('ATteam_TOW2_US',         2, transports=[M998_HUMVEE,                    M998_HUMVEE_AGL]),
                u(m1025_agl,                5, (0, 8, 5, 0))
            ]
        )
    )