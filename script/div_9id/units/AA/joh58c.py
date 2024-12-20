import warno_mfw.utils.ndf.edit as edit
import warno_mfw.utils.ndf.ensure as ensure
from ndf_parse.model import List, ListRow, Object
from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.creators.unit.basic import UNIT_UI
from warno_mfw.creators.weapon import WeaponCreator
from warno_mfw.hints.paths.GameData.Generated.Gameplay import Gfx as ndf_paths
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # JOH-58C
    # 1 minigun, 2 stingers
    with ctx.create_unit("JOH-58C/S", "US", "OH58_CS_US") as joh58c:
        with joh58c.edit_weapons() as weapons:
            edit_weapons(weapons)
        joh58c.modules.get('MissileCarriage', by_name=True).by_member('Connoisseur').value = generate_missile_carriages(ctx.ndf[ndf_paths.MissileCarriage])
        ctx.get_unit('OH58_CS_US').modules.ui.UpgradeFromUnit = joh58c
        return joh58c
    
def generate_ammo_descriptor(ctx: ModCreationContext) -> str:
    ammo_name = 'Ammo_AGM_BGM71D_TOW_2A_x4'
    copy: Object = ctx.ndf[ndf_paths.AmmunitionMissiles].by_name('Ammo_ATGM_BGM71D_TOW_2A_x2').value.copy()
    copy.by_member('DescriptorId').value = ctx.guids.generate(ammo_name)
    
def edit_weapons(weapons: WeaponCreator) -> str:
    # set ammo
    weapons.Salves = [1,1]
    # copy first turret unit descriptor from Kiowa WR; replace ammunition with TOW 2A x4
    #       Ammo_AGM_BGM71D_TOW_2_x4
    # TOW 2A instead?
    weapons.get_turret_weapon(0).by_member('Ammunition').value = '$/GFX/Weapon/Ammo_AGM_BGM71D_TOW_2_x4'
    weapons.add_mounted_weapon(Ammunition='$/GFX/Weapon/Ammo_RocketAir_Hydra_70mm_x19',
                               EffectTag="'FireEffect_RocketAir_Hydra_70mm_x19'")

def make_mounted_weapon(weapons: WeaponCreator,
                        base: Object | None = None,
                        weapon_index:           int = 0,
                        turret_index:           int = 0,
                        mesh_offset:            int = 1,
                        weapon_shoot_data_ct:   int = 1,
                        **changes) -> Object:
    copy: Object = base.copy() if base is not None else weapons.get_turret_weapon(turret_index, 0)
    mesh_index = weapon_index + mesh_offset
    weapon_shoot_datas = [f'"WeaponShootData_{x}_{mesh_index}"' for x in range(weapon_shoot_data_ct)]
    edit.members(copy,
                 HandheldEquipmentKey=f"'MeshAlternative_{mesh_index}'",
                 SalvoStockIndex=weapon_index,
                 WeaponActiveAndCanShootPropertyName=f"'WeaponActiveAndCanShoot_{mesh_index}'",
                 WeaponIgnoredPropertyName=f"'WeaponIgnored_{mesh_index}'",
                 WeaponShootDataPropertyName=weapon_shoot_datas,
                 **changes)
    return copy

def generate_missile_carriages(missile_carriage_ndf: List) -> str:
    copy: Object = missile_carriage_ndf.by_name('MissileCarriage_OH58D_Combat_Scout_US').value.copy()
    edit.members(copy,
                 WeaponInfos=[
                    ensure.NdfObject('TMissileCarriageWeaponInfo', 
                                Count=4,
                                MissileType='eAGM',
                                MountingType='eMountingPod',
                                WeaponIndex='0'),
                    ensure.NdfObject('TMissileCarriageWeaponInfo', 
                                Count=19,
                                MissileType='eAGM',
                                MountingType='eMountingPod',
                                WeaponIndex='1')
                ])
    missile_carriage_ndf.add(ListRow(copy, namespace='MissileCarriage_d9_JOH58D_KIOWA_US'))
    showroom_copy = copy.copy()
    edit.members(showroom_copy, PylonSet='~/DepictionPylonSet_Helico_Default_Showroom')
    missile_carriage_ndf.add(value=showroom_copy, namespace='MissileCarriage_d9_JOH58D_KIOWA_US_Showroom')
    return 'MissileCarriage_d9_JOH58CS_US'