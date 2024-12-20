from __future__ import annotations

from datetime import datetime
from typing import Callable

import div_9id.ammo
import div_9id.ammo.fgr_17_viper
import div_9id.ammo.m60e3
import div_9id.ammo.m203
from div_9id.units import AA, AIR, ART, HEL, INF, LOG, REC, TNK, transports
from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.metadata.division import DivisionMetadata
from warno_mfw.metadata.mod import ModMetadata
from warno_mfw.metadata.warno import WarnoMetadata
from warno_mfw.unit_registration.division_unit_registry import DivisionUnitRegistry
from warno_mfw.unit_registration.unit_group import UnitGroup
from warno_mfw.utils.bat import generate_mod, reset_source_for
from warno_mfw.utils.types.message import Message

wn_metadata = WarnoMetadata(rf"C:\Program Files (x86)\Steam\steamapps\common\WARNO")
mod_metadata = ModMetadata('dninemfive', '9th Infantry Division (HTMD)', wn_metadata, "0.0.0", 'd9', 'd99ID')
div_metadata = DivisionMetadata('d9', '9ID', 'US', 1390)

reset_source_for(mod_metadata)

with Message(f"Creating mod {mod_metadata.name} by {mod_metadata.author}") as root_msg:
    with ModCreationContext(mod_metadata, root_msg) as mod_context:
            div_9id.ammo.fgr_17_viper.create(mod_context)
            div_9id.ammo.m60e3.create(mod_context)
            div_9id.ammo.m203.create(mod_context)
            division_units: DivisionUnitRegistry
            with root_msg.nest("Creating units") as msg:
                division_units = DivisionUnitRegistry(mod_context,
                                                      div_metadata,
                                                      root_msg,
                                                      "US_82nd_Airborne",
                                                      "US_8th_Inf",
                                                      "US_11ACR",
                                                      "US_3rd_Arm",
                                                      "NATO_Garnison_Berlin",
                                                      "US_101st_Airmobile",
                                                      "UK_2nd_Infantry",
                                                      "FR_11e_Para",
                                                      "RFA_5_Panzer",
                                                      "RFA_2_PzGrenadier",
                                                      "FR_5e_Blindee",
                                                      "US_24th_Inf",
                                                      "SOV_76_VDV")
                # make new units  
                _ = transports.Transports(mod_context)
                for category in [LOG, INF, ART, TNK, REC, AA, HEL, AIR]:
                    group: Callable[[DivisionUnitRegistry, Message], UnitGroup] = getattr(category, 'group')
                    group(division_units, msg).register_all()                
            # make division
            division_texture_name: str = mod_context.add_division_emblem(root_msg, "img/patch/icon.png", div_metadata) 
            mod_context.create_division(div_metadata,
                                        "Descriptor_Deck_Division_US_82nd_Airborne_multi",
                                        division_units,
                                        "Descriptor_Deck_Division_US_8th_Inf_multi",
                                        root_msg,
                                        DivisionName=mod_context.localization.register("9TH INFANTRY DIVISION (HTMD)"),
                                        DescriptionHintTitleToken=mod_context.localization.register("9TH INFANTRY DIVISION (HTMD)"),
                                        EmblemTexture = division_texture_name)
            # add a default deck to Decks.ndf (not required)
    
    generate_mod(mod_metadata, root_msg)
print(f"Generation finished at {datetime.now().time()}")