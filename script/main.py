from context.mod_creation_context import ModCreationContext
from message import Message, try_nest
from misc.import_warno_scripts import import_script
from ndf_parse import Mod
from ndf_parse.model import ListRow, Object
# https://stackoverflow.com/a/5469427
from subprocess import Popen
from utils.ndf import dict_to_map
from metadata.division import DivisionMetadata
from metadata.mod import ModMetadata
from metadata.warno import WarnoMetadata
import os
# https://stackoverflow.com/a/1557364
import shutil
import sys

WARNO_DIRECTORY = rf"C:\Program Files (x86)\Steam\steamapps\common\WARNO"

wn_metadata = WarnoMetadata(WARNO_DIRECTORY)
mod_metadata = ModMetadata('dninemfive', '9th Infantry Division (Motorized)', wn_metadata, "0.0.0")
div_metadata = DivisionMetadata('d9', '9ID', 'US', 1390)

def reset_source():
    """ This is fucking unhinged and i need to fix it asap but it works for now """
    with Message("Resetting source") as msg:
        owd = os.getcwd()
        # silly but whatever
        with msg.nest(f"Changing cwd from {owd} to {wn_metadata.mods_path}") as _:
            os.chdir(wn_metadata.mods_path)
        # oh god this is stupid why am i doing this
        with msg.nest(f"Temporarily replacing my `utils` module with Eugen's utils") as _:
            my_utils = sys.modules["utils"]
            import_script(wn_metadata, "utils")
        with msg.nest(f"Deleting source files at {mod_metadata.source_path}") as _:
            shutil.rmtree(mod_metadata.source_path, ignore_errors=True)
        with msg.nest(f"Running CreateNewMod()") as _:
            import_script(wn_metadata, "CreateNewMod")
            getattr(sys.modules["CreateNewMod"], "CreateNewMod")(mod_metadata.relative_source_path)
        with msg.nest("undoing my insane changes") as _:
            sys.modules["utils"] = my_utils
            os.chdir(owd)

def run_bat(msg: Message | None, folder: str, name: str, *args):
    path = os.path.join(folder, f'{name}.bat')
    # https://stackoverflow.com/a/11729668
    path_and_args = [path, *args, '<nul']
    with try_nest(msg, f"Running command `{" ".join(path_and_args)}` in `{folder}`", force_nested=True) as _:
        Popen(path_and_args, cwd=folder).wait()

def reset_source_sane():
    with Message("Resetting source (sane version)") as msg:
        with msg.nest("Deleting existing files") as _:
            shutil.rmtree(mod_metadata.source_path, ignore_errors=True)
        run_bat(msg, wn_metadata.mods_path, "CreateNewMod", mod_metadata.relative_source_path)

def generate_mod():
    run_bat(None, mod_metadata.output_path, "GenerateMod")
    

# reset_source()
reset_source_sane()
mod = Mod(mod_metadata.source_path, mod_metadata.output_path)
mod.check_if_src_is_newer()

guid_cache_path: str = "guid_cache.txt"

