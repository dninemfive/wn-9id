from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.utils.ndf import ensure


def create(ctx: ModCreationContext) -> str:
    with ctx.create_ammo('Ammo_d9_M60E3', 'Ammo_MMG_M60_7_62mm') as creator:
        creator.edit_members(Name=ctx.localization.register('M60E3'),
                             TraitsToken=["'MOTION'", "'CAC'"],
                             PorteeMinimaleGRU=None)
        creator.object.by_member('HitRollRuleDescriptor').value\
                      .by_member('BaseHitValueModifiers').value\
                            = ensure.NdfList(('EBaseHitValueModifier/Base', 0),
                                           ('EBaseHitValueModifier/Idling', 35),
                                           ('EBaseHitValueModifier/Moving', 10),
                                           ('EBaseHitValueModifier/Targeted', 0))