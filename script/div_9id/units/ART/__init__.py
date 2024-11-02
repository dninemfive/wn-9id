from div_9id.units.transports import BLACKHAWK, M35, M998_HUMVEE
from warno_mfw.unit_registration.division_unit_registry import DivisionUnitRegistry
from warno_mfw.unit_registration.unit_group import UnitGroup
from warno_mfw.unit_registration.unit_registration_info import \
    UnitRegistrationInfo as u
from warno_mfw.utils.types.message import Message

from .m198_155mm_clu        import create as m198_clu
from .m198_copperhead       import create as m198_copperhead_
from .xm119_imcs            import create as xm119
from .xm142_himars_clu      import create as xm142_clu
from .xm142_himars_he       import create as xm142_he
from .xm142_himars_atacms   import create as xm142_atacms
from .xm1100_120mm          import create as xm1100
from .m58_miclic            import create as miclic

LIGHT_TRANSPORTS = [M998_HUMVEE, BLACKHAWK]

def group(registry: DivisionUnitRegistry, parent_msg: Message | None = None) -> UnitGroup:
    return UnitGroup(
        'ART',
        registry,
        parent_msg,
        (
            'Mortars',
            [
                u('Mortier_107mm_US', 2, transports=LIGHT_TRANSPORTS),
                u(xm1100, 1)
            ]
        ),
        (
            '105mm Howitzers',
            [
                u('Howz_M102_105mm_US', 2, transports=LIGHT_TRANSPORTS),
                u(xm119, 1)
            ]
        ),
        (
            '155mm Howitzers',
            [
                u('Howz_M198_155mm_US', 2,    transports=M35),
                u(m198_clu,             1, (0, 2, 1, 0), M35),
                u(m198_copperhead_,     1, (0, 1, 0, 0), M35)
            ]
        ),
        (
            'Rocket Artillery',
            [
                u(xm142_clu,        1, (0, 2, 1, 0)),
                u(xm142_he,         1, (0, 2, 1, 0)),
                u(xm142_atacms,     1, (0, 1, 0, 0)),
                u(miclic,           1,  (0, 2, 1, 0), M35)
            ]
        )
        # Fire Direction
        #   M998 HUMVEE LTACFIRE
    )