# make packlist
pack_list: dict[str, int] = {
    '~/Descriptor_Deck_Pack_AH1F_ATAS_US': 2,
    '~/Descriptor_Deck_Pack_AH1F_Cobra_US': 4,
    '~/Descriptor_Deck_Pack_AH1S_Cobra_US': 4,
    '~/Descriptor_Deck_Pack_AH64_Apache_US': 2,
    '~/Descriptor_Deck_Pack_ATteam_TOW2_US': 2,
    '~/Descriptor_Deck_Pack_Airborne_CMD_US': 1,
    '~/Descriptor_Deck_Pack_Airborne_Dragon_US': 2,
    '~/Descriptor_Deck_Pack_Airborne_Scout_US': 1,
    '~/Descriptor_Deck_Pack_CH47_Super_Chinook_US': 2,
    '~/Descriptor_Deck_Pack_EH60A_EW_US': 1,
    '~/Descriptor_Deck_Pack_Engineer_CMD_US': 2,
    '~/Descriptor_Deck_Pack_FOB_US': 1,
    '~/Descriptor_Deck_Pack_Howz_M102_105mm_US': 2,
    '~/Descriptor_Deck_Pack_Howz_M198_155mm_US': 2,
    '~/Descriptor_Deck_Pack_LRRP_US': 1,
    '~/Descriptor_Deck_Pack_M577_US': 1,
    '~/Descriptor_Deck_Pack_M981_FISTV_US': 1,
    '~/Descriptor_Deck_Pack_MANPAD_Stinger_C_US': 1,
    '~/Descriptor_Deck_Pack_Mortier_107mm_US': 2,
    '~/Descriptor_Deck_Pack_OH58C_CMD_US': 1,
    '~/Descriptor_Deck_Pack_OH58C_Scout_US': 2,
    '~/Descriptor_Deck_Pack_OH58D_Combat_Scout_US': 1,
    '~/Descriptor_Deck_Pack_Ranger_Dragon_US': 1,
    '~/Descriptor_Deck_Pack_Rifles_Cavalry_US': 1,
    '~/Descriptor_Deck_Pack_Rifles_half_AT4_US': 1,
    '~/Descriptor_Deck_Pack_Rifles_half_CMD_US': 1,
    '~/Descriptor_Deck_Pack_Rifles_half_Dragon_US': 4,
    '~/Descriptor_Deck_Pack_Sniper_US': 1,
    '~/Descriptor_Deck_Pack_UH60A_CO_US': 1,
    '~/Descriptor_Deck_Pack_UH60A_Supply_US': 1,
    # add new units here...
}
with ModCreationContext(mod_metadata, 'guid_cache.txt') as mod_context:
        mod_context.create_division(div_metadata,
                                    "Descriptor_Deck_Division_US_82nd_Airborne_multi",
                                    None,
                                    DescriptionHintTitleToken = "'ECGMWQOEZA'",                             # 8th Infantry Division (Mech.)
                                    EmblemTexture = '"Texture_Division_Emblem_US_35th_infantry_division"',
                                    PackList = dict_to_map(pack_list))
        # make new units
        
        """ LOG """
        # M998 HUMVEE SUPPLY
        #   copy of: M35 Supply
        #   but with:
        #       "UNITE_M35_supply_US" replaced in TTagsModuleDescriptor
        #       ApparenceModel replaced with that of M998 Humvee
        #       GenericMovement replaced with that of M998 Humvee
        #       LandMovement replaced with that of M998 Humvee (if different)
        #       TSupplyModuleDescriptor replaced with that of Rover 101FC Supply
        #       TProductionModuleDescriptor/ProductionResourcesNeeded changed to appropriate value
        #           (replaced with that of Rover 101FC Supply?)
        #       TUnitUIModuleDescriptor/NameToken replaced with that of M998 Humvee (for now)
        #       TUnitUIModuleDescriptor/UpgradeFromUnit cleared
        # M1075 PLS
        # copy of: HEMTT
        # but with:
        #       TUnitUIModuleDescriptor/NameToken replaced with that of M1038 Humvee (for now)
        #       TUnitUIModuleDescriptor/UpgradeFromUnit set to M998 HUMVEE SUPPLY
        #       unit rule xp should also be higher
        # ✪ M998 HUMVEE SGT.
        # ✪ M1025 HUMVEE AGL
        # ✪ M1010 TC3V
        """ INF """
        # MOT. MP PATROL
        # (just copy AB MP PATROL)
        # for MOT. infantry: copy MECH. version, but reduce men to 8 and replace M240B with SAW and LAW with AT-4
        # ✪ MOT. RIFLES LDR.
        # MOT. RIFLES (AT-4)
        # MOT. RIFLES (DRAGON)
        # ✪ MOT. ENGINEERS LDR.
        # MOT. ENGINEERS
        # M998 HUMVEE SQC
        # just copy M1038 HUMVEE
        # M998 HUMVEE M2HB
        # copy the AB version, but no forward deploy and normal vision
        # M998 HUMVEE AGL
        # copy the AB version, but no forward deploy and normal vision
        """ ART """
        # M198 155mm [CLU]
        # M198 COPPERHEAD
        # M58 MICLIC
        # XM142 HIMARS [HE]
        # XM142 HIMARS [CLU]
        # XM142 ATACMS
        # XM119 IMCS 105mm
        # XM1100 120mm
        """ TNK """
        # XM4 AGS
        # RDF/LT
        # M966 HUMVEE TOW
        # M1025 HUMVEE TOW
        # M998 HUMVEE GLH-L
        # M1025 HUMVEE AGL
        """ REC """
        # 👓 M998 HUMVEE M2HB
        # copy 👓 M1025 HUMVEE M2HB
        # 👓 FAV
        # 👓 FAV AGL
        # 👓 FAV TOW
        # 👓 OPERATIONAL SUPPORT
        # [👓] FOLT
        # 👓 FWD SUPPORT [EW]
        # [👓] MERCURY GREEN RPV
        # [👓] MOT. SCOUTS
        # copy SCOUTS, but replace M240 with SAW
        # [👓] SCAT
        # [[👓]] JOH-58D KIOWA
        # [[👓]] M561 GAMA GOAT FAAR
        """ AA """
        # JOH-58C KIOWA
        # M167A1 VADS 20mm
        # copy AB version, remove forward deploy and add the air-transportable trait
        # M998 AVENGER
        # copy AB version, remove forward deploy
        # M998 SETTER
        # MIM-72A T-CHAPARRAL
        # STINGER (TDAR)
        # EXCALIBUR VWC
        """ HEL """
        # AH-1S COBRA
        """ AIR """
        # A-6E INTRUDER [HE]
        # A-6E INTRUDER [CLU]
        # A-6E INTRUDER [LGB]
        # A-6E INTRUDER SWIP
        # EA-6B PROWLER [SEAD]
        # EA-6B PROWLER [EW]
        # A-7E CORSAIR II [HE]
        # A-7E CORSAIR II [SEAD]
        # F-14B TOMCAT [AA]
        # F-14B TOMCAT [LGB]
        # F/A-18C [AA]
        # F/A-18D [FAC]

        # add a default deck to Decks.ndf (not required)

generate_mod()