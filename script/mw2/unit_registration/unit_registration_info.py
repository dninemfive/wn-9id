from dataclasses import dataclass
from typing import Iterable

from . import _types

@dataclass
class UnitRegistrationInfo(object):
    unit: str | _types.UnitDelegate
    packs: int
    units_per_xp: _types.UnitsPerXp | None = None
    transports: Iterable[_types.Transport] | None = None