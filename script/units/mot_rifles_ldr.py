from context.module_context import ModuleContext
from context.unit_creation_context import UnitCreationContext
from metadata.deck_unit_info import TDeckUniteRule
from misc.unit_creator import UNIT_UI
from ndf_parse.model import List

def create(ctx: UnitCreationContext) -> tuple[tuple[str, int], TDeckUniteRule]:
    # ✪ MOT. RIFLES LDR.
    # copy: Airborne Ldr.
    with ctx.create_unit("MOT. RIFLES LDR.", "US", "Airborne_CMD_US") as mot_rifles_ldr:
        # reduce men to 8
        # remove Shock and Airborne traits
        # remove forward deploy
        # reduce cost
        # change TTypeUnitModuleDescriptor:TypeUnitFormation from Supply?

        rule = TDeckUniteRule(
            mot_rifles_ldr.new.descriptor_path,
            AvailableWithoutTransport=False,
            # TODO: decide on transports
            AvailableTransportList=["$/GFX/Unit/Descriptor_Unit_M998_Humvee_US"],
            # TODO: automatically get this from Airborne CMD
            NumberOfUnitInPack=6,
            # unit rule xp should also be higher
            NumberOfUnitInPackXPMultiplier=[0, 1, 0.6, 0]
        )
        return ((mot_rifles_ldr.new.deck_pack_descriptor_path, 2), rule)
        