import utils.ndf.edit as edit
from context.mod_creation import ModCreationContext
from context.unit_module import UnitModuleContext
from creators.ammo import AmmoCreator
from creators.unit.basic import UNIT_UI
from creators.weapon import WeaponCreator
from metadata.division_unit_registry import UnitRules
from metadata.unit import UnitMetadata
from ndf_parse.model import List, ListRow


def create(ctx: ModCreationContext) -> UnitRules | None:
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
        return UnitRules(xm142_himars_he, 2, [0, 4, 3, 0])
        