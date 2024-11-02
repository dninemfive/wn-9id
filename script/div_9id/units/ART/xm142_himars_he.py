import warno_mfw.utils.ndf.edit as edit
from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.context.unit_module import UnitModuleContext
from warno_mfw.creators.ammo import AmmoCreator
from warno_mfw.creators.unit.basic import UNIT_UI
from warno_mfw.creators.weapon import WeaponCreator
from warno_mfw.metadata.unit import UnitMetadata
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
from ndf_parse.model import List, ListRow


def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    # XM142 HIMARS [HE]
    # copy BM-21 Grad
    with ctx.create_unit("XM142 HIMARS [HE]", "US", "BM21_Grad_SOV") as xm142_himars_he:
        # copy MLRS ammo but with 6 instead of 12 shots
        ammo_name = 'Ammo_d9_RocketArt_M26_227mm_HE_x6'
        with ctx.create_ammo(ammo_name, 'Ammo_RocketArt_M26_227mm') as ammo:
            ammo.edit_members(NbTirParSalves=6,
                              AffichageMunitionParSalve=6)
        # change weapon
        with xm142_himars_he.edit_weapons() as weapons:
            edit.members(weapons.get_turret_weapon(0),
                         Ammunition=f'$/GFX/Weapon/{ammo_name}',
                         EffectTag="'FireEffect_RocketArt_M26_227mm'")
        # change nationalite
        xm142_himars_he.modules.type.edit_members(
            Nationalite='Allied',
            MotherCountry='US'
        )
        # update speed, fuel capacity
        # change upgradefromunit, countrytexture
        xm142_himars_he.modules.ui.edit_members(
            UpgradeFromUnit=None,
            CountryTexture='US'
        )
        # change unit dangerousness
        # change unit attack/defense value
        # change unit cost
        return xm142_himars_he
        