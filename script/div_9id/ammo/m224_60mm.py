from __future__ import annotations

from mw2.context.mod_creation import ModCreationContext


def create(ctx: ModCreationContext) -> str:
    # copy 81mm mortar                          Ammo_Mortier_81mm
    # use HE value from 60mm mortar on AMLs?    Ammo_Canon_HE_60mm_CM60A1
    # reduce range proportionally
    # increase fire rate, decrease supply cost
    with ctx.create_ammo('Ammo_d9_M224_M720_HE_60mm', 'Ammo_Mortier_81mm') as creator:
        creator.edit_members(Name=ctx.localization.register('M224 (M720 HE)'),
                             Caliber=ctx.localization.register('60mm'),
                             PorteeMaximaleTBAGRU=4925)
        
# TODO: M722 Smoke