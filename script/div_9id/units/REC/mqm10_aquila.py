from warno_mfw.context.mod_creation import ModCreationContext
from warno_mfw.unit_registration.new_src_unit_pair import NewSrcUnitPair
from warno_mfw.utils.ndf import ensure

FLIGHT_ALTITUDE = 706 # = 3000 / 3.2 * METRE
                     # weird discrepancy: 706 for LowAltitudeFlyingAltitude, but 494 for Altitude
FLIGHT_SPEED = 200
DRAGONFLY = 'A37B_Dragonfly_US'
SCHMEL = 'Pchela_1T_SOV'

def create(ctx: ModCreationContext) -> NewSrcUnitPair:
    with ctx.create_unit("#RECO2 MQM-10 AQUILA", "US", SCHMEL, button_texture_src_path='img/units/rq_2_pioneer/icon.png') as mqm_10_aquila:
        mqm_10_aquila.unit.set_country('US')
        ctx.get_unit(DRAGONFLY).modules.ui.UpgradeFromUnit = mqm_10_aquila
        return mqm_10_aquila