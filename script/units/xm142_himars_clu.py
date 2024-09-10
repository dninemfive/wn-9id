from context.module_context import ModuleContext
from context.unit_creation_context import UnitCreationContext
from metadata.division_unit_registry import UnitInfo
from metadata.unit import UnitMetadata
from misc.unit_creator import UNIT_UI
from misc.ammo_creator import AmmoCreator
from misc.weapon_creator import WeaponCreator
from ndf_parse.model import List, ListRow
from utils.ndf import to_List as qlist

def create(ctx: UnitCreationContext) -> UnitInfo | None:
    # M198 155mm COPPERHEAD
    # copy M198 155mm
    with ctx.create_unit("XM142 HIMARS [CLU]", "US", "lars probably idk") as m198_clu:
        # copy MLRS ammo but with 6 instead of 12 shots
        with AmmoCreator(ctx, "RocketArt_M26_227mm_Cluster_HIMARS") as ammo:
            ammo.edit_members(NbTirParSalves=6,
                              AffichageMunitionParSalve=6)
        with WeaponCreator(ctx, m198_clu.new, "M270_MLRS_cluster_US") as weapon:
            weapon.object.by_member("TurretDescriptorList").value.<first>.by_member("MountedWeaponDescriptorList").value.<first>.by_member("Ammunition").value = "Ammo_d9_RocketArt_M26_227mm_Cluster_HIMARS"
        with m198_clu.module_context('TBaseDamageModuleDescriptor') as damage_module:
            # TODO: dynamically adjust this from M198 
            damage_module.edit_members(MaxPhysicalDamages=7)
        # update transportable (TODO: automate this)
        with m198_clu.module_context('TTransportableModuleDescriptor') as transportable_module:
            transportable_module.edit_members(TransportedSoldier='"d9_M198_COPPERHEAD_US"')
        # upgrade from M198 [CLU]
        with m198_clu.module_context('TUnitUIModuleDescriptor') as ui_module:
            ui_module.edit_members(UpgradeFromUnit="Descriptor_Unit_d9_M198_155mm_CLU_US")
        # change unit dangerousness (see 2S3M1 vs regular)
        # change unit attack/defense value (see 2S3M1 vs regular)
        # change unit cost (see 2S3M1 vs regular)
        return UnitInfo(m198_clu, 2, [0, 4, 3, 0])
        