from ndf_parse.model import List, ListRow, Object
from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.creators.unit.abc import UnitCreator
from warno_mfw.hints.paths.GameData.Generated.Gameplay import Gfx as ndf_paths
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
from warno_mfw.utils.ndf import edit, ensure


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("AH-64A APACHE [SEAD]", "US", "AH64_Apache_US") as apache_sead:
        # upgrade from Apache ATAS or whatever is at the end of the apache upgrades list
        apache_sead.modules.ui.UpgradeFromUnit = 'AH64_Apache_emp1_US'
        add_weapon_descriptor(ctx.ndf[ndf_paths.WeaponDescriptor], apache_sead)
        # new MissileCarriage
        # same one for both in-game and showroom
        apache_sead.unit.modules.edit_members(
            'MissileCarriage',
            True,
            Connoisseur=add_missile_carriage(ctx.ndf[ndf_paths.MissileCarriage],
                                             apache_sead))
        subgenerators_name, subgenerators_showroom_name = 'SubGenerators_d9_AH64A_APACHE_SEAD_US', 'SubGenerators_Showroom_d9_AH64A_APACHE_SEAD_US'
        gfx_autogen_showroom = ctx.ndf[ndf_paths.Depictions.GeneratedDepictionAerialUnitsShowroom].by_name('Gfx_AH64_Apache_US_Showroom_Autogen').value.copy()
        edit.members(gfx_autogen_showroom, SubDepictionGenerators=[subgenerators_showroom_name])
        ctx.ndf[ndf_paths.Depictions.GeneratedDepictionAerialUnitsShowroom].add(ListRow(gfx_autogen_showroom, namespace='Gfx_d9_AH64A_APACHE_SEAD_US_Showroom_Autogen'))
        showroom_unit = ctx.get_unit('AH64_Apache_US', showroom=True).copy()
        showroom_unit.modules.edit_members('TApparenceModelModuleDescriptor',
                                           Depiction=...)
        # new missilecarriagedepiction
        missile_carriage_depiction = ensure.NdfObject(
            'TStaticMissileCarriageSubDepictionGenerator',
            MissileCarriageConnoisseur='MissileCarriage_d9_AH64A_APACHE_SEAD_US',
            Missiles=[
                ensure.NdfObject(
                    'TStaticMissileCarriageSubDepictionMissileInfo',
                    Depiction=ensure.NdfObject(
                        'TemplateDepictionStaticMissilesGroundUnit',
                        PhysicalProperty=ensure.quoted('Tourelle3_MissileCount'),
                        ProjectileModelResource='$/GFX/DepictionResources/Modele_Missile_AGM_122_Sidearm' # oh hey would you look at that
                    ),
                    MissileCount=2,
                    WeaponIndex=2
                )
            ],
            Pylons='~/DepictionPylonSet_Helico_Default',
            ReferenceMesh=''
        )
        # maybe use the ATGM Apache model and do MissileCount=1 ProjectileModelResource=AIM-9 or smth?
        # note to self: make sure to set custom cadavre in addition to custom showroom unit
        # also nts: some way of creating a "base unit" e.g. base XM142, F-14, to avoid duplicating effort
        # oh also create the ammo and missile and stuff ofc
        # also also nts: stop returning UnitRules for this sort of thing, just return the unit; # of packs is always specified in .register(),
        # counts per pack can either be specified or looked up using the lookup class using the base unit
        # idea: .variant method on unit creators which creates a new unit which upgrades from the specified one and has specified changes 
        apache_sead.modules.production.command_point_cost = 250
        apache_sead.modules.ui.SpecialtiesList = ['sead']
        apache_sead.modules.ui.UpgradeFromUnit = 'AH64_Apache_emp1_US'
        return apache_sead
    
def add_weapon_descriptor(ndf: List, creator: UnitCreator) -> None:    
    weapon_descriptor: Object = ndf.by_name(creator.src_unit.weapon_descriptor.name).value.copy()
    turrets: List = weapon_descriptor.by_member('TurretDescriptorList').value
    turret_2: Object = turrets[1].value
    mounted_weapon: Object = turret_2.by_member('MountedWeaponDescriptorList').value[0].value
    mounted_weapon.by_member('Ammunition').value = '$/GFX/Weapon/Ammo_AA_AIM9J_Sidewinder'
    ndf.add(ListRow(weapon_descriptor, namespace=creator.new_unit.weapon_descriptor.name))
    creator.modules.edit_members('WeaponManager', True, Default=creator.new_unit.weapon_descriptor.path)

def add_missile_carriage(ndf: List, creator: UnitCreator, showroom: bool = False) -> str:
    missile_carriage = ensure.NdfObject(
        'TMissileCarriageConnoisseur',
        MeshDescriptor='$/GFX/DepictionResources/Modele_AH64_Apache_ATAS_US',
        PylonSet=f'~/DepictionPylonSet_Helico_Default{'_Showroom' if showroom else ''}',
        WeaponInfos=[
            ensure.NdfObject('TMissileCarriageWeaponInfo',
                            Count=2,
                            MissileType='eAGM',
                            WeaponIndex=2),
            ensure.NdfObject('TMissileCarriageWeaponInfo',
                            Count=8,
                            MissileType='eAGM',
                            WeaponIndex=3)                               
        ]
    )
    name: str = creator.new_unit.missile_carriage.showroom.name if showroom else creator.new_unit.missile_carriage.name
    ndf.add(ListRow(missile_carriage, namespace=name))
    return name

def add_subgenerators(ndf: List, creator: UnitCreator) -> str:
    pass