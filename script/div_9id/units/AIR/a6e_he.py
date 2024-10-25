from dataclasses import dataclass
from typing import Literal, Self

import mw2.utils.ndf.edit as edit
import mw2.utils.ndf.ensure as ensure
from mw2.constants import ndf_paths
from mw2.context.mod_creation import ModCreationContext
from mw2.context.unit_module import UnitModuleContext
from mw2.metadata.unit import NamePathPair, UnitMetadata
from mw2.unit_registration.new_src_unit_pair import NewSrcUnitPair
from ndf_parse.model import List, ListRow, Object


@dataclass
class TMissileCarriageWeaponInfo(object):
    Count: int
    MissileType: Literal['eAGM', 'eAAM']
    WeaponIndex: int
    MountingType: Literal['eMountingDefault', 'eMountingMissile', 'eMountingPod', 'eMountingBomb'] = 'eMountingDefault'

    def to_ndf(self: Self) -> Object:
        return ensure._object('TMissileCarriageWeaponInfo',
                              Count=self.Count,
                              MissileType=self.MissileType,
                              MountingType=self.MountingType,
                              WeaponIndex=self.WeaponIndex)

PylonSetType = Literal['ATGM',
                       'Airplane_Default',
                       'Airplane_FR',
                       'Airplane_RFA',
                       'Airplane_SOV',
                       'Airplane_UK',
                       'Airplane_US',
                       'Helico_Default',
                       'Helico_SOV',
                       'Vehicle_Default']

class TMissileCarriageConnoisseur(object):
    def __init__(self: Self, mesh_descriptor: str, pylon_set: PylonSetType, *weapon_infos: TMissileCarriageWeaponInfo):
        self.MeshDescriptor = mesh_descriptor
        self.PylonSet = ensure.prefix(pylon_set, '~/DepictionPylonSet_')
        self.WeaponInfos: list[TMissileCarriageWeaponInfo] = []
        for item in weapon_infos:
            self.add(item)

    def add(self: Self, weapon_info: TMissileCarriageWeaponInfo):
        self.WeaponInfos.append(weapon_info)
        self.WeaponInfos = list(sorted(self.WeaponInfos, key=lambda x: x.WeaponIndex))

    def to_ndf(self: Self, showroom: bool = False) -> Object:
        return ensure._object(
            'TMissileCarriageConnoisseur',
            MeshDescriptor=self.MeshDescriptor,
            PylonSet=f'{self.PylonSet}{'_Showroom' if showroom else ''}',
            WeaponInfos=[x.to_ndf() for x in self.WeaponInfos]
        )
    
@dataclass
class TemplateDepictionStaticMissilesAirUnit(object):
    PhysicalProperty: str
    ProjectileModelResource: str

@dataclass
class TStaticMissileCarriageSubDepictionMissileInfo(object):
    Depiction: TemplateDepictionStaticMissilesAirUnit
    MissileCount: int
    WeaponIndex: int

    def to_ndf(self: Self) -> Object:
        return ensure._object(
            'TStaticMissileCarriageSubDepictionGenerator',
            Depiction=self.Depiction,
            MissileCount=self.MissileCount,
            WeaponIndex=self.WeaponIndex
        )
    
class TStaticMissileCarriageSubDepictionGenerator(object):
    def __init__(self: Self, reference_mesh: str, pylons: PylonSetType, *missiles: TStaticMissileCarriageSubDepictionMissileInfo):
        self.ReferenceMesh = reference_mesh
        self.Pylons = ensure.prefix(pylons, '~/DepictionPylonSet_')
        self.Missiles = sorted(missiles, key=lambda x: x.WeaponIndex)

    def to_ndf(self: Self, unit: UnitMetadata, showroom: bool = False) -> Object:
        return ensure._object(
            'TStaticMissileCarriageSubDepictionGenerator',
            MissileCarriageConnosseur=unit.missile_carriage.showroom_if(showroom).path,
            Missiles=[x.to_ndf() for x in self.Missiles],
            Pylons=f'{self.Pylons}{'_Showroom' if showroom else ''}',
            ReferenceMesh=self.ReferenceMesh
        )

MK_82_X12 = TMissileCarriageWeaponInfo(12, 'eAGM', 2, 'eMountingBomb')
AIM_9L_X2 = TMissileCarriageWeaponInfo(2, 'eAAM', 3)
MISSILE_CARRIAGE_CONNOISSEUR = TMissileCarriageConnoisseur(
    '$/GFX/DepictionResources/Modele_F4F_Phantom_II_HE1_RFA',
    'Airplane_Default',
    MK_82_X12,
    AIM_9L_X2
)
SUBGENERATOR = TStaticMissileCarriageSubDepictionGenerator(
    '$/GFX/DepictionResources/Modele_F4F_Phantom_II_HE2_RFA',
    'Airplane_Default',
    MK_82_X12,
    AIM_9L_X2
)

def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("A-6E INTRUDER [HE]", "US", "F4F_Phantom_II_HE1_RFA") as a6e_he:
        a6e_he.modules.ui.UpgradeFromUnit=None
        a6e_he.unit.set_country('US')
        with a6e_he.edit_weapons() as weapons:
            weapons.Salves.remove(0)
            weapons.SalvoIsMainSalvo.remove(0)
            weapons.TurretDescriptorList.remove(0)
        # add_carriages(ctx.ndf[ndf_paths.MISSILE_CARRIAGE], a6e_he.new_unit, MISSILE_CARRIAGE_CONNOISSEUR)
        # add_carriages(ctx.ndf[ndf_paths.MISSILE_CARRIAGE_DEPICTION], a6e_he.new_unit, SUBGENERATOR)
        # make new entry in GeneratedDepictionAerialUnitsShowroom.ndf pointing at the SubGenerators
        # copy relevant Ops?
        # do the same for non-showroom files
        return a6e_he
    
def add_carriage(ndf: List, unit: UnitMetadata, connoisseur: TMissileCarriageConnoisseur, showroom: bool = False) -> NamePathPair:
    ndf.add(ListRow(
        connoisseur.to_ndf(showroom),
        namespace=unit.missile_carriage.showroom.name if showroom else unit.missile_carriage.name
    ))
    return unit.missile_carriage.showroom if showroom else unit.missile_carriage

def add_carriages(ndf: List, unit: UnitMetadata, connoisseur: TMissileCarriageConnoisseur) -> tuple[NamePathPair, NamePathPair]:
    return (
        add_carriage(ndf, unit, connoisseur, showroom=False),
        add_carriage(ndf, unit, connoisseur, showroom=True)
    )

def add_subgenerator(ndf: List, unit: UnitMetadata, subgenerator: TStaticMissileCarriageSubDepictionGenerator, showroom: bool = False) -> str:
    ndf.add(ListRow(
        subgenerator.to_ndf(showroom),
        namespace=unit.reference_mesh.path
    ))
    return unit.subgenerators.path

def add_carriages(ndf: List, unit: UnitMetadata, subgenerator: TStaticMissileCarriageSubDepictionGenerator) -> tuple[str, str]:
    return (
        add_subgenerator(ndf, unit, subgenerator, showroom=False),
        add_subgenerator(ndf, unit, subgenerator, showroom=True)
    )