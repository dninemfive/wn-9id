from mw2.unit_registration.division_unit_registry import DivisionUnitRegistry
from mw2.unit_registration.unit_group import UnitGroup
from mw2.unit_registration.unit_registration_info import UnitRegistrationInfo as u
from mw2.utils.types.message import Message

from .cmd_m997_tc3v import create as cmd_m997_tc3v_
from .m998_humvee_supply import create as m998_humvee_supply_


def group(registry: DivisionUnitRegistry, parent_msg: Message | None = None) -> UnitGroup:
    return UnitGroup(
        'LOG',
        registry,
        parent_msg,
        (
            'Command',
            [
                u('M1025_Humvee_CMD_US', 2),
                u(cmd_m997_tc3v_, 1),
                u('OH58C_CMD_US', 1),
            ]
        ),
        (
            'Supply',
            [
                u('FOB_US', 1),
                u(m998_humvee_supply_, 2),
                u('M35_supply_US', 1),
                u('HEMTT_US', 2, (0, 3, 2, 0)),
                u('UH60A_Supply_US', 2),
                u('CH47_Super_Chinook_US', 2),
            ]
        )
    )