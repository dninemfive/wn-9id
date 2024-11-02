from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.utils.ndf import ensure


def create(ctx: ModCreationContext) -> str:
    # add small amount of AP?
    with ctx.create_ammo('Ammo_d9_40mm_HEDP', 'Ammo_Lance_grenade_Mk19_40mm') as creator:
        creator.edit_members(Name=ctx.localization.register('M203'),
                             TraitsToken=["'STAT'", "'HE'"],
                             PorteeMaximaleGRU=850,
                             NbTirParSalves=1,
                             AffichageMunitionParSalve=1)
        creator.object.by_member('HitRollRuleDescriptor').value\
                      .by_member('BaseHitValueModifiers').value\
                            = ensure._list(('EBaseHitValueModifier/Base', 0),
                                           ('EBaseHitValueModifier/Idling', 45),
                                           ('EBaseHitValueModifier/Moving', 0),
                                           ('EBaseHitValueModifier/Targeted', 0))